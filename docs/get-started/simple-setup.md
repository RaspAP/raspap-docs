# Simple Setup
RaspAP gives you two different ways to get up and running quickly. The simplest and recommended approach is to use our custom OS image with RaspAP preinstalled via the **Raspberry Pi Imager**. This option eliminates guesswork, lets you customize settings before flashing, and gives you a base upon which to build. Alternatively, you may execute the Quick installer on an existing [compatible OS](../index.md#compatible-operating-systems). Each method is described in the following sections.

## Installation method
=== "Pre-built image"
    ### Raspberry Pi Imager
    The easiest way to install RaspAP is by using the official [Raspberry Pi Imager](https://www.raspberrypi.com/software/). This method lets you select RaspAP directly from the "Other specific-purpose OS" category. You can also customize settings (hostname, username, password and SSH access) before flashing directly to your microSD card in one step.

    ![Raspberry Pi Imager](../images/imager.png){: style="width:640px"}
    Simply download and launch Raspberry Pi Imager, choose **OS → Other specific-purpose OS → RaspAP**, select your preferred architecture (64-bit or 32-bit), and follow the prompts to configure and flash your card.

    !!! warning "Important"
        Newer distributions of Raspberry Pi OS require a user to be created on first boot. For security reasons, RaspAP's custom OS images _do not_ preconfigure a user. You must use the **custom settings** in Raspberry Pi Imager to define a user when writing to the SD card. Failure to do so will cause a headless setup to stall with an interactive prompt to create a new user.

    !!! note Note
        To ensure that wireless operation isn't blocked by `rfkill`, the WiFi country is preset to "US" in these images. If this is _not_ your country, be sure to change this with `sudo raspi-config` and choose **Localisation Options** on first boot.

    ### Direct download
    Custom Raspberry Pi OS Lite images with the latest RaspAP are also available for direct download. This includes both 32- and 64-bit builds for ARM architectures. Before downloading a custom OS with RaspAP preinstalled, refer to [this resource](https://www.raspberrypi.com/software/operating-systems/) to ensure compatibility with your hardware.

    | Operating system     | Debian version | Kernel version  | RaspAP version | Size  |
    | ---------------------| ---------------|-----------------|----------------|-------|
    | Raspberry Pi OS (64-bit) Lite | 13 (trixie)  | 6.12     | Latest         | 885 MB|
    | Raspberry Pi OS (32-bit) Lite | 13 (trixie)  | 6.12     | Latest         | 858 MB|

    These images are automatically generated with each release of RaspAP and are made [available here](https://github.com/RaspAP/raspap-webgui/releases/latest). You may choose between an `arm64` or `armhf` (32-bit) based build.

    !!! tip
        Torrent files are available to avoid GitHub's download timeout issues. Downloads still come from GitHub but can complete reliably without interruption. If you prefer not to use torrents, other methods are suggested in [this GitHub thread](https://github.com/orgs/community/discussions/169381). Contact us if you experience any issues.

    After downloading your desired image from the [latest release page](https://github.com/RaspAP/raspap-webgui/releases/latest), use the [v1.9.6 release of Raspberry Pi Imager](https://github.com/raspberrypi/rpi-imager/releases/tag/v1.9.6) or later to flash the OS image onto a microSD card. The Pi Imager is recommended because it lets you modify optional OS configuration settings, such as setting a username and password, and enabling remote access via SSH. Once completed, insert the card into your device and boot it up. The latest RaspAP release version with the most popular optional components will be active and ready for you to configure.

    ??? note "SD Card flashing alternative"
        [balenaEtcher](https://etcher.balena.io/) is an alternative to [Raspberry Pi Imager](https://www.raspberrypi.com/software/), but it does not offer the ability to modify the basic Raspberry Pi configuration settings mentioned above. In this event, you can enable remote access and [configure a user manually](https://www.raspberrypi.com/documentation/computers/configuration.html#remote-access).

=== "Quick install"
    Alternatively, start with a clean install of the [latest release of Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/). Both the 32- and 64-bit release versions are supported, as well as the latest Desktop distributions. Consult [this FAQ](../faq.md#distros) before installing RaspAP in a desktop environment.

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
    ```
    curl -sL https://install.raspap.com | bash
    ```
    The [Quick installer](quick-installer.md) will complete the steps in the [manual installation](manual.md) for you. At the end of the install process, accept the prompt to reboot your system.

## Initial settings
After completing either of these setup options, the wireless AP network will be configured as follows:

&nbsp;&nbsp;&nbsp;&nbsp;**IP address:** 10.3.141.1  
&nbsp;&nbsp;&nbsp;&nbsp;**Username:** admin  
&nbsp;&nbsp;&nbsp;&nbsp;**Password:** secret  
&nbsp;&nbsp;&nbsp;&nbsp;**DHCP range:** 10.3.141.50 to 10.3.141.254  
&nbsp;&nbsp;&nbsp;&nbsp;**SSID:** `RaspAP`  
&nbsp;&nbsp;&nbsp;&nbsp;**Password:** ChangeMe  

!!! warning "Post-Install action"
    It is **strongly recommended** that your first post-install action is to change the default admin [authentication](../features-core/authentication.md) settings. Thereafter, your AP's [basic settings](../features-core/ap-basics.md) and many [advanced options](../features-core/ap-basics.md#advanced-options) are now ready to be modified by RaspAP.

!!! tip "Tip"
    If this is _not_ a clean install or you are configuring a device with a non-standard [integration](../faq.md#integrations) try following the [manual installation](manual.md) instructions or deploy RaspAP in a [Docker container](docker.md).

## Next Steps
The most common use-case for RaspAP is to be a [Repeater](../features-core/repeater.md). There are many other use-cases and features to explore in our [Core](../features-core/index.md) or [Experimental](../features-experimental/index.md) Features, or look at joining our [Insiders](../features-insiders/index.md) for even more.

## Discussions
Questions or comments about the Quick start? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).
