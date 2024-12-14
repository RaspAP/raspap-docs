# FAQ

This guide was written to address some frequently asked questions among users of RaspAP.
FAQ items are organized into thematic sections, below, for easier reference.

If you would like to see a new FAQ that you feel would assist other users, [start a discussion](https://github.com/RaspAP/raspap-webgui/discussions) or [open an issue](https://github.com/RaspAP/raspap-webgui-docs/issues).

## General
* [Is RaspAP a fork of OpenWrt or another router project?](#fork)
* [What is the scope of support for Desktop distributions?](#distros)
* [What do all these settings in the UI do? Changing them seems to have no effect.](#settings)
* [How do I prepare the SD card to connect to WiFi in headless mode?](#headless)
* [Can I use wlan0 and wlan1 rather than eth0 for my AP?](#interfaces)
* [Can I use RaspAP as a monitor only, without changing my configuration?](#monitor)
* [Can I use RaspAP with my custom dnsmasq configuration?](#dnsmasq)
* [What is the maximum number of simultaneous clients that I can connect to my AP?](#maxclients)
* [Where can I find a list of USB WiFi adapters that use in-kernel drivers?](#adapters)
* [What are the passphrase requirements used by RaspAP?](#passphrase)
* [Can I remove the AP password to create an open WiFi network?](#nopw)
* [How do I prevent WAN access to RaspAP's web administration?](#access)
* [Can I reduce the risk of SD card corruption and extend a card's lifespan?](#minwrite)

## Troubleshooting
* [After a clean install, WiFi  and/or RaspAP behaves unpredictably.](#clean)
* [My 802.11ac 5 GHz hotspot failed to start. What now?](#actroubleshoot)
* [Clients cannot obtain an IP address from the hotspot.](#noip)
* [My WiFi network disappeared and I can't access the web UI.](#webui)
* [My custom hostapd.conf / php.ini is gone.](#custom)
* [I changed the admin password and forgot what it was.](#password)
* [RaspAP control panel works but there is no WiFi after reboot.](#nowifi)
* [Bridged AP mode is unstable or clients can't connect.](#bridged)
* [Managed mode AP doesn't work on the Pi Zero W.](#pizero-w)
* [WiFi scanning doesn't work or I get the error "cannot execute wpa_cli reconfigure".](#scanning)
* [I started the hotspot but it shows "hostapd down". What's happening?](#hostapd-down)
* [Pinging the AP from a client computer (or vice versa) results in an intermittent failure. Can I troubleshoot this?](#ping)
* [My wlan1 keeps being disabled and/or clients are repeatedly disconnected.](#disassociated)
* [RaspAP web UI fails to start or unable to save settings.](#webfail)
* [Why do I receive an 'Invalid CSRF token' message and a blank screen?](#token)
* [Can I restore RaspAP's default settings?](#restore)

## Integrations
* [How do I integrate RaspAP with Pi-hole?](#pihole)
* [Can I integrate RaspAP with Adguard Home?](#adguard)
* [Can I configure RaspAP to work with a captive portal?](#captive)
* [How do I create an AP activation schedule?](#schedule)
* [Can I schedule the WiFi password to change automatically?](#genpassword)
* [Can I configure a managed mode AP without using the UI?](#managed)
* [Can I configure an alternate port for RaspAP's web service?](#webport)
* [What breaks RaspAP when Docker is installed on the same system and how I can fix it?](#docker)
* [Can I integrate RaspAP with OpenMediaVault?](#omv)
* [Can I use RaspAP to share Speedify's aggregated connections?](#speedify)
* [How do I serve custom pages from RaspAP?](#custompages)
* [Can I automatically update RaspAP's adblock lists?](#adblockauto)

<a name="openvpn"></a>
## OpenVPN
* [OpenVPN fails to start and/or I have no internet.](#openvpn-fails)
* [OpenVPN works but I have partial or no internet access.](#partial)
* [OpenVPN is enabled but I am still blocked from country restricted websites.](#restricted)  

<a name="wireguard"></a>
## WireGuard
* [Uploading my WireGuard config results in "MIME type not allowed".](#mimetype)
* [I think my traffic isn't being routed through the WireGuard VPN. Can I debug this?](#wgtraffic)
* [How can I clear RaspAP's WireGuard log?](#wglog)

## Networking
* [Why can't I access wireless mode 'N' (802.11n)?](#wireless-mode)
* [How do I exclude NAT rules from IP traffic on localhost?](#iptables)
* [Why is the channel dropdown disabled on the Hotspot page?](#channels)
* [802.11ac is supposed to operate at 433 Mbps. Why is my AP's throughput so much less?](#433ac) 
* [Why is the maximum throughput of my 802.11n AP reduced by half?](#wirelessn)
* [Can I connect the WiFi client to a WEP network?](#wep)
* [Can I turn the hotspot on/off over SSH?](#hotspotssh)
* [Can I share internet from a wireless LAN with Ethernet clients?](#wlanether)
* [Can RaspAP automatically connect to a known WiFi network at boot?](#autoconnect)

## Install & upgrade
* [Can I isolate RaspAP from other software on my system?](#isolate)
* [How do I upgrade RaspAP?](#upgrade)
* [Do I need the RaspAP service to run at boot?](#raspap-service)
* [Can the Quick Installer accept the default options without prompting me?](#unattended)
* [Can I restore RaspAP's default settings?](#restore)
* [How do I uninstall RaspAP?](#uninstall)

## <a name="fork"></a>Is RaspAP a fork of OpenWrt or another router project?
RaspAP is an independent wireless router project designed for embedded systems and created by a [community of developers](https://github.com/RaspAP/raspap-webgui/graphs/contributors). By contrast, [OpenWrt](https://openwrt.org/) is an operating system built around the Linux kernel. While powerful, it's rather more difficult to tailor custom applications around OpenWrt. That is, users are generally limited to what is available in OpenWrt's package repository, unless they fork the project code and modify the OS.

RaspAP is popularly used to provide a variety of networking and wireless routing services to other Linux projects and applications. Moreover, with [Docker support](docker.md) users are able to run RaspAP in an isolated container. This gives you much greater flexibility if you're hosting other Linux services and/or applications on your device.

## <a name="distros"></a>What is the scope of support for Desktop distributions?
A desktop distribution (or "distro") usually has a very different set of programs that handles various underlying OS functions and wraps it with a pretty GUI. While this project generally recommends non-desktop distros, such as Raspberry Pi OS Lite, it's understood that many users prefer using a desktop environment.

For this reason, Raspberry Pi OS (64-bit) Desktop has undergone extensive testing and is subsequently [validated for use with this project](index.md#compatible-operating-systems) with _clean installs_ of the OS.

Please be aware that "supported" [is not a guarantee](issues.md#supported-devices). That is, if you experience issues with RaspAP in your desktop environment, it's _your_ responsibility (not the maintainers of this project) to eliminate potential conflicts with other software that you've installed _after_ booting a fresh desktop OS. Before reporting a bug, you may use one of several [community support channels](issues.md#issue-policy) to help you determine the cause of your issue or find a potential workaround.

## <a name="settings"></a>What do all these settings in the UI do? Changing them seems to have no effect.
RaspAP manipulates several daemons, services and helper programs behind the scenes for you. In the footer of each management panel is a helpful "Information provided by..." label. These indicate which Linux daemon and/or program is being modified by the UI. Learning what these services are and how they work will go a long way toward demystifying things.

![](https://i.imgur.com/q1RflMy.png){: style="width:350px"}

For example, two of the best starting points for understanding `hostapd` (the service that implements 802.11 AP management) include the [hostapd Linux documentation page](https://wireless.wiki.kernel.org/en/users/Documentation/hostapd) and [hostapd Wifi homepage](https://w1.fi/cgit/hostap/plain/hostapd/hostapd.conf).

!!! info "Info"
    After you choose **Save settings** for `hostapd` or `dhcpcd`, these services must be restarted for your changes to take effect. If you're not sure if your AP is behaving as expected, enable logging in the **Logging** tab of **Hotspot** and check the output.

## <a name="headless"></a>How do I prepare the SD card to connect to WiFi in headless mode?
Since [May 2016](https://www.raspberrypi.org/blog/another-update-raspbian/), Raspbian has been able to copy wifi details from `/boot/wpa_supplicant.conf` into `/etc/wpa_supplicant/wpa_supplicant.conf` to automatically configure wireless network access. 

An example `wpa_supplicant.conf` file is shown below. Replace the fields with your settings:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=your_ISO-3166_two-letter_country_code

network={
    ssid="my_SSID"
    psk="my_PSK"
    key_mgmt=WPA-PSK
}
```

## <a name="interfaces"></a>Can I use wlan0 and wlan1 rather than eth0 for my AP?
Yes, this is supported by RaspAP. In this scenario, you may wish to use the `wlan0` interface as the AP interface with `wlan1` as the wireless client interface. Refer to the dedicated [WiFi repeater](repeater.md)
walkthrough for steps to enable this configuration.

## <a name="monitor"></a>Can I use RaspAP as a monitor only, without changing my configuration?
Yes, RaspAP has support for a so-called "monitor mode". In `config.php` change the setting `RASPI_MONITOR_ENABLED` to `true`. This disables the ability to modify settings, start/stop daemons, shutdown or reboot the RPi. RaspAP will continue to report interface statistics, service settings and data usage as normal. See [this](defaults.md#managing-config-values) for more information. 

## <a name="dnsmasq"></a> Can I use RaspAP with my custom dnsmasq configuration?
Yes, RaspAP supports this through the use of `dnsmasq.d`. The primary `/etc/dnsmasq.d/090_raspap.conf` managed by the UI includes the following directive to enable your custom .conf files:

```
conf-dir=/etc/dnsmasq.d
```

Configuration files placed in this directory will be used by the dnsmasq service and are untouched by the UI. 

## <a name="maxclients"></a>What is the maximum number of simultaneous clients that I can connect to my AP?
There are [several factors that come into play](https://github.com/raspberrypi/linux/issues/3010) here including, but not limited to, the specific RPi model, firmware version, available RAM and so on. 

Every update to the RPi's firmware takes up more of the limited RAM reserved for wireless, resulting in less space to host AP clients. Users of RaspAP have reported
up to [19 simultaneous clients](https://github.com/RaspAP/raspap-webgui/issues/462#issuecomment-588367233) with a Pi model 3B, but a smaller number with a newer model. This is related to the installed firmware, rather than the specific hardware.

The good news is, you can easily switch to an [alternative minimal firmware](https://github.com/RPi-Distro/firmware-nonfree/blob/bullseye/debian/config/brcm80211/cypress/README.txt) that has been tuned to maximise the number of clients in AP mode while still supporting STA ("station" or wireless client) mode. The expected number of supported clients using this firmware is now 19. 

To achieve this, a number of features have been removed:

* advanced roaming features (802.11k, 802.11v and 802.11r)
* dfsradar - allows an AP to operate in channels that may be used by radar
  systems
* obss-obssdump - ACS (Auto Channel Support)
* swdiv - antenna diversity (this is not relevant with only one antenna) 

In an up-to-date Raspberry Pi OS install, you can switch between the two variants by running the following command:

```
sudo update-alternatives --config cyfmac43455-sdio.bin
```

This method will persist across `firmware-brcm80211` updates.

## <a name="adapters"></a>Where can I find a list of USB WiFi adapters that use in-kernel drivers?
There are many USB WiFi adapters that work without the need to install a driver in Linux. The term "in-kernel" refers to drivers that are packaged and maintained by the Linux kernel.

This [GitHub list](https://github.com/morrownr/USB-WiFi) currently has 60 links to USB WiFi adapters that work without installing drivers (ie., "plug and play") on devices like the Raspberry Pi.

With adapters that use in-kernel drivers, you may simply plug the adapter in and it will work. Many people find that using adapters with in-kernel drivers is a better solution than buying an adapter that requires drivers to be found, downloaded, compiled, installed, fixed and reinstalled.

## <a name="passphrase"></a>What are the passphrase requirements used by RaspAP?
The requirements are based on [IEEE standard 802.11i-2004](https://en.wikipedia.org/wiki/IEEE_802.11i-2004) which defines a passphrase as a sequence of between 8 and 63 ASCII-encoded characters.
Furthermore, each character in the passphrase must have a decimal encoding in the range of 32 to 126 (IEEE Std. 802.11i-2004, Annex H.4.1). These are often known as [printable characters](https://en.wikipedia.org/wiki/ASCII#Printable_characters)
that represent letters, digits, punctuation marks and a few miscellaneous symbols.

This means that so-called special characters, or extended ASCII codes, are not permitted in a passphrase. For example, the Euro sign "€", German "ä" and British pound symbol "£" fall outside this range. 

RaspAP will automatically generate a secure passphrase, or PSK, for you. On the **Hotspot > Security** tab, click or tap the magic icon :fontawesome-solid-wand-magic-sparkles: next to the PSK input. Choose **Save settings**
and **Restart hotspot** for the changes to take effect. 

## <a name="nopw"></a>Can I remove the AP password to create an open WiFi network?
Yes. On the **Hotspot > Security** tab, select 'None' for Security type. Choose **Save settings** and **Restart hotspot** for the changes to take effect.

## <a name="access"></a>How do I prevent WAN access to RaspAP's web administration?
There are two ways to do this. The simplest method is to set the web server's bind address in RaspAP's **System > Advanced** tab to the IPv4 address you wish to grant access to. Choose **Save settings** and **Restart lighttpd**.
After this is done, the web server will refuse connections to all IP addresses other than the one you've defined. 

A somewhat cleaner method with a "403 Forbidden" response can be done manually with lighttpd. You could modify lighttpd's main config directly, but to keep things neater we can use RaspAP's own configuration in lighttpd's `/conf-available` directory. Edit it like so:

```
sudo nano /etc/lighttpd/conf-available/50-raspap-router.conf
```

Add the following to the end, substituting the `192.168.0.0/16` private IPv4 address range (192.168.0.0 – 192.168.255.255) for your own network:

```
# deny access to RaspAP admin for users that
# are not in the 192.168.0.0/16 network
$HTTP["remoteip"] != "192.168.0.0/16" {
    url.access-deny = ( "" )
}
```

Save and exit the file, then restart the lighttpd service:

```
sudo systemctl restart lighttpd.service
```

Clients outside of your defined network range will receive a '403' response when accessing the web UI.

## <a name="minwrite"></a>Can I reduce the risk of SD card corruption and extend a card's lifespan?
Yes. RaspAP has developed a [minimal write mode](minwrite.md) that substantially reduces disk I/O activity and helps to extend the life of microSD cards.

## <a name="clean"></a>After a clean install, WiFi  and/or RaspAP behaves unpredictably.
Issues like this are frequently reported. The vast majority of these problems stem from one (or a combination) of the following:

1. The install was not performed on a clean OS.
2. A faulty, corrupt, fake, poor quality and/or otherwise unsuitable SD card was used.
3. The SD card has insufficient storage space.
4. Raspberry Pi Imager software applied preconfigured wireless settings.

If you observe RaspAP or your wireless AP behaving strangely, be sure to follow the project prerequisites and perform a _clean_ install with a known-good SD card from a reputable manufacturer.

Problems such as [this](https://www.reddit.com/r/RaspAP/comments/1bo7vdf/need_help_with_ver_310_badly_no_idea_what_im/) can be difficult to diagnose. In this case, the Raspberry Pi Imager was adding the user's old WiFi settings to an otherwise clean OS image. Be sure to check the "OS customization" options when using this software. When in doubt, use an alternative SD card imaging tool.

RaspAP has been successfully integrated with many popular open source projects. One of the best ways to use RaspAP in an existing project is to deploy it in an isolated [Docker container](docker.md).

## <a name="actroubleshoot"></a> My 802.11ac 5 GHz hotspot failed to start. What now?
RaspAP uses [`iw`](https://wireless.wiki.kernel.org/en/users/documentation/iw) and the [`wireless-regdb`](https://wireless.wiki.kernel.org/en/developers/Regulatory/wireless-regdb) to determine which channels are allowed for your configured country. However, not all channels may be supported by your device's wireless adapter or firmware. If your 5 GHz access point fails to start, use the steps below to troubleshoot the problem.

Begin by enabling `hostapd` service logging by sliding the **Logfile output** toggle on the **Hotspot > Logging** tab. Choose **Save settings** followed by **Restart hotspot** and check the log output. The logs will often indicate when a selected channel is not supported by the hardware. For example:

```
wlan0: IEEE 802.11 Hardware does not support configured channel
Could not select hw_mode and channel. (-3)
```

This may occur with the Raspberry Pi or another device's onboard wireless chipset, or an external wireless adapter. To mitigate this, select one of the following 5 GHz channels: `36`, `40`, `44` or `48`, then choose **Save settings**. Click or tap the **Clear log** button on the **Hotspot > Logging** tab, if needed, and finally choose **Restart hotspot**. Check the logs again and see if the error persists.

If the 802.11ac AP still fails to start, an [external AC wireless adapter](faq.md#adapters) with in-kernel drivers is an option worth considering.

## <a name="noip"></a>Clients cannot obtain an IP address from the AP.
Clients may receive a "failed to obtain IP address" or similar error message when connecting to your AP. These are the most frequent reasons for this error:
1. A poor WiFi signal from the access point. In this event, reduce the distance between your device and the AP.
2. Your device does not operate properly with the encryption method set by the AP. 
3. The access point is misconfigured.

The first and simplest fix is to reconnect the client to your WiFi network. When you do this, the AP forgets the previous attempt and initiates a new process to assign an IP address to your device.
Exact methods vary between devices, however most will have a 'Forget this network' option or similar in the WiFi settings. This is shown in iOS, below:
 
![](https://i.imgur.com/7xvx5JT.png){: style="width:350px"}

If clients still fail to connect, restart the AP. You may do this by choosing **Restart hotspot** from RaspAP. This reinitializes several related services in a predictable order and timing.
Assuming these services are configured to restart automatically on reboot (the default behavior when RaspAP's installer is used) you may also simply reboot your Pi.

RaspAP gives you control over many aspects of your WiFi network, including DHCP. With its [default settings](defaults.md), RaspAP has been rigorously
tested and validated to provide connectivity in routed AP mode. If you suspect that RaspAP is misconfigured and not providing IP addresses to clients, you may troubleshoot this yourself.

Clients connecting to your AP are assigned, or leased, an IP address with `dnsmasq`. You can see how this process works by enabling the **Log DHCP requests** option in the **DHCP Server > Logging** tab. 
When a client connects to your AP, a typical `dnsmasq-dhcp` exchange follows this pattern:

```
dnsmasq-dhcp[2516]: DHCPDISCOVER(wlan0) [MAC address] 
dnsmasq-dhcp[2516]: DHCPOFFER(wlan0) 10.3.141.249 [MAC address] 
dnsmasq-dhcp[2516]: DHCPREQUEST(wlan0) 10.3.141.249 [MAC address] 
dnsmasq-dhcp[2516]: DHCPACK(wlan0) 10.3.141.249 [MAC address] iPhone
```

If one or more steps in this exchange are missing, either your device is unable to respond to the server's `DHCPOFFER` or the AP itself is misconfigured.

!!! tip "Tip"
    By default, the `dnsmasq` service listens on TCP/UDP port 53 and UDP port 67. If you have configured firewall software such as `ufw` or `iptables` to filter traffic on these ports, the service may not be able to respond to DHCP requests.

As a last resort, you can assign a static IP address to your device. Copy the MAC address for your device as it appears above and create a new entry in RaspAP's **DHCP Server > Static Leases** tab. 
Save settings, restart `dnsmasq` and try connecting your client again.

## <a name="webui"></a>My WiFi network disappeared and I can't access the web UI
If you are running your Pi headless and are unable to access RaspAP's web interface from the default `http://10.3.141.1/` address, do the following:

1. Be sure your browser isn't forcing SSL by appending `https://` to the address, which can result in misleading errors. This may sound obvious but it's reported frequently. (Related: add [SSL support for RaspAP](ssl.md).
2. Connect your device to wired ethernet and access it via the browser or SSH on the `eth0` interface using one of the methods described below. [Check the logs for hostapd errors](ap-basics.md#troubleshooting) and reconfigure the service, or run the installer again to restore the [default configuration](defaults.md).
3. There are [several methods](https://www.raspberrypi.com/documentation/computers/remote-access.html) you can use to determine your Pi's IP address. RaspAP's installer only configures a static IP address for the AP interface on `wlan0`. If the AP has entered a failed state, you may still be able to connect on an alternate interface.
4. Recent versions of the RPi OS kernel include the `avahi-daemon` which facilitates local network discovery via multicast DNS (mDNS). On client computers with the Bonjour service installed (all macOS machines and Windows PCs with Apple iTunes), try accessing your Pi by entering [http://raspberrypi.local/](http://raspberrypi.local/) in the browser or via SSH with `ssh pi@raspberrypi.local`.
5. If you don't have access to wired ethernet or the above methods fail, configure your Pi for USB-OTG, also known as "on-the-go" or gadget mode. Instructions for enabling USB-OTG vary between various models and not all Pi hardware has support for this.

## <a name="custom"></a>My custom `hostapd.conf` / `php.ini` is gone.
The [installer](quick.md) applies a "known good" [default configuration](defaults.md) to some services, including `hostapd`. It will also, optionally, optimize PHP by changing a very limited number of settings. Your custom configurations haven't been lost however; they've been moved to the backups directory in `/etc/raspap/backups`.

You are free to SSH in to restore those files to their rightful position. However, you may need to ensure that the RaspAP modifications are applied to your own custom configurations.

## <a name="password"></a>I changed the admin password and forgot what it was.
Login credentials are stored in `/etc/raspap/raspap.auth`. The password is encrypted and cannot be edited manually. However, deleting this file with `sudo rm /etc/raspap/raspap.auth` will restore the default admin password.

## <a name="nowifi"></a>RaspAP control panel works but there is no WiFi after reboot.
This problem often occurs when another program tries to reconfigure hostapd at startup. It can also happen when your RPi is configured as both a WiFi client and access point, also known as a [managed mode](ap-sta.md) AP. To address this, RaspAP has added a `systemd` init service to bring up networking services in a predictable order and timing after the Linux kernel is booted. You can check the status of this service with:

```
sudo systemctl status raspapd.service
```

The `raspapd.service` is optionally installed and enabled by the Quick Installer. It is also included in the manual setup steps.

## <a name="bridged"></a>Bridged AP mode is unstable or clients can't connect.
RaspAP [delegates all DHCP control to your router](bridged.md) in bridged AP mode. If you have trouble connecting clients, start with this project's [default configuration](issues.md#default-settings) in routed AP mode _first_ and try connecting a client. Enable logging for DHCP and hostapd to help you identify any problems. If you have no issues with client connectivity with the default routed AP, but cannot connect clients in bridged AP mode, in most cases the problem lies with your router—not RaspAP. Check your router's web interface and DHCP settings.

If clients disconnect intermittently, this often indicates an undervoltage issue with your RPi. Check the kernel log for any `Under-voltage detected!` errors. Be sure you are using an official 5.1V power supply (each model has [different power requirements](https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md)) and detach any USB devices. Executing `dmesg | grep br0` can also offer clues. Execute `sudo dhclient -v` to gain insights into DHCP requests between your device and router. A typical DHCP exchange follows this pattern:

```
CLIENT -> DHCPDISCOVER
SERVER -> DHCPOFFER
CLIENT -> DHCPREQUEST
SERVER -> DHCPACK
```

If your device (the client) broadcasts `DHCPDISCOVER`, but there is no `DHCPOFFER` response from your router, you have a misconfiguration or other issue with your network. Troubleshooting client connectivity in bridged AP mode is not supported. No hard feelings.

## <a name="pizero-w"></a>Managed mode AP doesn't work on the Pi Zero W.
See [this walkthrough](ap-sta.md) where the installation is described in detail.

## <a name="scanning"></a>WiFi scanning doesn't work or I get the error `cannot execute "wpa_cli reconfigure"`.
On some configurations, the **Configure WiFi client** panel may appear empty. This project uses the `wpa_supplicant` command line client `wpa_cli` to populate a list of available wireless networks. If you can't execute this from the shell, neither can the web UI. For example, the results of this command:

```
sudo wpa_cli -i wlan0 scan_results
Failed to connect to non-global ctrl_ifname: wlan0  error: No such file or directory
```
...indicate a problem with the socket used to communicate with `wpa_supplicant`. You may also encounter errors such as "Could not connect to wpa_supplicant: wlan0 - re-trying".

If this happens, first check the contents of `wpa_supplicant` with `sudo cat /etc/wpa_supplicant/wpa_supplicant.conf`. You should see, at minimum, the following:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
```

The above is present on clean installs of Raspbian. If you've made changes to this file, ensure that these lines appear first. Next, reinitialize the socket with:

```
sudo wpa_supplicant -B -Dnl80211,wext -c/etc/wpa_supplicant/wpa_supplicant.conf -iwlan0
```

substituting `wlan0` with your wireless interface, if necessary. You should then be able to perform scans as expected.

!!! tip "Tip"
    If you are using `wpa_suplicant.conf` to connect to your device with SSH on a wireless interface, do _not_ reboot after running the Quick Installer. More information on this topic is [available here](ap-sta.md#when-to-reboot).

## <a name="hostapd-down"></a>I started the hotspot but it shows "hostapd down". What's happening?
Hostapd, the Linux service that creates the access point, can fail to start for a variety of reasons. The following are common causes, with troubleshooting advice:

1. If you've attached an external wireless adapter (bound to `wlan1`, for example) and have selected this as the AP interface, be sure that it either uses an [in-kernel driver](#adapters), also 
known as "plug and play" support, or that you have installed the correct driver for it.
2. Confirm that the 802.11 wireless mode you've selected is supported by the adapter you've chosen in the list of available interfaces. For example, if you've selected the `802.11ac 5 GHz` wireless mode
with incompatible hardware, RaspAP will create the configuration for you but `hostapd` will fail to start.
   
In each of these cases, the `hostapd` service will report errors that can be useful for troubleshooting. Enable logging by selecting **Logfile output** on the **Hostapd > Logging** tab, choose 
**Save settings** then **Restart hotspot**.

Refer to [this FAQ](faq.md#actroubleshooting) and [this FAQ](#disassociated) for more info.

## <a name="ping"></a>Pinging the AP from a connected client computer (or vice versa) results in an intermittent failure. Can I troubleshoot this?
An intermittent ping failure on the wireless interface could indicate any number of things; a poor wireless signal, co-channel interference and disassociated client being among the most common.
The following are methods for troubleshooting this:

1. Get a signal strength report. A signal of -80 dBm or less from your AP is unreliable. If your client computer supports Linux, use `sudo iw dev wlan0 scan | awk '/signal:/{sta=$2$3} /SSID:/{print $0" "sta}'` and check your AP's dBm value.
Alternatively, use any one of several graphical WiFi explorer type tools and obtain your signal strength this way.

2. Use `wavemon` on the AP to scan for overlapping channels from nearby APs. Install it with `sudo apt install wavemon`. If it shows an AP with a strong signal on the same channel as your AP, you 
are likely experiencing co-channel interference. Select a different channel or band for your AP, restart it and compare the results.

3. Use `mtr` to run a continuous scan that reports on latency and percentage packet loss. Install it with `sudo apt install mtr-tiny`. Obtain your client's IPv4 address from the dashboard or
**DHCP Server > Client list** and start the utility, for example `mtr 10.3.141.151`. While the scan is running, reposition your client computer and/or your AP and observe the results.

4. Enable `hostapd` service logging from RaspAP with **Hotspot > Logging > Logfile output**, followed by **Save settings** and restart your AP. Look for errors that indicate clients are being disassociated from the AP. Refer to [this FAQ](#disassociated) for more info.

## <a name="disassociated"></a>My wlan1 keeps being disabled and/or clients are repeatedly disconnected.
Issues [such as this](https://github.com/RaspAP/raspap-webgui/issues/666) can be tricky to diagnose. In this case, an AP is started with an external USB wireless adapter, but client devices are continuously authenticated and disconnected
(or "disassociated"). This may appear in `hostapd` service logs like so:

```
wlan1: STA 24:62:ab:fd:24:34 IEEE 802.11: authenticated
wlan1: STA 24:62:ab:fd:24:34 IEEE 802.11: associated (aid 1)
wlan1: AP-STA-CONNECTED 24:62:ab:fd:24:34
wlan1: STA 24:62:ab:fd:24:34 RADIUS: starting accounting session 1D0030DD3176A315
wlan1: STA 24:62:ab:fd:24:34 WPA: pairwise key handshake completed (RSN)
wlan1: AP-STA-DISCONNECTED 24:62:ab:fd:24:34
wlan1: STA 24:62:ab:fd:24:34 IEEE 802.11: disassociated
wlan1: STA 24:62:ab:fd:24:34 IEEE 802.11: deauthenticated due to inactivity (timer DEAUTH/REMOVE)
```

The AP itself may also fail repeatedly with errors like the following:

```
wlan1: INTERFACE-ENABLED 
Failed to set beacon parameters
wlan1: INTERFACE-DISABLED 
wlan1: INTERFACE-ENABLED 
Failed to set beacon parameters
wlan1: interface state ENABLED->DISABLED
wlan1: AP-DISABLED 
wlan1: CTRL-EVENT-TERMINATING 
```

If you see messages indicating "deauthenticated due to inactivity", you can try the "Disable `disassoc_low_ack`" setting on the **Hotspot > Advanced** tab. Choose **Save settings** then restart your AP. Monitor the hostapd service logs and see if your clients are able to remain connected.

In this specific case, the user determined that the external [RT3070 WiFi adapter](https://unix.stackexchange.com/questions/610338/raspberry-pi-4-model-b-external-rt3070-wifi-adapter-hostapd-crashing) was at fault.

## <a name="webfail"></a>RaspAP web UI fails to start or unable to save settings.
After performing a clean install of RaspAP or upgrading an existing installation, the web UI may fail to start or the admin panel may behave in unexpected ways. For example, pages may load but any
attempt to save settings will fail. In other cases, the lighttpd web server may fail to respond completely. Errors such as these in `/var/log/lighttpd/error.log` are common:

```
(gw_backend.c.503) bind failed for: unix:/run/lighttpd/php.socket-0: No such file or directory
(gw_backend.c.601) gw-backend failed to start: /usr/bin/php-cgi
(gw_backend.c.1655) [ERROR]: spawning gw failed
```

These signs point to a corrupted filesystem on the SD card. If during a power disconnection the memory card is in a write operation, there is a high chance that one or more sectors will be
damaged. In these cases, a fresh install on a new SD card can save you time and frustration. RaspAP's [minimal SD card write](minwrite.md) mode can help in this case.

!!! tip "Tip"
    Be sure to use genuine MicroSD cards from a reputable manufacturer. Card clones are common and hard to distinguish from legitimately made ones, but certainly not subject to the same quality standards. Neither fake nor cheap cards are typically suitable for an entire OS to run from.

## <a name="token"></a>Why do I receive an 'Invalid CSRF token' message and a blank screen?
A [cross-site request forgery](https://owasp.org/www-community/attacks/csrf) (CSRF) is a type of exploit where unauthorized commands are executed against a website on behalf of a trusted user. To guard against this, RaspAP generates a one-time token that is unique for every user and stored in the PHP session object. This token value is inserted into a hidden field on every form in the RaspAP application. If the token doesn’t exist in the submitted
form data or fails to match with the token on the server, the form will reject the submission and return an error.

The most common cause for this error message is when your PHP session expires. By default, the PHP session timeout is defined as 24 minutes (1440 seconds). When this timeout is reached stored data will be seen as "garbage" and cleaned up by the garbage collection process.

If you submit a form in RaspAP 24 minutes after the page was loaded, the application will return a CSRF token error. When this occurs, simply refresh the page to generate a new session token.

## <a name="restore"></a>Can I restore RaspAP's default settings?
Yes, two methods are [described here](defaults.md#restoring-settings).

## <a name="pihole"></a>How do I integrate RaspAP with Pi-hole?
There have been several discussions around integrating RaspAP with Pi-hole, with the end goal of hosting a complete AP and ad-blocker on a single device. Both projects rely on `dnsmasq`, so integration between them is tricky. There are now several options available to users of RaspAP.

1. The first option is to configure RaspAP to use a Pi-Hole installation on a separate device. Go to RaspAP's **DHCP Server** > **Advanced** page and enable the "Upstream DNS Server" option, add your Pi-Hole's DNS, save settings and restart dnsmasq.

2. Install RaspAP in an isolated [Docker container](docker.md) together with Pi-Hole. You will need to configure Pi-Hole's `dnsmasq` service to listen on a port other than `53`.

3. Install Pi-Hole in a Docker container and proceed with a normal installation of RaspAP on the same device.

4. Alternatively, you may use RaspAP's own [ad blocking facility](adblock.md) with support for custom blocklists. 

## <a name="adguard"></a>Can I integrate RaspAP with Adguard Home?
Yes, you can run RaspAP and [Adguard Home](https://github.com/AdguardTeam/AdGuardHome) on the same device. Change Adguard Home’s listening port to `5300` and bind to `127.0.0.1`, then go to RaspAP's > **DHCP Server** > **Advanced** page and enable the "Upstream DNS Server".  Add `127.0.0.1#5300` as an upstream DNS Server. Save settings and restart dnsmasq. Tip via [@firestrife23](https://github.com/RaspAP/raspap-webgui/issues/542#issuecomment-609078400)

## <a name="captive"></a>Can I configure RaspAP to work with a captive portal?
Yes. The [nodogsplash project](https://github.com/nodogsplash/nodogsplash) works just fine with RaspAP and is recommended over other methods. A detailed setup guide is [available here](captive.md). 

## <a name="schedule"></a>How do I create an AP activation schedule?
This is a common function in consumer wireless routers. For example, let's assume you want to disable your AP on Monday through Friday between 02:00 and 08:00. You can implement this with `cron` to stop/start RaspAP's service control script at certain times. Run `sudo crontab -e` and add entries like so:

```
# Stop RaspAP services at 02:00 on Monday through Friday
0 2 * * 1-5 sudo /etc/raspap/hostapd/servicestart.sh --action stop

# Start RaspAP services at 08:00 on Monday through Friday
0 8 * * 1-5 sudo /etc/raspap/hostapd/servicestart.sh --seconds 3
```

For help with crontab, head over to <a href="https://crontab.guru/">crontab.guru</a>.

## <a name="genpassword"></a> Can I schedule the WiFi password to change automatically?
Yes. Here's [one way to do it](https://gist.github.com/billz/2cc43e96563293d650e313e068d52dfb) using bash. Save the script to your home directory (`/home/pi` for example) and set the execution
bit with `sudo chmod +x genpassphrase.sh`. When executed, the script will automatically generate a strong password (or a weaker, pronounceable one), update the `wpa_passphrase` setting in `hostapd.conf` and finally restart
the `raspapd.service`. The new passphrase and QR code will be visible on the **Hotspot > Security** tab.

This can be useful if you're using RaspAP to serve WiFi to clients in a public place, and need to update the passphrase regularly. Similar to creating an [AP activation schedule](#schedule),
you can have this execute at specific intervals by using `cron`. Run `sudo crontab -e` and add an entry like so:

```
# Generate a new passphrase and restart RaspAP everyday at midnight
@midnight /home/pi/genpassphrase.sh
```

For help with crontab, head over to <a href="https://crontab.guru/">crontab.guru</a>.

## <a name="managed"></a> Can I configure a managed mode AP without using the UI?
Yes. Let's assume you are creating an RPi OS image (or other supported OS) with scripts that setup RaspAP at first startup. In this scenario, to configure a managed mode AP you must manually connect via a browser, make some changes via the UI and then save your settings. This can be also be done programmatically. Assuming you have [`wpa_supplicant.conf` fully populated](faq.md#headless) and a valid [`hostapd.conf`](ap-sta.md#how-does-ap-sta-work), set the following values in `/etc/raspap/hostapd.ini`:

```
LogEnable = 0
WifiAPEnable = 1
BridgedEnable = 0
WifiManaged = wlan0
```

substituting `wlan0` for your AP interface, if necessary. You may then restart the raspap daemon with `sudo systemctl restart raspapd.service`.

## <a name="webport"></a>Can I configure an alternate port for RaspAP's web service?
Yes. You can now do this from the **Advanced** tab in System. Manual steps for changing `lighttpd`'s default port are included below.

Edit `/etc/lighttpd/lighttpd.conf` and change the following line:

```
server.port                 = 8080
```
then give the service a kick...
```
sudo systemctl restart lighttpd.service
```
You can then access RaspAP as before with the new port number in the URI, for example, `http://raspberrypi.local:8080`. This will allow you run another web server alongside lighttpd, if that is your goal. 

## <a name="docker"></a>What breaks RaspAP when Docker is installed on the same system and how I can fix it?
Installing RaspAP after installing Docker often results in connected clients not having internet access from the AP. The reason for this is Docker manipulates `iptables` rules to provide network isolation. Docker installs two custom iptables chains named `DOCKER-USER` and `DOCKER`, and it ensures that incoming packets are always checked by these two chains first. Docker also sets the policy for the `FORWARD` chain to `DROP`.

When RaspAP is started in its default router mode, this will result in the AP not forwarding traffic anymore. If you want RaspAP to continue functioning as a router, you can add explicit `ACCEPT` rules to the `DOCKER-USER` chain to allow it:

`sudo iptables -I DOCKER-USER -i src_if -o dst_if -j ACCEPT`

When Docker is correctly installed _after_ RaspAP, the following `iptables` chain should be present:

```
Chain INPUT (policy ACCEPT) target prot opt source destination
Chain FORWARD (policy ACCEPT)
target prot opt source destination DOCKER-USER all -- anywhere anywhere
DOCKER-ISOLATION-STAGE-1 all -- anywhere anywhere
ACCEPT all -- anywhere anywhere ctstate RELATED,ESTABLISHED DOCKER all -- anywhere anywhere
ACCEPT all -- anywhere anywhere ACCEPT all -- anywhere anywhere
Chain OUTPUT (policy ACCEPT) target prot opt source destination
Chain DOCKER (1 references) target prot opt source destination
```

Additional info [here](https://github.com/RaspAP/raspap-webgui/issues/458#issuecomment-643425658) and [here](https://docs.docker.com/network/iptables/). 

**tl;dr:** Install RaspAP _first_, followed by Docker, adding the explicit `iptables` rule `sudo iptables -I DOCKER-USER -i src_if -o dst_if -j ACCEPT`.

## <a name="omv"></a>Can I integrate RaspAP with OpenMediaVault?
Yes, you can run RaspAP alongside [OpenMediaVault](https://www.openmediavault.org/) for a complete media center and wireless hotspot on a single device. In this way, you are able to share the media storage
in your local network via a wireless hotspot while connected to a router via ethernet. This is illustrated in the schematic below:

```
[Router] <---- eth ----> [Pi] (RaspAP + OMV5)
   |                      |
 WiFi 1              WiFi 2 (subnet)
```

Follow these steps to create this configuration:

1. Follow RaspAP's [Quick start](quick.md) guide and set up your network as you wish.
2. Change the default Web server port to `8080` (so that it doesn't conflict with OMV5), from RaspAP's **System > Advanced** panel.
3. Install OMV5 skipping network configuration.
4. Configure your OMV5 install without changing the network settings.
5. To make your OMV5 drives accessible from the subnet (WiFi 2), add the following settings at the end of **OMV Control panel > Menu > SMB/CIFS > Settings Tab > Extra Options**:
```
bind interfaces only = yes
interfaces = lo eth0
```

Source: [openmediavault forums](https://forum.openmediavault.org/index.php?thread/39060-raspap-and-omv5-media-center-wifihotspot-with-ethernet/).

## <a name="speedify"></a>Can I use RaspAP to share Speedify's aggregated connections?
Yes, RaspAP is compatible with Speedify's connection bonding. In this scenario, you may want to combine several internet connections (for example, a DSL connection, 4G cellphone and an LTE router) and share these via RaspAP.

Begin by running Speedify's [one step install](https://support.speedify.com/article/562-install-speedify-linux), login with your credentials and connect Speedify. Next, [configure Speedify for WiFi sharing](https://support.speedify.com/article/566-speedify-linux-wifi)
by editing the following file:

```
sudo nano /etc/speedify/speedify.conf
```

Make sure to uncomment the following lines (remove the "`#`" symbol). To share over the Wi-Fi interface `wlan0`, set:

```
ENABLE_SHARE=1 
SHARE_INTERFACE="wlan0"
WIFI_INTERFACE="wlan0" 
```

Once you have configured the sharing settings, save the file (if you are using nano, use ++ctrl+o++ and press ++enter++ to save). Exit the text editor and then execute:
 
```
sudo service speedify-sharing restart
```

Refer to [Speedify's support article](https://support.speedify.com/article/566-speedify-linux-wifi) for additional tips and troubleshooting.

## <a name="custompages"></a>How do I serve custom pages from RaspAP?
Several users have asked if they can extend RaspAP or otherwise serve their own custom directory with the existing `lighttpd` web service. Broadly, there are two approaches to achieve this.
In the examples below, we will add support for a custom directory called "admin".


**Option 1.** Create a subdirectory of RaspAP's default install location (`/var/www/html`) called "admin": `/var/www/html/admin`. Now, modify RaspAP's [application routing rules](https://docs.raspap.com/manual/#create-the-web-application)
 by adding this directory to the exclusion list. You may do this with `sudo nano /etc/lighttpd/conf-available/50-raspap-router.conf`. Next, modify the following line like so: 

```
$HTTP["url"] =~ "^/(?!(dist|app|ajax|config|admin)).*" {
```

Note that "admin" is appended above "config", above. This instructs lighttpd not to rewrite URLs that match this pattern. Reload the lighttpd service with `sudo systemctl reload lighttpd.service`.

You may now create your own `index.php` file in this folder and request it from the browser as `http://10.3.141.1/admin/` or `http://raspberrypi.local/admin`.

**Option 2.**  Reinstall RaspAP and specify a custom install destination, for example `/var/www/html/raspap`. This will leave the default web root free for you to create any files you wish, without attempting to rewrite the URLs (the installer will only apply routing rules to your custom RaspAP root). 

## <a name="adblockauto"></a>Can I automatically update RaspAP's adblock lists?
RaspAP's [adblock feature](adblock.md) uses several [blocklists](adblock.md#blocklist-source) that are aggregated and updated daily. In a typical setup, you may use the **Ad blocking** management
page to manually update these lists. Alternatively, this <a href="https://github.com/RaspAP/raspap-webgui/discussions/1216">user-contributed script</a> will automatically fetch the latest blocklists on
the schedule of your choosing (for example, daily, weekly, etc.) and reload `dnsmasq`.
```
#!/bin/sh
#
sleep $(shuf -i 0-3600 -n1)
curl -L https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts > /etc/raspap/adblock/hostnames.tmp
curl -L https://big.oisd.nl/dnsmasq > /etc/raspap/adblock/domains.tmp

mv /etc/raspap/adblock/hostnames.tmp /etc/raspap/adblock/hostnames.txt
mv /etc/raspap/adblock/domains.tmp /etc/raspap/adblock/domains.txt
chown root:www-data /etc/raspap/adblock/hostnames.txt
chown root:www-data /etc/raspap/adblock/domains.txt

sudo systemctl reload dnsmasq.service
```
Credit to <a href="https://github.com/DanielLester83">DanielLester83</a>.

## <a name="openvpn-fails"></a>OpenVPN fails to start and/or I have no internet.
RaspAP supports OpenVPN clients by uploading a valid `.ovpn` file to `/etc/openvpn/client` and, optionally, creating a `login.conf` file with your client auth credentials. Additionally, in line with the project's [default configuration](defaults.md), the following iptables rules are added to forward traffic from OpenVPN's `tun0` interface to your configured wireless interface (`wlan0` is the default):

```
-A FORWARD -i tun0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
-A FORWARD -i wlan0 -o tun0 -j ACCEPT
``` 

After starting the OpenVPN service, you may check and validate these rules like so:

```
$ sudo iptables -L FORWARD -v -n
Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
 1955 1493K ACCEPT     all  --  tun0   wlan0   0.0.0.0/0            0.0.0.0/0            state RELATED,ESTABLISHED
 1715  194K ACCEPT     all  --  wlan0  tun0    0.0.0.0/0            0.0.0.0/0
```

It is your responsibility to provide a valid `.ovpn` file. RaspAP does not attempt to validate the settings or RSA keys contained in this file. If OpenVPN fails to start, check for errors with `sudo systemctl status openvpn-client@client` and `journalctl --identifier openvpn`.

## <a name="partial"></a>OpenVPN works but I have partial or no internet access.
Issues [like this](https://github.com/RaspAP/raspap-webgui/issues/612) are frequently reported. Begin by confirming the status of your connection:

```
$ sudo systemctl status openvpn-client@client
● openvpn-client@client.service - OpenVPN tunnel for client
   Loaded: loaded (/lib/systemd/system/openvpn-client@.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2020-06-12 15:45:41 CDT; 1min 39s ago
     Docs: man:openvpn(8)
           https://community.openvpn.net/openvpn/wiki/Openvpn24ManPage
           https://community.openvpn.net/openvpn/wiki/HOWTO
 Main PID: 2689 (openvpn)
   Status: "Initialization Sequence Completed"
    Tasks: 1 (limit: 2200)
   Memory: 1.1M
   CGroup: /system.slice/system-openvpn\x2dclient.slice/openvpn-client@client.service
           └─2689 /usr/sbin/openvpn --suppress-timestamps --nobind --config client.conf
```
You can also use `journalctl --identifier openvpn` to identify any errors. If your internet access is intermittent or otherwise degraded with the `openvpn-client` active, the next step is to test your connection for packet loss and latency. There are many Linux tools you can use to diagnose your network. `mtr` is a good choice as it combines functionality of the traceroute and ping programs. Install and use it to perform your own evaluation:

```
sudo apt install mtr -y
sudo mtr -rwc 50 -i 0.2 -rw duckduckgo.com

Start: 2021-06-13T11:42:26+0100
HOST: raspberrypi                                Loss%   Snt   Last   Avg  Best  Wrst StDev
  1.|-- 192.168.1.254                              0.0%    50   26.8  27.1  26.5  31.4   0.8
  2.|-- somerouter.net                            88.0%    50   392.0 390.4 362.1 596.7  1.2
```

The results are reported as round-trip response times in milliseconds and the percentage of packet loss. If you see loss and/or latency like the above example, report it to your VPN provider or find another one. Read [this](https://www.linode.com/docs/networking/diagnostics/diagnosing-network-issues-with-mtr/) for more on interpreting mtr results.

Protip: free VPNs are frequently oversubscribed and usually not worth the trouble.

## <a name="restricted"></a>OpenVPN is enabled but I am still blocked from country restricted websites.
Remote hosts use a variety of methods to defeat VPNs, some more aggressively than others. Many VPN providers will advise you to configure custom DNS servers to mitigate [DNS leaks](https://dnsleaktest.com/), which you can do from RaspAP's **DHCP > Advanced** tab. Others have specific VPN nodes to use with popular streaming services. 

Several users have reported that Firefox's [DNS-over-HTTPS (DoH)](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) has created problems with their VPN, in effect creating a DNS leak from the browser that circumvents RaspAP's DNS settings. Be sure to disable this "feature" when using a VPN service. 

If you suspect network traffic is not being routed through tun0 (or any other interface) for some reason, you can monitor this directly from your RPi with `iftop`:

```
sudo apt install iftop
sudo iftop -i [interface]
```

## <a name="mimetype"></a>Uploading my WireGuard config results in "MIME type not allowed".
For security reasons, your OpenVPN or WireGuard `.conf` files must have a Linux MIME type of `text/plain`. Windows ignores MIME types, relying instead on extensions. To avoid errors, be sure your file has a `text/plain` 
MIME type embedded in it before uploading.

Most OpenVPN and WireGuard service providers give you the option of downloading a file formatted for Linux. Alternatively, you may convert your Windows config file
for use with Linux with `dos2unix` or one of several online tools made for this purpose. 

## <a name="wgtraffic"></a>I think my traffic isn't being routed through the WireGuard VPN. Can I debug this?
There are several things you can do to troubleshoot this. First, with the WireGuard service active, verify your public IPv4 address and check the external link, as shown below:

![](https://user-images.githubusercontent.com/229399/147815548-a16ef105-230b-4e89-a4e6-69abba51b92a.png){: style="width:276px"}

Next, you may check the WireGuard service status by executing `sudo systemctl status wg-quick@wg0.service` from the shell, like so:

```
$ sudo systemctl status wg-quick@wg0.service
● wg-quick@wg0.service - WireGuard via wg-quick(8) for wg0
     Loaded: loaded (/lib/systemd/system/wg-quick@.service; enabled; vendor preset: enabled)
     Active: active (exited) since Wed 2021-12-29 15:31:03 GMT; 1 day 18h ago
       Docs: man:wg-quick(8)
             man:wg(8)
             https://www.wireguard.com/
             https://www.wireguard.com/quickstart/
             https://git.zx2c4.com/wireguard-tools/about/src/man/wg-quick.8
             https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8
   Main PID: 1450 (code=exited, status=0/SUCCESS)
      Tasks: 0 (limit: 1438)
        CPU: 0
     CGroup: /system.slice/system-wg\x2dquick.slice/wg-quick@wg0.service
```

You may also use RaspAP's built-in WireGuard logging facility. On the **WireGuard > Logging** tab, enable the "Display WireGuard debug log" option and choose **Save settings**. Check the log
output in the tab and look for any errors.

!!! tip "Tip"
    The debug log facility queries the `systemd` journal with a one-time execution of `journalctl --identifier wg-quick`. If you want to update this log output, simply enable the option again. You may also execute this command directly from the shell, if you wish.

Finally, you may check and verify the WireGuard config itself, including PostUp / PostDown rules, by executing `sudo cat /etc/wireguard/wg0.conf`.

As a last piece of advice, be sure to test more than one client device connection with your WireGuard-enabled AP. Some users have reported traffic not routing as expected with one device, while a 
different device behaves normally. 

Please note that RaspAP provides a front-end to the WireGuard service only. It has no way of validating your WireGuard configuration. For this reason, bug reports such as "WireGuard not working"
won't be considered. 

## <a name="wglog"></a>How can I clear RaspAP's WireGuard log?
WireGuard doesn't do any logging by default. The quasi-logging done by RaspAP executes `sudo journalctl --identifier wg-quick`. The Linux journal is not something you usually clear by yourself, however you can use journalctl's self maintenance to retain only the past two days:

```
sudo journalctl --vacuum-time=2d
```

See `man journalctl` for more information.

## <a name="wireless-mode"></a>Why can't I access wireless mode 'N' (802.11n)?
On the **Configure hotspot** > **Security** tab, be sure to select CCMP for the Encryption Type. Save the settings and restart the hotspot. The wireless mode should be reported on clients as 802.11b/g/n.

```
RaspAP:
  PHY Mode:		802.11n
  Channel:		1
  Network Type:		Infrastructure
  Security:		WPA2 Personal
  Signal / Noise:	-49 dBm / -86 dBm
  Transmit Rate:	73
```

If using TKIP for encryption with WPA, you will be restricted to 54 Mb/s. This is because the IEEE 802.11n draft prohibits using high throughput with WEP or TKIP ciphers.

## <a name="iptables"></a> How do I exclude NAT rules from IP traffic on localhost?
RaspAP's [Quick Installer](quick.md) configures network-address-translation (NAT) with iptables rules, so that the RPi can act as an internet gateway to multiple hosts on a local network with a single public IP address. This is done by rewriting the addresses of IP packets as they pass through the NAT system. Many access points, including RaspAP, use a combination of IP forwarding and masquerading to achieve this.

In some cases, NAT rules applied to `localhost` can interfere with other services running on an RPi. An example is the Plex Media Server, which has an API that listens on localhost. As of this writing, the Plex API has been built to not authenticate communication between service processes of the server. This can cause a failure to communicate with the Plex API or similar add-on services on your RPi.

The solution is to add a NAT rule ahead of the rule RaspAP installs to not apply NAT to connections destined to 127.0.0.0/8:

```
$ sudo iptables -t nat -I POSTROUTING -d 127.0.0.0/8 -j ACCEPT
```
The resulting iptables chain should look something like this:

```
$ sudo iptables -t nat -L -n -v
Chain PREROUTING (policy ACCEPT 31 packets, 4810 bytes)
 pkts bytes target prot opt in out source destination

Chain INPUT (policy ACCEPT 31 packets, 4810 bytes)
 pkts bytes target prot opt in out source destination

Chain OUTPUT (policy ACCEPT 23 packets, 1338 bytes)
 pkts bytes target prot opt in out source destination

Chain POSTROUTING (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target prot opt in out source destination
   17 999 ACCEPT all -- * * 0.0.0.0/0 127.0.0.0/8
   2422 158K MASQUERADE all -- * * 0.0.0.0/0 0.0.0.0/0
```
Refer to [this issue](https://github.com/RaspAP/raspap-webgui/issues/333#issue-454352554).

## <a name="channels"></a> Why is the channel dropdown disabled on the Hotspot page? 
RaspAP is capable of detecting the frequencies (channels) supported by each of your device's wireless interfaces. If an interface is selected that is not capable of broadcasting on the 5 GHz band, the associated channels and the **Save settings** button are disabled. Next to the **Wireless Mode** selector, a tooltip :fontawesome-solid-circle-question:{ style="color: var(--md-default-fg-color--light) } will provide a brief explanation. 

![](https://github.com/RaspAP/raspap-webgui/assets/229399/576531cd-fcf1-4377-9d51-3824ee498efb){: style="width:320px"}

In this case, selecting a compatible 2.4 GHz wireless mode will populate the list of available channels for that interface. Alternatively, select another interface or connect a 5 GHz capable external wireless adapter. RaspAP will automatically detect the adapter and add it to the list of available interfaces.

## <a name="433ac"></a> 802.11ac is supposed to operate at 433 Mbps. Why is my AP's throughput so much less?
The 802.11ac wireless standard uses 433 Mbps per spatial stream in the 5GHz band. Therefore, the theoretical maximum speed for a single-stream device is 433 Mbps when using an 80 MHz wide channel. However, real-world speeds are often significantly less due to a number of factors.

In the Raspberry Pi's case, its onboard wireless chipset is connected to the primary System on a Chip (SoC) with a 4-bit SDIO link that runs at 41.7 MHz. 4 bits x 41.7 suggests about 160 Mbps should be possible with 802.11ac on this device. In practice, iPerf tests won't get close to this figure because SDIO is a simplex link (that is, half-duplex) with overhead in each of the protocol and transport layers. Given these restrictions, real-world iPerf tests in the range of 90-100 Mbps are actually quite good for this hardware.

## <a name="wirelessn"></a>Why is the maximum throughput of my 802.11n AP reduced by half? 
In order to achieve optimal throughput with 802.11n, the wireless stream must operate at a 40 MHz wide channel on the 2.4 GHz band. A 20 MHz channel will restrict you to 72 Mbps. Your `hostapd.conf` might have  the required settings, but this is no guarantee of a 40 MHz channel.

In practice, this can be quite difficult due to interference on the 2.4 GHz band. There are many things that will cause an AP to fallback to 20 MHz. The most common reason is if an AP detects another wireless network within 40 MHz, i.e. two channels, of its own channel. For example, if an AP is set to channel 6, another network operating anywhere from channel 4 to 8 will trigger a fallback. hostapd will usually report a fallback like so:

```
20/40 MHz operation not permitted on channel pri=3 sec=7 based on overlapping BSSes
```

For more information on optimizing 802.11n, refer to this [resource](https://www.lmi.net/wp-content/uploads/Optimizing_802.11n.pdf).

Generally speaking, the 5 GHz band has substantially greater capacity due to more non-overlapping radio channels and less radio interference as compared to the 2.4 GHz band. 

## <a name="wep"></a>Can I connect the WiFi client to a WEP network?
Wired Equivalent Privacy (WEP) has been deprecated for quite awhile but old routers still exist in the wild. Not all routers accept hex passwords, but you can try converting an ASCII password using an online tool like [this one](https://www.binaryhexconverter.com/ascii-text-to-hex-converter).
A valid WEP key should be 5 or 13 characters or a 10- or 26-digit hexadecimal value. Be sure the hex values are unpadded and there are no trailing spaces. For example, `52617370415069734772656174` is a valid hex passphrase.

Paste your converted hex value into RaspAP's WiFi client passphrase field and try connecting.

If you're not able to connect with a hex passphrase, you can also try this alternate [manual configuration method](https://wiki.netbsd.org/tutorials/how_to_use_wpa_supplicant/#index3h2).

## <a name="hotspotssh"></a>Can I turn the hotspot on/off over SSH?
Yes, RaspAP provides a front-end to several Linux `systemd` services, including `hostapd`. From the terminal, check the status of the `hostapd.service` like so:

```
$ sudo systemctl status hostapd.service 
● hostapd.service - Access point and authentication server for Wi-Fi and Ethernet
     Loaded: loaded (/lib/systemd/system/hostapd.service; enabled; vendor preset: enabled)
```

Stop the service with `sudo systemctl stop hostapd.service` and start it with `sudo systemctl start hostapd.service`.

If you're curious about which other services and Linux tools RaspAP controls for you, take a look at [`raspap.sudoers`](https://github.com/RaspAP/raspap-webgui/blob/master/installers/raspap.sudoers).  

## <a name="wlanether"></a>Can I share internet from a wireless LAN with Ethernet clients?
Yes, RaspAP simplifies this with an intuitive and easy-to-use [WLAN routing](wlanrouting.md) solution.

## <a name="autoconnect"></a>Can RaspAP automatically connect to a known WiFi network at boot?
When rebooting, users must manually re-establish a connection to a known WiFi network by using the **WiFi client** UI. This is the default behavior of `wpa_supplicant`. That is, on startup the `wpa_supplicant` service is executed by `systemd` (not RaspAP) and enables logging and the DBus control interface; it does not automatically connect to any known networks.

However, you can change this behavior and have `wpa_supplicant` establish a connection on startup by editing the root user's `crontab`, like so:

```
$ sudo crontab -e
```

Using your editor, append a line like the following:

```
# m h  dom mon dow   command
@reboot /sbin/wpa_supplicant -B -Dnl80211 -c/etc/wpa_supplicant/wpa_supplicant.conf -iwlan0
```

Save the file and exit from your editor. On the next system boot, your RaspAP router will automatically connect to your preferred wireless network, if it's available.


## <a name="isolate"></a>Can I isolate RaspAP from other software on my system?
Yes, you have the option of installing RaspAP in an isolated and portable [Docker container](docker.md). 


## <a name="upgrade"></a>How do I upgrade RaspAP?
Upgrading an existing install without changing your configuration is very straightforward. Several different methods are described below.

The [version 3.0.2](https://github.com/RaspAP/raspap-webgui/releases/tag/3.0.2) release introduced a new feature to upgrade your RaspAP installation. To use this, simply navigate to the **About** page and click or tap on the **Check for update** button. This queries the GitHub API for the latest release version, compares it with your current install and prompts you to upgrade if a newer release is available.

![Update](https://github.com/RaspAP/raspap-webgui/assets/229399/9a2ba5af-4a9f-4dfd-8306-048f96292bae){: style="width:520px"}

No other actions are required on your behalf. Alternatively, you may also use the [Quick installer](quick.md) to upgrade to the [latest release](https://github.com/RaspAP/raspap-webgui/releases/latest) version. This is done with the `--upgrade` option, as shown below:

```
curl -sL https://install.raspap.com | bash -s -- --upgrade
```

The installer upgrade is [_idempotent_](https://en.wikipedia.org/wiki/Idempotence), meaning it can be repeated an arbitrary number of times and the result will be as if it had been done only once. If you choose this method, you're done! Confirm the upgrade by checking the release version on the **About** page.

If you want to install a specific version, you may do so by referencing a tag using `git`:

```
sudo git fetch -v --tags
sudo git checkout 3.0.8
```

A tag is a pointer that isn't connected to the main development tree that git knows about. As a result, git will reply that you're in a "detached HEAD" state. This isn't a big deal, it just means that you have a specific version of the code that isn't connected to the git tree.

Alternatively, if you want the latest _bleeding edge_ commits from the master branch, use the following:

```
sudo git checkout -b master
sudo git pull origin master
```

If you've customized your installation by editing `config.php`, update the release version in this file:
```
sudo nano /var/www/html/includes/config.php
```
Change the value in this line to the release version, save the file and exit.

```
define('RASPI_VERSION', '3.0.8');
```

Whichever method you choose (about page button, installer upgrade, specific release or latest updates), your RaspAP configuration won't be changed.

## <a name="raspap-service"></a>Do I need the RaspAP service to run at boot?
If you are using your RPi as a client on a WiFi network (also known as managed mode) and hosting an access point simultaneously, the `raspapd.service` will ensure that your hotspot is active after a reboot. It does this by detecting WiFi client AP mode, adding the `uap0` interface and starting up networking services in a specific order.

If your RPi is configured with wired ethernet (`eth0`) or you haven't experienced problems with the AP starting on boot, you can disable the RaspAP daemon like so:

```
sudo systemctl disable raspapd.service
```

## <a name="unattended"></a> Can the Quick Installer accept the default options without prompting me?
Yes, the [Quick Installer](quick.md) has a non-interactive mode that lets you perform unattended setups. This mode assumes "yes" as an answer to all prompts. You can do an unattended install of RaspAP by appending the `--yes` command line option, like so:

```
curl -sL https://install.raspap.com | bash -s -- --yes
```

The options `-y` or `--assume-yes` are also accepted and have the same result. 

## <a name="uninstall"></a>How do I uninstall RaspAP?
An uninstaller is provided to remove RaspAP cleanly, and also restore any backups of your configuration that were created before RaspAP was installed. Start the uninstaller with the following:

```
curl -sL https://install.raspap.com | bash -s -- --uninstall
```

Alternatively, you may execute the uninstaller directly from the project folder (default location is `/var/www/html`):

```
cd /var/www/html
source installers/uninstall.sh
_remove_raspap
```

Whichever method you choose, the result is the same. Check your network configuration before rebooting to ensure you can still access your device.

