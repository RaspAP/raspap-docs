# Minimal SD card write

![](https://user-images.githubusercontent.com/229399/227795437-42d9c102-c05e-4eea-88cc-3c9e81de44ad.jpg){: style="width:640px"}

## Overview
Linux, and indeed most substantial operating systems, is frequently writing logs files, cache files and temporary data to disk (or the microSD card with the Raspberry Pi). Performing a shutdown puts these files away into a known valid state. If power is unexpectedly cut to a Raspberry Pi, these unwritten system files can become corrupted and render a card unbootable.

What is more, most microSD cards were not designed with 24/7 operation in mind. Continuous writing to the card's flash memory shortens its lifespan. They often accumulate bad sectors rather quickly after a period of extended use. This is particularly true of so-called "budget" microSD cards.

Using a Raspberry Pi as an access point requires reliable operation over a long period of time. While "read-only mode" operation for the SD card is one approach to prolong its use, this prevents user settings from being persisted to storage &#151; meaning that any changes will be lost if the device is disconnected from power. This makes it less than ideal for RaspAP, or indeed any application such as a web server or database that depends on persistent storage.

## Solution
Rather than force the system into a read-only mode, RaspAP has an alternative "minimal write mode" that substantially reduces the risk of SD card corruption and also helps to extend the card's lifespan.

This solution involves moving logging, cache and temporary data to a RAM-based file system. The default system log processor `rsyslog` is replaced with an in-memory logger and several log-related services are disabled. The `tmpfs` filesystem is used for most processes that require write access, such as sessions used by `php-cgi`, as well as paths for transient and cache data including `/var/cache` and `/var/tmp`.

In addition, the system's boot options are modified to disable swap and file system checks. A tangible side benefit of retaining a read/write boot partition is that your system will behave otherwise normally &#151; you may install packages, add services and perform most operations as before.

## Enabling minimal write
The minimal microSD card write utility, **minwrite**, may be invoked by using RaspAP's [Quick installer](quick.md). This does _not_ (re)install RaspAP &#151; only the [minwrite](https://github.com/RaspAP/raspap-webgui/blob/master/installers/minwrite.sh) shell script is loaded and executed. Users of this method are informed of which operations are performed at each step. Alternatively, [manual configuration](#manual-steps) steps are also provided. Notes specific to Armbian are given where applicable.

!!! warning "Warning"
    These methods have been used successfully with many Debian-based systems. However, you still use this at your own risk. We recommend either creating a backup image of your SD card before proceeding, or begin with a baseline setup that you can easily recreate if needed.

Both methods are reasonably straightforward. Bear in mind that RAM usage on your device will necessarily increase, since we'll be migrating the disk I/O activity of several system processes to the `tmpfs` ramdisk. For this reason, it's recommended to review the [memory considerations](#memory-considerations) before proceeding.

After we've enabled **minwrite** we'll look at a technique to evaluate its effectiveness.

### Quick install
The [minwrite utility](https://github.com/RaspAP/raspap-webgui/blob/master/installers/minwrite.sh) may be invoked remotely from the [Quick installer](quick.md) like so:

```
curl -sL https://install.raspap.com | bash -s -- --minwrite
```

Alternatively, if you have a local install of RaspAP you may execute it from the `/installers` directory like so:

```
./raspbian.sh --minwrite.sh
```

You will be prompted at each step during the minwrite script's execution. As a final step, be sure to reboot your system.

```
$ curl -sL https://install.raspap.com | bash -s -- --minwrite


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
Additionally, `dphys-swapfile`, which manages a swapfile in the root filesystem on the SD card, is removed as it won’t be able to work.

Remove these packages with the following:

```
sudo apt-get remove --purge dphys-swapfile logrotate
sudo apt-get autoremove --purge
```

#### Disable services
Linux is able to update packages autonomously without an external command. This task is scheduled by the `apt-daily.service`, which triggers the system to start `apt` tasks and scan installed packages for available updates. If updates are found, the `apt-daily-upgrade.service` downloads and installs them without user intervention. While useful for keeping your system updated, these are intensive processes in terms of disk I/O that we can safely disable and handle manually.

Disable the `bootlogd.service`, `apt-daily` and related services like so:

```
sudo systemctl unmask bootlogd.service
sudo systemctl disable bootlogs
sudo systemctl disable apt-daily.service apt-daily.timer apt-daily-upgrade.timer apt-daily-upgrade.service
```
!!! note "Note"
    By disabling these services, you will need to manually check for package updates periodically with `sudo apt-get update && sudo apt-get upgrade`.

#### Replace logger
In this step we'll replace the default system logger `rsyslog` with an in-memory logger, `busybox-syslogd`. [BusyBox](https://manpages.debian.org/jessie/busybox-syslogd/syslogd.8.en.html) combines tiny versions of many common Linux utilities into a single small executable. It provides a fairly complete POSIX environment for any small or embedded system, including a minimal write Raspberry Pi.

Install it like so and remove `rsyslog`:

```
sudo apt-get install busybox-syslogd
sudo dpkg --purge rsyslog
```

Be aware that because `busybox-syslogd` writes system logs to RAM, these logs will be lost if your device is disconnected from power.

#### Disable swap
Next we'll modify system boot options to disable [swap](https://wiki.debian.org/Swap) and filesystem checks, as these are both intensive disk I/O processes. Edit this file with `sudo nano /boot/cmdline.txt` and append the following to the end:

```
fsck.mode=skip noswap
```

The resulting file will look something like this (copied from a Pi 3 Model B+):

```
console=serial0,115200 console=tty1 root=PARTUUID=bddffae9-02 rootfstype=ext4 fsck.repair=yes rootwait fsck.mode=skip noswap
```

Save your changes and quit out of the editor with ++ctrl+x++ followed by ++y++ and finally ++enter++.

!!! note "Note"
    By default Armbian does not use any SD card-based swap, so unless you’ve customized your installation there’s nothing to disable.

#### Move directories to RAM
As a final step, we'll move several directories to the `tmpfs` filesystem. By storing these directories on a ramdisk instead of the SD card, we can substantially reduce the volume of I/O operations on the card's flash memory. Writing to `tmpfs` also provides fast sequential read/write speeds. The tradeoff is that `tmpfs` is _volatile storage_ &#151; meaning that you will lose all data stored on the filesystem if you lose power.

We'll select paths to migrate to `tmpfs` for transient and cache data, as well as those required for RaspAP's operation that are associated with disk I/O activity. Moving these directories to `tmpfs` is done by editing `fstab` with `sudo nano /etc/fstab`. Append the following lines to the end:

```
tmpfs /tmp tmpfs  nosuid,nodev 0 0
tmpfs /var/log tmpfs  nosuid,nodev 0 0
tmpfs /var/tmp tmpfs  nosuid,nodev 0 0
tmpfs /var/lib/misc tmpfs  nosuid,nodev 0 0
tmpfs /var/cache tmpfs  nosuid,nodev 0 0
tmpfs /var/lib/vnstat tmpfs  nosuid,nodev 0 0
tmpfs /var/php/sessions tmpfs  nosuid,nodev 0 0
```

Save your changes and quit out of the editor with ++ctrl+x++ followed by ++y++ and finally ++enter++.

!!! note "Note"
    Armbian puts `/tmp` in RAM by default, while Raspberry Pi OS does not. On both Armbian and Raspberry Pi OS, `/run` is stored in RAM already and `/var/run` symlinks to it. 

The `/var/tmp` directory is made available for programs that require temporary files or directories that are preserved between system reboots. Therefore, data stored in `/var/tmp` is more persistent than data in `/tmp`. In practice, however, few programs in common use with Raspberry Pi OS write to this directory so we can safely move it to RAM. 

#### Reboot
A reboot is required for the above steps to take effect: `sudo reboot`.

## Memory considerations
The **minwrite** configuration migrates as much as possible from SD card storage to the `tmpfs` ramdisk. As a result, a concomitant increase in memory utilization is expected. To benchmark this, we can compare the change in memory usage on a Pi 3 Model B+ with 1GB of RAM with a typical RaspAP installation.

Here we use the following to return the amount of free system memory expressed as a percentage of total available:

```
free -m | awk '/Mem:/ { total=$2 ; used=$3 } END { print used/total*100}'
```

| Pre-minwrite | Post-minwrite            |
| ------------ | -------------------------|
| 11.88%       | :material-check:  29.70% |

While this is a noticable increase in RAM usage, it's still well within the margin for reliable operation of the OS. If you have a higher rate of RAM utilization on your device, or have limited available system memory to begin with, bear this in mind before proceeding.

!!! note "Note"
    Recall that we've disabled swap, so if the system runs out of physical memory (RAM) there is no partition available for the kernel to allocate virtual memory in its place. This will cause the kernel to throw an out of memory (OOM) error. Normally this causes the kernel to panic and stop functioning. 

## File system metrics
We can evaluate a **minwrite** configuration by using `iotop`, a utility that watches I/O usage information output by the Linux kernel. Install it like so:

```
sudo apt-get install iotop
```

Execute it with the following switches to monitor accumulated activity of processes doing actual I/O:

```
sudo iotop -aoP
```

After a period of time, you will see disk I/O activity reported for a number of processes. Returning to our Pi 3 Model B+ test bench, we can compare the before and after results: 

**Pre-minwrite I/O**
```
Total DISK READ:         0.00 B/s | Total DISK WRITE:       191.31 B/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:      22.52 K/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
     95 ?sys root          0.00 B    860.00 K	              [jbd2/mmcblk0p2-]
    145 ?sys root          0.00 B      3.03 M				  systemd-journald
    412 ?sys root          0.00 B    112.00 K 				  rsyslogd -n -iNONE
    529 ?sys vnstat        0.00 B    264.00 K				  vnstatd -n
   1080 ?sys www-data    800.00 K     48.00 K				  lighttpd -D -f /etc/lighttpd/lighttpd.conf
   1186 ?sys www-data      2.25 M      0.00 B				  php-cgi
   1187 ?sys www-data      4.00 K      0.00 B				  php-cgi
   1188 ?sys www-data     52.00 K      0.00 B				  php-cgi
   4752 ?sys root          0.00 B      4.00 K				  dhcpcd -w -q
   5402 ?sys dnsmasq       0.00 B    140.00 K				  dnsmasq -x /run/dnsmasq/dnsmasq.pid
```

**Post-minwrite I/O**
```
Total DISK READ:         0.00 B/s | Total DISK WRITE:         0.00 B/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       0.00 B/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
    101 ?sys root          0.00 B      8.00 K  				  [jbd2/mmcblk0p2-8]
    837 ?sys www-data     24.00 K      0.00 B				  lighttpd -D -f /etc/lighttpd/lighttpd.conf
    890 ?sys www-data    170.00 K      0.00 B				  php-cgi
    891 ?sys www-data      4.00 K      0.00 B				  php-cgi
    892 ?sys www-data      4.00 K      0.00 B 			      php-cgi
    893 ?sys www-data     80.00 K      0.00 B 	              php-cgi
```

Notice that in the latter `iotop` output, logging to disk is nearly absent and `vnstatd` now writes data to RAM. The remaining disk write activity originates mainly from the ext4 journal update process `jbd2`.

At the same time, RaspAP settings may be modified and persisted to the microSD card and the system otherwise operated normally.

## Discussions
Questions or comments about using **minwrite** mode? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).

