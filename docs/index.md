# Overview

![](https://camo.githubusercontent.com/4ab9f14ff0d3e36887b0264e7c2ea5b8daac1450a46e1fa29161f6a0362a3fe3/68747470733a2f2f692e696d6775722e636f6d2f556467444b50692e706e67)

Simple AP setup & WiFi management for Debian-based devices

## About
RaspAP lets you quickly get a WiFi access point up and running to share the connectivity of many popular Debian-based devices, including the Raspberry Pi.
Our popular Quick installer creates a known-good default configuration that "just works" on all current Raspberry Pis with onboard wireless.

## Quick start
Start with a clean install of the [latest release of Raspberry Pi OS (32-bit) Lite](https://www.raspberrypi.org/downloads/raspbian/). The Raspberry Pi OS desktop and 64-bit beta distros are unsupported.

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
The [Quick installer](/quick/) will complete the steps in the [manual installation](/manual/) for you.

After the reboot at the end of the installation the wireless AP network will be configured as follows:

  IP address: 10.3.141.1  
  Username: admin  
  Password: secret  
  DHCP range: 10.3.141.50 to 10.3.141.255  
  SSID: `raspi-webgui`  
  Password: ChangeMe  

## Compatible operating systems
RaspAP was originally made for Raspbian, but now also installs on the following Debian-based distros.

| Distribution | Release  | Architecture | Support |
|---|:---:|:---:|:---:|
| Raspberry Pi OS | (32-bit) Lite Buster | ARM | Official |
| Armbian | Buster | [ARM](https://docs.armbian.com/#supported-chips) | Official |
| Debian  |  Buster | ARM / x86_64  | Beta |
| Ubuntu  |  18.04 LTS / 19.10 | ARM / x86_64  | Beta |

Please note that "supported" is not a guarantee. If you are able to improve support for your preferred distro, we encourage you to [actively contribute](#get-involved) to the project.

## Get involved
We welcome all users of RaspAP to contribute to the project. This can take the form of [issue reports](https://github.com/billz/raspap/issues), [discussions](https://github.com/billz/raspap/discussions), or [pull requests](https://github.com/billz/raspap/pulls).
Developers can get started by following these steps:

1. Fork the project in your account and create a new branch: `your-great-feature`.
2. Open an issue in the repository describing the feature contribution you'd like to make.
3. Commit changes in your feature branch.
4. Open a pull request and reference the initial issue in the pull request message.

Find out more about our [coding style guidelines and recommended tools](https://github.com/billz/raspap/blob/master/CONTRIBUTING.md).

## Support us
RaspAP is free software, but powered by your support. If you find RaspAP useful for your personal or commercial projects, [become a GitHub sponsor](https://github.com/sponsors/RaspAP) or join the project on [Open Collective](https://opencollective.com/raspap). 100% of financial contributions go to activities directly related to this project.

