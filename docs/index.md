# Overview

![RaspAP-banner](https://user-images.githubusercontent.com/229399/164047475-6d8cf1fd-ec50-4fcc-9d36-f0385f819979.png)

Simple AP setup & WiFi management for Debian-based devices

## About
RaspAP is feature-rich wireless router software that _just works_ on many popular [Debian-based devices](#compatible-operating-systems), including the Raspberry Pi.
Our popular [Quick installer](quick.md) and [Docker container](docker.md) create a known-good default configuration in minutes on all current Raspberry Pis with onboard wireless.

## Quick start
Start with a clean install of the [latest release of Raspberry Pi OS Lite](https://www.raspberrypi.org/software/operating-systems/). Both the 32- and 64-bit release versions are supported, as well as the latest 64-bit Desktop distribution. Consult [this FAQ](faq.md#distros) before installing RaspAP in a desktop environment.



!!! tip "Tip"
    Be sure to use an official power supply with your device. Power supply requirements [differ by Raspberry Pi model](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#power-supply). Inadequate voltage is the source of many WiFi issues.

Update RPi OS to its latest version, including the kernel and firmware, followed by a reboot:

```
sudo apt-get update
sudo apt-get full-upgrade
sudo reboot
```
Set the WiFi country in raspi-config's **Localisation Options**: `sudo raspi-config`.

!!! warning "Important"
    Failure to perform this step will prevent the RPi from enabling wireless operation. When this happens, you will see the warning `Wi-Fi is currently blocked by rfkill` in the console.

Install RaspAP from your device's shell prompt:
```sh
curl -sL https://install.raspap.com | bash
```
The [Quick installer](quick.md) will complete the steps in the [manual installation](manual.md) for you.

After the reboot at the end of the installation the wireless AP network will be configured as follows:

  **IP address:** 10.3.141.1  
  **Username:** admin  
  **Password:** secret  
  **DHCP range:** 10.3.141.50 to 10.3.141.254  
  **SSID:** `raspi-webgui`  
  **Password:** ChangeMe  

It's _strongly recommended_ that your first post-install action is to change the default admin [authentication](authentication.md) settings. Thereafter, your AP's [basic settings](ap-basics.md) and many [advanced options](ap-basics.md#advanced-options) are now ready to be modified by RaspAP.

!!! tip "Tip"
    If this is _not_ a clean install or you are configuring a device with a non-standard [integration](faq.md#integrations) try following the [manual installation](manual.md) instructions or deploy RaspAP in a [Docker container](docker.md).

## Get Insiders
RaspAP is free software, but powered by your support. If you find RaspAP useful for your personal or commercial projects, [become a sponsor](insiders.md#how-to-become-a-sponsor)
and get access to [exclusive features](insiders.md#whats-in-it-for-me) in the :octicons-heart-fill-24:{: .heart } [Insiders Edition](insiders.md).

## Compatible operating systems
RaspAP was originally made for Raspbian, but now also installs on the following Debian-based distros.

| Distribution | Release  | Architecture | Support |
|---|:---:|:---:|:---:|
| Raspberry Pi OS | (64-bit) Lite Bookworm | ARM | Official |
| Raspberry Pi OS | (32-bit) Lite Bookworm | ARM | Official |
| Raspberry Pi OS | (64-bit) Desktop Bookworm | ARM | Official |
| Raspberry Pi OS | (64-bit) Lite Bullseye | ARM | Official |
| Raspberry Pi OS | (32-bit) Lite Bullseye | ARM | Official |
| Armbian | 23.11  (Jammy) | [ARM](https://www.armbian.com/rpi4b/) | Beta |
| Debian  |  Bookworm | ARM / x86_64  | Beta |
| Ubuntu  |  Server 23.04 (Lunar) | ARM / x86_64  | Beta |

![](https://github.com/RaspAP/raspap-webgui/assets/229399/6fe62f2d-631a-46c9-8ceb-83ebf0ade6a9){: style="width:480px"}

You are also encouraged to use RaspAP's community-led [Docker container](docker.md).

Please note that "supported" is not a guarantee. If you are able to improve support for your preferred distro, we encourage you to [actively contribute](#get-involved) to the project.

## Get involved
We welcome all users of RaspAP to contribute to the project. This can take the form of [issue reports](https://github.com/RaspAP/raspap-webgui/issues), [discussions](https://github.com/RaspAP/raspap-webgui/discussions), or [pull requests](https://github.com/RaspAP/raspap-webgui/pulls).
Developers can get started by following these steps:

1. Fork the project in your account and create a new branch: `your-great-feature`.
2. Open an issue in the repository describing the feature contribution you'd like to make.
3. Commit changes in your feature branch.
4. Open a pull request and reference the initial issue in the pull request message.

Find out more about our [coding style guidelines and recommended tools](https://github.com/RaspAP/raspap-webgui/blob/master/CONTRIBUTING.md).

## Discussions
Questions or comments about the Quick start? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).

