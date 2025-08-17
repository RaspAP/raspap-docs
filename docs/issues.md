# Reporting issues

## Overview
RaspAP is free software. It is delivered to you, at no cost, and with no warranty of any kind. The [community of developers](https://github.com/RaspAP/raspap-webgui/graphs/contributors) who contribute to this project make every effort to deliver defect-free code. That said, no software is perfect. You can help us improve this project by accurately describing your issue.

## Issue policy
This project is currently led by one developer ([@billz](https://github.com/billz)) in his very limited spare time. Please respect our developers' time by using issues for reporting bugs only.
RaspAP is not a boxed product with a free troubleshooting hotline. If your issue is of a general nature and not directly related to a defect with this project, try searching the official [Raspberry Pi forums](https://www.raspberrypi.org/forums/), [RaspAP's GitHub discussions](https://github.com/RaspAP/raspap-webgui/discussions), or [Raspberry Pi on Stack Exchange](https://raspberrypi.stackexchange.com/). Chances are your question has been discussed and answered before.

Issues are only valid for _clean installs_ of this project's [compatible operating systems](index.md#compatible-operating-systems).
If you observe RaspAP behaving strangely and you did _not_ begin with a clean install, be sure to test it on a fresh SD card before reporting an issue.

The project [FAQ](faq.md) is continuously updated with answers to many common questions. Refer to this first before creating a new issue. 

## Guidelines
You can help us improve this project by accurately describing defects. To that end, these guidelines have been established to streamline the reporting process: 

1. Please read and follow the [Code of Conduct](https://github.com/RaspAP/raspap-webgui/blob/master/CODE_OF_CONDUCT.md). 
2. Provide useful detail to reproduce your issue. "Doesn't work" or "not working" is not a valid report. Here's an example [model bug report](https://github.com/RaspAP/raspap-webgui/issues/1451) and [feature request](https://github.com/RaspAP/raspap-webgui/issues/1498) [[2]](https://github.com/RaspAP/raspap-webgui/issues/1734).
3. Generate a [debug log](troubleshooting.md#debug-log) and upload the contents to a text sharing service, like [Pastebin](https://pastebin.com/). 
4. If an issue is unclear or needs further information, it will be labeled with `question` and `awaiting-user`.
5. Issues that becomes stale due to inactivity are automatically managed by stale-bot.

## Supported devices 
RaspAP functions very well "out of the box" on fresh installs of the latest RPi OS Lite 64- or 32-bit distribution with recent hardware like the RPi 4, 3B+ and Zero 2 W. The [version 2.3.1 release](https://github.com/RaspAP/raspap-webgui/releases/tag/2.3.1) extends beta support to additional Debian-based distros, including Armbian and Ubuntu Server. Please note that "supported" is [not a guarantee](index.md#compatible-operating-systems).

If you have installed other software packages on top of RaspAP, particularly those related to networking such as Pi-hole, please test RaspAP first on a clean install before reporting an issue. You may also use RaspAP's [Docker container](docker.md) to mitigate conflicts with other software packages.

## External hardware
RaspAP has been rigorously tested on the above supported distros and devices using the onboard wireless chipsets. While many good external wireless USB adapters, or "dongles", are available, a
substantial number lack in-kernel driver support or are otherwise unsuitable for this project. It is not practical, or even possible, to individually test every dongle on the market with this project. 
For this reason, issues that concern external wireless adapters, or request troubleshooting of these devices, will not be considered.

If you suspect a driver problem with your USB adapter, [RaspAP tools](https://github.com/RaspAP/raspap-tools#install-missing-wlan-driver-modules) 
can assist you with installing missing WLAN driver modules. Beyond this, your best avenue for troubleshooting are the public forums mentioned above.

## Default settings
One of RaspAP's most popular features is the [Quick Installer](quick.md), which gets an AP up and running quickly and with a minimum of hassle. This works by applying a known-good [default configuration](defaults.md) that has been validated in testing with the project's supported devices. When the project [prerequisites](index.md#quick-start) are followed, an AP with wired ethernet (`eth0`) or managed mode (`wlan0`) Wifi client AP will be functional with the default settings.

!!! warning "Important"
    RaspAP gives you control over many of the settings for `hostapd`, `dhcpcd` and `dnsmasq`. Once these default settings are changed, it's possible that one or all of the above services will enter a failed state.

## Will RaspAP let me create a configuration that "breaks" my hotspot?
In a word, yes. While the [Quick Installer](quick.md) automates most of the work of creating an AP, RaspAP does not automagically validate your custom configurations. As a result, you may observe anomalous behavior when restarting these services and/or rebooting your device.

When in doubt, you may perform a [system reset](defaults.md#restoring-settings) to restore the default settings.

Because of this, issues such as "hotspot isn't working" or "gui doesn't work" won't be considered. No hard feelings. 

## Submitting an issue
If, after searching these community forums, consulting the [FAQ](faq.md) and understanding the default settings, your issue still persists, please provide as much detailed information as possible. Use the provided issue template. Incomplete issue reports will not be considered. 
Thanks.

