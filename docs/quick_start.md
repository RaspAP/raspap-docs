# Quick start

## Quick Install

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

## Discussions
Questions or comments about the Quick start? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).