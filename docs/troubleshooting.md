# Troubleshooting

## Overview
RaspAP gives you advanced control over several Linux networking-related services. Likewise, devices such as the Raspberry Pi let you attach peripherals and adapters to extend the hardware in countless ways. As a result, your AP may fail to start for a variety of reasons. You may also observe your AP "disappearing," encounter errors connecting clients to the AP, have no internet connectivity on AP clients, or observe clients being disconnected for no apparent reason.

## Do's and don'ts
Is your RaspAP router behaving unexpectedly? Before proceeding any further, this common sense checklist will help you avoid the most common pitfalls:

1. _Do_ use a [custom OS with RaspAP preinstalled](quick_start.md#pre-built-image); this eliminates 90% of the guesswork.
2. _Don't_ use a metallic case with your device, which can impede radio performance.
3. _Do_ start with your device's onboard wireless and validate operation with it ^^first^^.
4. _Don't_ attach an [external wireless adapter](faq.md#adapters) (or "dongle") and assume it will work.
5. _Do_ use an official power supply for your device to avoid undervoltage errors.
6. _Don't_ attach USB peripherals without a powered hub (see #5).
7. _Do_ perform a survey of your wireless neighborhood to avoid [co-channel interference](faq.md#ping).
8. _Do_ use a microSD card from a reputable brand; consider enabling [minwrite mode](minwrite.md).
9. If you've modified the default settings and things don't work, do a [system reset](defaults.md#restoring-settings).
10. Still not working? Generate a debug log and perform a _self-diagnosis_ (do _NOT_ post the log output unless asked).

Follow this checklist and read the docs before starting another "doesn't work" discussion. New threads and issues that ignore these common sense points will be moderated. No hard feelings.

## Service logging
If your RaspAP router behaves unexpectedly, one of the best diagnostic tools at your disposal is the built-in service logging facility. You may enable the `hostapd` service log by sliding the **Logfile output** toggle on the **Hotspot > Logging** tab and choosing **Save settings**. Finally, choose
**Restart hotspot** and check the log output.

![](https://user-images.githubusercontent.com/229399/116439036-5c56b080-a84f-11eb-87ee-318932347daf.png){: style="width:580px"}

Similarly, you may also enable DHCP server activity by sliding either of the two logging options on the **DHCP server > Logging** tab. Many of RaspAP's optional components have a **Logging** or **Status** tab that provide useful diagnostic information.

## Debug log
In some situations, you may need more comprehensive information to diagnose a problem. RaspAP lets you generate a debug log with a detailed summary of your system including the installed OS, Linux kernel version, attached USB devices, RaspAP settings, network configuration and current state of several AP-related services.

![](https://github.com/RaspAP/raspap-webgui/assets/229399/66bf5cb5-3d77-44aa-92b8-5ebca6f003ad){: style="width:480px"}

To create this log, simply click or tap on the **Generate debug log** button from the **System > Tools** tab. You will be prompted to choose a location to store the generated `raspap_debug.log` file on your local computer or mobile device. An example portion of RaspAP's debug log is shown below:

```
System Info
===========
Hardware: Raspberry Pi 3 Model B Rev 1.2
Detected OS: Debian GNU/Linux 12 (bookworm) 64-bit
Kernel: Linux raspberrypi 6.1.0-rpi4-rpi-v8 (2023-10-05) aarch64 GNU/Linux
System Uptime: 4 days, 20 hours, 45 minutes
Memory Usage: 29.0749%

Installed Packages
==================
PHP Version: 8.2.7 (cli) (built: Jun  9 2023 19:37:27) (NTS)
Dnsmasq Version: 2.89
dhcpcd Version: 9.4.1
lighttpd Version: 1.4.69
vnStat Version: 2.10

RaspAP Install
==============
RaspAP Version: 2.9.9
RaspAP Installation Directory: /var/www/html
RaspAP hostapd.ini contents:
WifiInterface = wlan0
```

!!! warning "Important"
    RaspAP's service logs and debug log are intended to assist you with performing a _self-diagnosis_. Please do _not_ post your logs, in whole or in part, to RaspAP's discussions, issues or other channels. The maintainers of RaspAP [cannot parse your log or offer troubleshooting advice](issues.md#issue-policy). Members of the RaspAP community may be able to offer advice, but bear in mind that you're asking someone else to give up their time and help you figure out why something isn't working.

!!! tip "Tip"
    If you're unable to diagnose a problem, you can share your debug log with another party by uploading it to <a href="https://pastebin.com/" target="_blank">Pastebin</a>.

RaspAP's debug log contains information about your system and local network configuration. However, no passwords or other senstive data are included.

## Diagnosing problems
Look for any reported errors logged by the `hostapd`, `dhcpcd` or `dnsmasq` services. In most cases, errors thrown by one or more of these services have been discussed in various online forums.
Start by searching the official [Raspberry Pi forums](https://www.raspberrypi.org/forums/) or [Raspberry Pi on Stack Exchange](https://raspberrypi.stackexchange.com/). Chances are the problems with your AP have been discussed and answered before.

For additional help and advice, the [FAQ](faq.md) is a rich source of troubleshooting info that is continuously updated with answers to the most commonly asked questions. For issues not covered in
the FAQ, you may find many topics in [RaspAP discussions](https://github.com/RaspAP/raspap-webgui/discussions) and the [RaspAP subreddit](https://reddit.com/r/RaspAP).

!!! tip "Tip"
    Capture output from the Linux kernel's message buffer with `dmesg` to help diagnose failure events. Read the last 100 lines with `dmesg | tail -100` and look for any anomalies.

The performance of WiFi radios may be impacted by many factors, including, but not limited to:

1.  Undervoltage due to inadequate power or too many peripherals connected to the USB bus
2.  Interference from a poorly shielded HDMI cable or using a [specific HDMI screen resolution](https://www.enricozini.org/blog/2019/himblick/raspberry-pi-4-loses-wifi-at-2560x1440-screen-resolution/)
3.  RF interference from overlapping WiFi networks on a crowded 2.4 GHz band.

Bear these things in mind if your AP exhibits unexpected behavior and do your best to mitigate them.
 
## Reverting to base settings
It is generally advisable to begin with RaspAP's [default configuration](defaults.md), which has been rigorously tested and validated with the project's [supported operating systems](index.md#compatible-operating-systems). If, after modifying RaspAP's default settings, your AP no longer functions as expected, you may perform a [system reset](defaults.md#restoring-settings) to restore these defaults.

## Accessing backups
Each time you revert to RaspAP's base settings, your existing service configuration files are automatically backed up to `/etc/raspap/backups`. In this way, you can compare differences between your files and the default configuration, if needed.
There are many ways to do this in Linux, such as using the built-in GNU `diff` tool. Another option is to install `colordiff`, a wrapper for diff that produces the same output but with colored syntax highligting.
Install `colordiff` with `sudo apt-get install colordiff`.

Similarly, the web files located in the default `/var/www/html` root are backed up to `/var/www` in a directory named with a timestamp. Therefore, any changes you've made to RaspAP's internals are preserved. 

## Discussions
Questions or comments about troubleshooting? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).

