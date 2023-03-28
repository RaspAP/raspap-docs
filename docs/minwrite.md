# Minimal SD card write

![](https://user-images.githubusercontent.com/229399/227795437-42d9c102-c05e-4eea-88cc-3c9e81de44ad.jpg){: style="width:640px"}

## Overview
Linux, and indeed most substantial operating systems, is frequently writing logs files, cache files and temporary data to disk (or the microSD card with the Raspberry Pi). Performing a shutdown puts these files away into a known valid state. If power is unexpectedly cut to a Raspberry Pi, these unwritten system files can become corrupted and render a card unbootable.

What is more, most microSD cards were not designed with 24/7 operation in mind. Continuous writing to the card's flash memory shortens its lifespan. They often accumulate bad sectors rather quickly after a period of extended use. This is particularly true of so-called "budget" microSD cards.

Using a Raspberry Pi as an access point requires reliable operation over a long period of time. While "read-only mode" operation for the SD card is one approach to prolong its use, this prevents user settings from being persisted to storage &#151; meaning that any changes will be lost following a reboot. This makes it less than ideal for RaspAP, or indeed any application such as a web server or database that depends on read/write tasks.

## Solution
Rather than force the system into a read-only mode, RaspAP has an alternative "minimal write mode" that _substantially_ reduces the risk of SD card corruption and also helps to extend the card's lifespan.

This solution involves moving logging and temporary data to a RAM-based file system. The default system log processor `rsyslog` is replaced with an in-memory logger and several log-related services are disabled. A `tmpfs` filesystem is provided for services that require write access, such as sessions used by `php-cgi`, as well as paths for transient and cache data including `/var/cache` and `/var/tmp`.

In addition, the system's boot options are modified to disable swap and file system checks. A tangible side benefit of retaining a read/write boot partition is that your system will behave otherwise normally &#151; you may install packages, add services and perform most operations as before.

## Enabling minimal write
The minimal microSD card write utility, **minwrite**, may be invoked by using RaspAP's [Quick installer](quick.md). This does _not_ (re)install RaspAP &#151; only the [minwrite](https://github.com/RaspAP/raspap-webgui/blob/master/installers/minwrite.sh) shell script is loaded and executed. Users of this method are informed of which operations are performed at each step. Alternatively, manual configuration steps are also provided. 

> :information_source: **Important**: These methods have been used successfully with many systems. However, you still use this at your own risk. We recommend either creating a backup image of your SD card
before proceeding, or begin with a baseline setup that you can easily recreate if needed. 

Both methods are reasonably straightforward. After we've enabled **minwrite** we'll look at a technique to evaluate its effectiveness.

### Quick install
The [minwrite utility](https://github.com/RaspAP/raspap-webgui/blob/master/installers/minwrite.sh) may be invoked remotely from the [Quick installer](quick.md) like so:

```
curl -sL https://install.raspap.com | bash -s --minwrite
```

Alternatively, if you have a local install of RaspAP you may execute it from the `/installers` directory like so:

```
./raspbian.sh --minwwrite.sh
```

You will be prompted at each step during the minwrite script's execution. As a final step, be sure to reboot your system.

```
$ curl -sL https://install.raspap.com | bash -s --minwrite


 888888ba                              .d888888   888888ba
 88     8b                            d8     88   88     8b
a88aaaa8P' .d8888b. .d8888b. 88d888b. 88aaaaa88a a88aaaa8P
 88    8b. 88    88 Y8ooooo. 88    88 88     88   88
 88     88 88.  .88       88 88.  .88 88     88   88
 dP     dP  88888P8  88888P  88Y888P  88     88   dP
                             88
                             dP      version 2.8.8

The Quick Installer will guide you through a few easy steps


RaspAP Minwrite: Modify the OS to minimize microSD card write operation
Detected OS: Debian GNU/Linux 11 (bullseye)
RaspAP Minwrite: Removing packages
The following packages will be removed: dphys-swapfile logrotate
Proceed? [Y/n]:
The following packages will be REMOVED:
  dphys-swapfile* logrotate*
0 upgraded, 0 newly installed, 3 to remove and 65 not upgraded.
After this operation, 351 kB disk space will be freed.
(Reading database ... 65355 files and directories currently installed.)
Removing dphys-swapfile (20100506-7+rpt1) ...
Removing logrotate (3.18.0-2+deb11u1) ...
Processing triggers for man-db (2.9.4-2) ...
(Reading database ... 65313 files and directories currently installed.)
Purging configuration files for logrotate (3.18.0-2+deb11u1) ...
Purging configuration files for dphys-swapfile (20100506-7+rpt1) ...
[ ✓ ok ]
RaspAP Minwrite: Disabling services
The following services will be disabled: bootlogd.service bootlogs console-setup apt-daily
Proceed? [Y/n]:
```

### Manual steps 
These steps perform the same actions as the Quick install method. Details are provided so that you may choose to customize or skip some steps, if desired.

#### Remove packages
The goal here is to only remove packages that actively write to the filesystem, and that we intend to replace or disable entirely. In a subsequent step, `logrotate` will be replaced with `busybox-syslogd`.
Additionally, `dphys-swapfile`, which manages a swapfile in the root filesystem on the SD card, won’t be able to work.

Remove these packages like so:

```
sudo apt-get remove --purge dphys-swapfile logrotate
sudo apt-get autoremove --purge
```

#### Disable services
Several services are disabled here, including those related to logging such as `bootlogd.service`. In additon, `apt-daily` and several related services are disabled.

In Linux, the system is able to update packages autonomously without an external command. This task is scheduled by the `apt-daily.service`, which triggers the system to start `apt` tasks and scan installed packages for available updates. If updates are found, the `apt-daily-upgrade.service` downloads and installs them without user intervention. 

Disable these services with the following:

```
sudo systemctl unmask bootlogd.service
sudo systemctl disable bootlogs
sudo systemctl disable apt-daily.service apt-daily.timer apt-daily-upgrade.timer apt-daily-upgrade.service
```

It's important to note that by disabling these services, you will need to manually check for package updates periodically with `sudo apt-get update && sudo apt-get upgrade`.

#### Replace logger
In this step we'll replace the default system logger `rsyslog` with an in-memory logger, `busybox-syslogd`. [BusyBox](https://manpages.debian.org/jessie/busybox-syslogd/syslogd.8.en.html) combines tiny versions of many common Linux utilities into a single small executable. It provides a fairly complete POSIX environment for any small or embedded system, including a minimal write Raspberry Pi.

Install it like so and remove `rsyslog`:

```
sudo apt-get install busybox-syslogd
sudo dpkg --purge rsyslog
```

Be aware that because `busybox-syslogd` writes system logs to RAM, these logs will be deleted on a reboot or if your device is disconnected from power.

#### Disable swap
Next we'll modify system boot options to disable [swap](https://wiki.debian.org/Swap) and filesystem checks. These are both intensive disk I/O operations. Edit this file with your editor of choice, for example `sudo nano /boot/cmdline.txt`. Append the following to the end of this file:

```
fsck.mode=skip noswap
```
Save your changes and quit out of the editor with ++ctrl+x++ followed by ++y++ and finally ++enter++.

#### Move directories to RAM
As a final step, we'll move several directories to the `tmpfs` filesystem. By directing write operations to a ramdisk instead of the SD card, we can substantially reduce the volume of I/O operations on the card's flash memory. Writing to `tmpfs` also provides fast sequential read/write speeds. The tradeoff is that `tmpfs` is _volatile storage_ &#151; meaning that you will lose all data stored on the filesystem if you lose power.

We'll select paths to migrate to `tmpfs` for transient and cache data, as well as those required for RaspAP's operation that are associated with disk I/O activity. Moving these directories to `tmpfs` is done by editing `fstab` with `sudo nano /etc/fstab`. Add the following lines:

```
tmpfs /tmp tmpfs  nosuid,nodev 0 0
tmpfs /var/log tmpfs  nosuid,nodev 0 0
tmpfs /var/tmp tmpfs  nosuid,nodev 0 0
tmpfs /var/lib/misc tmpfs  nosuid,nodev 0 0
tmpfs /var/cache tmpfs  nosuid,nodev 0 0
tmpfs /var/lib/vnstat tmpfs  nosuid,nodev 0 0
tmpfs /var/php/sessions tmpfs  nosuid,nodev 0 0
```

> :information_source: **Note**: Armbian puts `/tmp` in RAM by default, while Raspberry Pi OS des not. On both Armbian and Raspberry Pi OS, `/run` is stored in RAM already and `/var/run` symlinks to it. 

Save your changes and quit out of the editor with ++ctrl+x++ followed by ++y++ and finally ++enter++.

According to the Linux docs, the `/var/tmp` directory is made available for programs that require temporary files or directories that are preserved between system reboots. Therefore, data stored in `/var/tmp` is more persistent than data in `/tmp`. In practice, few programs in common use with Raspberry Pi OS write to this directory so we can safely move it to RAM. 

#### Reboot
A reboot is required for the above steps to take effect. Do so by executing `sudo reboot`.

## Memory considerations


## File system metrics


