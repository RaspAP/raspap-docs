# Quick start

RaspAP gives you two different ways to get up and running quickly. The simplest and recommended approach is to use a custom Raspberry Pi OS image with RaspAP preinstalled. This option eliminates guesswork and gives you a base upon which to build. Alternatively, you may execute the Quick installer on an existing [compatible OS](index.md#compatible-operating-systems). Each method is described in the following sections.

## Pre-built image
Custom Raspberry Pi OS Lite images with the latest RaspAP are available for direct download. This includes both 32- and 64-bit builds for ARM architectures. Before downloading a custom OS with RaspAP preinstalled, refer to [this resource](https://www.raspberrypi.com/software/operating-systems/) to ensure compatibility with your hardware.


| Operating system     | Debian version | Kernel version  | RaspAP version | Size  |
| ---------------------| ---------------|-----------------|----------------|-------|
| Raspberry Pi OS (64-bit) Lite | 12 (bookworm)  | 6.6    | Latest         | 871 MB|
| Raspberry Pi OS (32-bit) Lite | 12 (bookworm)  | 6.6    | Latest         | 903 MB|

These images are automatically generated with each release of RaspAP and are made [available here](https://github.com/RaspAP/raspap-webgui/releases/latest). You may choose between an `arm64` or `armhf` (32-bit) based build.

!!! warning "Important"
    Newer distributions of Raspberry Pi OS require a user to be created on first boot. For security reasons, RaspAP's custom OS images _do not_ preconfigure a user. For this reason, you must use the **custom settings** in Raspberry Pi Imager or Etcher to define a user when writing to the SD card. Failure to do so will cause a headless setup to stall with an interactive prompt to create a new user. 

After downloading your desired image from the [latest release page](https://github.com/RaspAP/raspap-webgui/releases/latest), use a utility such as the Raspberry Pi Imager or [balenaEtcher](https://www.balena.io/etcher) to flash the OS image onto a microSD card. Insert the card into your device and boot it up. The latest RaspAP release version with the most popular optional components will be active and ready for you to configure.

!!! note Note
    To ensure that wireless operation isn't blocked by `rfkill`, the WiFi country is preset to "US" in these images. If this is _not_ your country, be sure to change this with `sudo raspi-config` and choose **Localisation Options** on first boot.

## Quick Install
Alternatively, start with a clean install of the [latest release of Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/). Both the 32- and 64-bit release versions are supported, as well as the latest 32-bit Desktop distribution. Consult [this FAQ](faq.md#distros) before installing RaspAP in a desktop environment.


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
The [Quick installer](quick.md) will complete the steps in the [manual installation](manual.md) for you. At the end of the install process, accept the prompt to reboot your system.

## Initial settings
After completing either of these setup options, the wireless AP network will be configured as follows:

  **IP address:** 10.3.141.1  
  **Username:** admin  
  **Password:** secret  
  **DHCP range:** 10.3.141.50 to 10.3.141.254  
  **SSID:** `RaspAP`  
  **Password:** ChangeMe  

It's _strongly recommended_ that your first post-install action is to change the default admin [authentication](authentication.md) settings. Thereafter, your AP's [basic settings](ap-basics.md) and many [advanced options](ap-basics.md#advanced-options) are now ready to be modified by RaspAP.

!!! tip "Tip"
    If this is _not_ a clean install or you are configuring a device with a non-standard [integration](faq.md#integrations) try following the [manual installation](manual.md) instructions or deploy RaspAP in a [Docker container](docker.md).

## Discussions
Questions or comments about the Quick start? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).
