# Overview

![](https://camo.githubusercontent.com/4ab9f14ff0d3e36887b0264e7c2ea5b8daac1450a46e1fa29161f6a0362a3fe3/68747470733a2f2f692e696d6775722e636f6d2f556467444b50692e706e67)

Simple AP setup & WiFi management for Debian-based devices

## About
RaspAP is feature-rich wireless router software that _just works_ on many popular [Debian-based devices](/#compatible-operating-systems), including the Raspberry Pi.
Our popular Quick installer creates a known-good default configuration in minutes on all current Raspberry Pis with onboard wireless.

## Quick start
Start with a clean install of the [latest release of Raspberry Pi OS (32-bit) Lite](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit). The Raspberry Pi OS desktop and 64-bit beta distros are unsupported.

> :information_source: **Note**: Be sure to use an official power supply with your device. Power supply requirements [differ by Raspberry Pi model](https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md). Inadequate voltage is the source of many WiFi issues.

Update RPi OS to its latest version, including the kernel and firmware, followed by a reboot:

```
sudo apt-get update
sudo apt-get full-upgrade
sudo reboot
```
Set the WiFi country in raspi-config's **Localisation Options**: `sudo raspi-config`.

Install RaspAP from your device's shell prompt:
```sh
curl -sL https://install.raspap.com | bash
```
The [Quick installer](quick.md) will complete the steps in the [manual installation](manual.md) for you.

After the reboot at the end of the installation the wireless AP network will be configured as follows:

  **IP address:** 10.3.141.1  
  **Username:** admin  
  **Password:** secret  
  **DHCP range:** 10.3.141.50 to 10.3.141.255  
  **SSID:** `raspi-webgui`  
  **Password:** ChangeMe  

Your AP's [basic settings](ap-basics.md) and many [advanced options](ap-basics.md#advanced-options) are now ready to be modified by RaspAP.

## Get Insiders
RaspAP is free software, but powered by your support. If you find RaspAP useful for your personal or commercial projects, [become a sponsor](insiders.md#how-to-become-a-sponsor)
and get access to [exclusive features](insiders.md#exclusive-features) in the :octicons-heart-fill-24:{: .heart } [Insiders Edition](insiders.md).

## Compatible operating systems
RaspAP was originally made for Raspbian, but now also installs on the following Debian-based distros.

| Distribution | Release  | Architecture | Support |
|---|:---:|:---:|:---:|
| Raspberry Pi OS | (32-bit) Lite Buster | ARM | Official |
| Armbian | Buster | [ARM](https://docs.armbian.com/#supported-chips) | Official |
| Debian  |  Buster | ARM / x86_64  | Beta |
| Ubuntu  |  18.04 LTS / 19.10 | ARM / x86_64  | Beta |

![](https://user-images.githubusercontent.com/229399/115760318-81f03f80-a3a1-11eb-8df5-15ec4aec3e8a.png){: style="width:400px"}


Please note that "supported" is not a guarantee. If you are able to improve support for your preferred distro, we encourage you to [actively contribute](#get-involved) to the project.

## Get involved
We welcome all users of RaspAP to contribute to the project. This can take the form of [issue reports](https://github.com/RaspAP/raspap-webgui/issues), [discussions](https://github.com/RaspAP/raspap-webgui/discussions), or [pull requests](https://github.com/RaspAP/raspap-webgui/pulls).
Developers can get started by following these steps:

1. Fork the project in your account and create a new branch: `your-great-feature`.
2. Open an issue in the repository describing the feature contribution you'd like to make.
3. Commit changes in your feature branch.
4. Open a pull request and reference the initial issue in the pull request message.

Find out more about our [coding style guidelines and recommended tools](https://github.com/RaspAP/raspap-webgui/blob/master/CONTRIBUTING.md).

