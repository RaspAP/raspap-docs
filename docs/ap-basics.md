# Access point settings

## Basics

After running the [Quick installer](quick.md), [Docker setup](docker.md) or following the [manual installation](manual.md) steps, RaspAP will start up a routed wireless access point (AP) with a [default configuration](defaults.md).
As part of this initial setup, the `hostapd` service broadcasts an AP with the following settings:

**Interface:** `wlan0`  
**SSID:** `raspi-webgui`  
**Wireless Mode:** `802.11n - 2.4GHz`  
**Channel:** `1`  
**Security Type:** `WPA2`  
**Encryption Type:** `CCMP`  
**Passphrase:** `ChangeMe`  

Each of these settings may be changed on the **Hotspot > Basic** and **Security** tabs to any values you wish. Your changes will be applied and made visible on the broadcasted AP by choosing
**Save settings** followed by **Restart hotspot**.

![](https://user-images.githubusercontent.com/229399/115685883-efc44900-a358-11eb-8b9b-95c1029a2cad.png)

At this point, a dialog will appear to indicate the progress of the RaspAP service. This is a Linux `systemd` process that is responsible for starting up several network services in a specific order and timing.

## Connecting clients
When the AP is operational, you may connect clients to it by using one of two methods:

1. Select the SSID from the list of available networks on your device and enter the passphrase.
2. Scan the QR code displayed on the **Hotspot > Security** tab and join the AP.

By default, clients are assigned IP addresses from the DHCP range `10.3.141.50 — 10.3.141.254`. These values may be changed in the **DHCP options** section of the **DHCP server** settings UI. If for some reason a client is unable to obtain an IP address from your AP, consult [this FAQ](faq.md#noip).

## 802.11ac 5 GHz
For devices with compatible wireless hardware, RaspAP [version 3.0](https://github.com/RaspAP/raspap-webgui/releases/tag/3.0) largely removes the guesswork in creating a 5 GHz access point. It achieves this by being tightly integrated with the [wireless regulatory database](https://wireless.wiki.kernel.org/en/developers/Regulatory/wireless-regdb) used by the Linux kernel. Behind the scenes, RaspAP queries `iw` and intelligently matches its output with the 5 GHz channels allowed by `hostapd`, the user space daemon access point software.

From the **Hotspot > Advanced** tab, select your country from the dropdown then choose **Save settings**. This sets the wireless regulatory domain for your device. Now, on the **Hotspot > Basic** tab choose an interface and select the `802.11ac - 5 GHz` wireless mode option. RaspAP will automatically populate the available 5 GHz channels for your country. Select a channel followed by **Save settings**, then **Start** or **Restart hotspot**.

!!! tip "Tip"
    Not all AC channels may be compatible with your hardware. If your hotspot fails to start, enable `hostapd` service logging by sliding the **Logfile output** toggle on the **Hotspot > Logging** tab, followed by **Save settings**, then **Restart hotspot**. See [this FAQ](faq.md#actroubleshoot) for more assistance. 

If the **Channel** dropdown and **Save settings** button are disabled, refer to [this FAQ](faq.md#channels).

## Security settings
WPA2 is currently the most secure standard utilizing AES (Advanced Encryption Standard) and a pre-shared key for authentication. WPA2 is also backwards compatible with TKIP to allow interoperability with legacy devices. AES uses the CCMP encryption protocol which is a stronger algorithm for message integrity and confidentiality.

By default, RaspAP's access point is configured with WPA2 and CCMP encryption. You may of course change this to allow legacy clients (older mobile devices, for example) by selecting `TKIP+CCMP` as the encryption type. Choose **Save settings** and **Restart hotspot** for your changes to take effect. 

### WPA3-Personal
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

WPA3 is an improved encryption standard, thanks to Simultaneous Authentication of Equals (SAE) which replaces the Pre-Shared Key (PSK) authentication method used in prior WPA
versions. WPA3-Personal allows for better password-based authentication even when using simple passphrases. In general, WPA3-Personal networks with simple passphrases are more difficult to crack
by using brute-force, dictionary-based methods, as with WPA/WPA2.

![](https://user-images.githubusercontent.com/229399/148420827-51b176de-182e-48eb-962d-2943a47c8549.png){: style="width:400px"}

WPA3 also requires the use of Protected Management Frames (PMFs) to increase network security. If you wish to connect AP clients that may not have support for WPA3-Personal or PMFs, a transitional 
security mode is also available.

!!! note "Note"
    The Raspberry Pi's onboard wireless chipsets do not currently support the WPA3 standard. For this reason, in order to use this setting you will need to configure your AP with an external wireless adapter that supports WPA3.  

### 802.11w
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

The 802.11w amendment was introduced as a way to secure Wi-Fi management frames against attacks by ensuring that these frames are legitimately exchanged between an AP and its clients, rather than
a malicious third-party. These 802.11w Protected Management Frames (PMFs) can mitigate common types of "deauthentication" and "disassociation" attacks.

Similar to WPA3-Personal, 802.11w may be configured in one of two modes: enabled and required. _Enabled_ allows for mixed operation by allowing legacy devices that do not support 802.11w to associate
while also allowing devices that support 802.11w to use the PMF features. _Required_ will prevent clients that do not support 802.11w from associating with the SSID.

## Drag & drop widgets
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

The default dashboard layout may be customized to suit your needs. Enable this option from the **System > Theme** menu by selecting the **Dynamic widgets** toggle. Next, from the **Dashboard** click or tap the :fontawesome-solid-pen: icon to modify the widgets. Each widget may be resized, dragged and repositioned. Release the widget to drop it into a new location.

!!! tip "Tip"
    This option works best for large displays. The default dashboard widgets are optimized for mobile devices and smaller displays. 

<video width="680" height="500" controls>
  <source src="https://user-images.githubusercontent.com/229399/162409566-1c2195ce-1dfe-46e0-b2df-9e8972c3bb6f.mov" type="video/mp4">
</video>

Click or tap the :fontawesome-solid-pen: icon a second time when you're done making changes. The new responsive dashboard layout will be saved to your browser's local storage.

## Printable signs
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

Beneath the QR code on the **Hotspot > Security** tab, you will find a link to open a "Wi-Fi connect" sign suitable for printing. Click or tap the link after the :fontawesome-solid-print: printer icon to open a new window with your hotspot's QR code, SSID and password neatly formatted.

![](https://user-images.githubusercontent.com/229399/148738058-dfe7ea04-d59b-460a-a8b8-f0fca15ef715.png){: style="width:580px"}

To print, select **File > Print** from your browser's toolbar and adjust print preferences as needed. This feature can be especially useful if you operate a public wireless access point. You may also
opt to integrate a [captive portal](captive.md) for your visitors.

## Advanced options
The above sections cover everything you will need for a basic routed AP. The **Hotspot > Advanced** tab has several options that allow you to control advanced settings for the Linux `hostapd` service. These are discussed in the following sections.

### Bridged AP mode
If you wish to configure RaspAP as a [bridged AP](bridged.md), this may be done by sliding the **Bridged AP mode** toggle, saving settings and restarting the hotspot. Be aware that when the hotspot restarts
you will no longer be able to access the web interface from the default `10.1.141.1` address. Refer to this [explanation and tips](bridged.md#accessing-the-web-interface) for administering your bridged AP. 

### WiFi repeater mode
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

RaspAP is capable of acting as a [wireless repeater](repeater.md) to connect to your wireless network and rebroadcast an existing signal. This requires configuring interface metrics and default routes with DHCP. Alternatively, enabling the **WiFi repeater mode** toggle will create these settings for you automatically.

![WiFi repeater mode](https://github.com/RaspAP/raspap-webgui/assets/229399/fce68f76-2770-4d3e-99e1-ee9132408a0a){: style="width:420px"}

Save settings and choose **Restart hotspot** to active the wireless repeater. As with AP-STA mode, described below, this option is disabled or "greyed out" until a wireless client is configured. 

### WiFi client AP mode
RaspAP has support for this special mode, also known as a **micro-AP** or simply **AP-STA**. Typically this can be difficult to configure manually, but RaspAP performs most of the config work behind the scenes for you.

!!! note "Note"
    This option is disabled or "greyed out" until a wireless client is configured. This can be done via the **WiFi client** UI, or by manually [configuring a valid `wpa_supplicant.conf`](faq.md#how-do-i-prepare-the-sd-card-to-connect-to-wifi-in-headless-mode).

Before using this mode, it is recommended that users familiarize themselves with [how AP-STA works](ap-sta.md). Users of AP-STA mode should also be aware of its limitations, and understand that performance and stability of this AP mode will not be equal to using a second wireless adapter bound to a separate interface.
For the latter, refer to [this FAQ](faq.md#can-i-use-wlan0-and-wlan1-rather-than-eth0-for-my-ap). 

### Beacon interval
Wireless APs continuously send beacon frames to indicate their presence, traffic load, and capabilities. The default `hostapd` beacon interval is 100ms. If desired, you may change this to any value between 15 and 65535.

### Disable disassoc_low_ack
An AP may disassociate a client due to inactivity, transmission failures or other indications of connection loss. This phenomenon can usually be observed in the `hostapd` logs like so:

```
wlan0: AP-STA-DISCONNECTED 24:62:ab:fd:24:34
wlan0: STA 24:62:ab:fd:24:34 IEEE 802.11: disassociated
wlan0: STA 24:62:ab:fd:24:34 IEEE 802.11: deauthenticated due to inactivity (timer DEAUTH/REMOVE)
``` 

This option sets the `disassoc_low_ack` boolean value for `hostapd`. Be aware that this value is dependent on driver capabilities. Moreover, `hostapd` may disassociate a client (or station) for a variety of reasons, so this is not a silver bullet.

### Transmit power

RaspAP allows you to control the transmit power of the configured AP interface. The default "auto" setting will suffice for the vast majority of APs. A lower `txpower` value
can be useful to mitigate WiFi radio interference, for example if you are hosting multiple APs in a given area. It can also be advantageous to set `txpower` to a lower value in IoT or similar applications where reduced power consumption is needed.
 
![](https://user-images.githubusercontent.com/229399/115698577-0f616e80-a365-11eb-80e5-404527ca7bdb.png){: style="width:375px"}

Set the transmit power by selecting a value from the dropdown and choosing **Save settings**. The transmit power setting is expressed as dBm, or decibels (dB) with reference to one milliwatt (mW). 
It is not necessary to restart the AP for this to take effect. 

### Maximum number of clients
This option sets the `max_num_sta` value for `hostapd`, and is effective for placing a limit on the number of clients (stations) that can connect to your AP. When the limit is reached, new client connections will be rejected.

!!! note "Note"
    The default setting is 2007, but this is merely the value set by `hostapd` from the IEEE 802.11 specification. It should _not_ be interpreted as a guarantee that RaspAP can support this many simultaneous clients. In practice, this number depends on several factors and is a much lower value, as discussed in [this FAQ](faq.md#maxclients).  

### Custom user settings
RaspAP gives you control over many common AP settings via the **Hotspot > Basic**, **Security** and **Advanced** tabs. However, `hostapd` has lots of [other options](https://w1.fi/cgit/hostap/tree/hostapd/hostapd.conf) that aren't exposed in the management UI. For this reason, RaspAP lets advanced users define any number of valid `hostapd` settings by adding them to a custom configuration file.

Begin by creating `/etc/hostapd/hostapd.conf.users` on your device's filesystem, then add your desired settings to this file. For example, to enable `hostapd`'s built-in support for MAC address filtering, you may add the following:

```
# Accept/deny lists are read from separate files (containing list of
# MAC addresses, one per line).
accept_mac_file=/etc/hostapd.accept
deny_mac_file=/etc/hostapd.deny
```

Next, choose **Hotspot > Save settings** to parse this file and append your custom settings to RaspAP's `hostapd` configuration. Finally, choose **Hotspot > Restart hotspot** for your changes to take effect.

!!! tip "Tip"
    Direct manipulation of advanced `hostapd` settings may lead to your AP failing to start and/or other unanticipated behavior. For this reason, it's advisable to enable service logging on the **Hotspot > Logging** tab and monitor the log output for errors. 

## Troubleshooting
RaspAP gives you advanced control over several Linux networking-related services. As a result, your AP may fail to start for a variety of reasons. You may also encounter errors connecting clients to 
the AP, have no internet on AP clients, or observe clients being disconnected from the AP for no apparent reason. 

If any of the above happens, one of the best diagnostic tools at your disposal is RaspAP's built-in service logging facility. You may enable the `hostapd` service log by sliding the **Logfile output** toggle on the **Hotspot > Logging** tab and choosing **Save settings**. Finally, choose
**Restart hotspot** and check the log output.

![](https://user-images.githubusercontent.com/229399/116439036-5c56b080-a84f-11eb-87ee-318932347daf.png){: style="width:580px"}

Similarly, you may also enable DHCP server activity by sliding either of the two logging options on the **DHCP server > Logging** tab.

### Debug log
In some situations, you may need more comprehensive information to self-diagnose a problem. RaspAP lets you generate a debug log with a detailed summary of your system including the installed OS, Linux kernel version, attached USB devices, RaspAP settings, network configuration and current state of several AP-related services.

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

!!! tip "Tip"
    If you are unable to perform a self-diagnosis and would like to share your debug log (or a portion of it) with another party, upload it to <a href="https://pastebin.com/" target="_blank">Pastebin</a> or <a href="https://paste.ubuntu.com/" target="_blank">Ubuntu Pastebin</a>. Please don't paste the log in its entirety to RaspAP's discussions, issues or other support channels.

RaspAP's debug log contains information about your system and local network configuration. However, no passwords or other senstive data are included.

### Diagnosing problems
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
 
### Reverting to base settings
It is generally advisable to begin with RaspAP's [default configuration](defaults.md), which has been rigorously tested and validated with the project's [supported operating systems](index.md#compatible-operating-systems). If, after modifying RaspAP's default settings, your AP no longer functions as expected, you may perform a [system reset](defaults.md#restoring-settings) to restore these defaults.

### Accessing backups
Each time you revert to RaspAP's base settings, your existing service configuration files are automatically backed up to `/etc/raspap/backups`. In this way, you can compare differences between your files and the default configuration, if needed.
There are many ways to do this in Linux, such as using the built-in GNU `diff` tool. Another option is to install `colordiff`, a wrapper for diff that produces the same output but with colored syntax highligting.
Install `colordiff` with `sudo apt-get install colordiff`.

Similarly, the web files located in the default `/var/www/html` root are backed up to `/var/www` in a directory named with a timestamp. Therefore, any changes you've made to RaspAP's internals are preserved. 

## Discussions
Questions or comments about using access point settings? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).

