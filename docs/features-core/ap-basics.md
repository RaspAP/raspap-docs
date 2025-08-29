# Access point settings

## Basics

After booting a [custom OS](../get-started/simple-setup.md#pre-built-image), running the [Quick installer](../get-started/quick-installer.md), [Docker setup](../get-started/docker.md) or following the [manual installation](../get-started/manual.md) steps, RaspAP will start up a routed wireless access point (AP) with a [default configuration](../get-started/defaults.md).
As part of this initial setup, the `hostapd` service broadcasts an AP with the following settings:

**Interface:** `wlan0`  
**SSID:** `RaspAP`  
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

By default, clients are assigned IP addresses from the DHCP range `10.3.141.50 — 10.3.141.254`. These values may be changed in the **DHCP options** section of the **DHCP server** settings UI. If for some reason a client is unable to obtain an IP address from your AP, consult [this FAQ](../faq.md#noip).

## 802.11ac 5 GHz
For devices with compatible wireless hardware, RaspAP [version 3.0](https://github.com/RaspAP/raspap-webgui/releases/tag/3.0) largely removes the guesswork in creating a 5 GHz access point. It achieves this by being tightly integrated with the [wireless regulatory database](https://wireless.wiki.kernel.org/en/developers/Regulatory/wireless-regdb) used by the Linux kernel. Behind the scenes, RaspAP queries `iw` and intelligently matches its output with the 5 GHz channels allowed by `hostapd`, the user space daemon access point software.

From the **Hotspot > Advanced** tab, select your country from the dropdown then choose **Save settings**. This sets the wireless regulatory domain for your device. Now, on the **Hotspot > Basic** tab choose an interface and select the `802.11ac - 5 GHz` wireless mode option. RaspAP will automatically populate the available 5 GHz channels for your country. Select a channel followed by **Save settings**, then **Start** or **Restart hotspot**.

!!! tip "Tip"
    Not all AC channels may be compatible with your hardware. If your hotspot fails to start, enable `hostapd` service logging by sliding the **Logfile output** toggle on the **Hotspot > Logging** tab, followed by **Save settings**, then **Restart hotspot**. See [this FAQ](../faq.md#actroubleshoot) for more assistance. 

If the **Channel** dropdown and **Save settings** button are disabled, refer to [this FAQ](../faq.md#channels).

## Security settings
WPA2 is currently the most secure standard utilizing AES (Advanced Encryption Standard) and a pre-shared key for authentication. WPA2 is also backwards compatible with TKIP to allow interoperability with legacy devices. AES uses the CCMP encryption protocol which is a stronger algorithm for message integrity and confidentiality.

By default, RaspAP's access point is configured with WPA2 and CCMP encryption. You may of course change this to allow legacy clients (older mobile devices, for example) by selecting `TKIP+CCMP` as the encryption type. Choose **Save settings** and **Restart hotspot** for your changes to take effect. 

### WPA3-Personal
:octicons-beaker-24: Experimental 

WPA3 is an improved encryption standard, thanks to Simultaneous Authentication of Equals (SAE) which replaces the Pre-Shared Key (PSK) authentication method used in prior WPA
versions. WPA3-Personal allows for better password-based authentication even when using simple passphrases. In general, WPA3-Personal networks with simple passphrases are more difficult to crack
by using brute-force, dictionary-based methods, as with WPA/WPA2.

![](https://user-images.githubusercontent.com/229399/148420827-51b176de-182e-48eb-962d-2943a47c8549.png){: style="width:400px"}

WPA3 also requires the use of Protected Management Frames (PMFs) to increase network security. If you wish to connect AP clients that may not have support for WPA3-Personal or PMFs, a transitional 
security mode is also available.

!!! note "Note"
    The Raspberry Pi's onboard wireless chipsets do not currently support the WPA3 standard. For this reason, in order to use this setting you will need to configure your AP with an external wireless adapter that supports WPA3.  

### 802.11w
:octicons-beaker-24: Experimental

The 802.11w amendment was introduced as a way to secure Wi-Fi management frames against attacks by ensuring that these frames are legitimately exchanged between an AP and its clients, rather than
a malicious third-party. These 802.11w Protected Management Frames (PMFs) can mitigate common types of "deauthentication" and "disassociation" attacks.

Similar to WPA3-Personal, 802.11w may be configured in one of two modes: enabled and required. _Enabled_ allows for mixed operation by allowing legacy devices that do not support 802.11w to associate
while also allowing devices that support 802.11w to use the PMF features. _Required_ will prevent clients that do not support 802.11w from associating with the SSID.

## Printable signs
Beneath the QR code on the **Hotspot > Security** tab, you will find a link to open a "Wi-Fi connect" sign suitable for printing. Click or tap the link after the :fontawesome-solid-print: printer icon to open a new window with your hotspot's QR code, SSID and password neatly formatted.

![](https://user-images.githubusercontent.com/229399/148738058-dfe7ea04-d59b-460a-a8b8-f0fca15ef715.png){: style="width:580px"}

To print, select **File > Print** from your browser's toolbar and adjust print preferences as needed. This feature can be especially useful if you operate a public wireless access point. You may also
opt to integrate a [captive portal](captive.md) for your visitors.

## Advanced options
The above sections cover everything you will need for a basic routed AP. The **Hotspot > Advanced** tab has several options that allow you to control advanced settings for the Linux `hostapd` service. These are discussed in the following sections.

### Bridged AP mode
If you wish to configure RaspAP as a [bridged AP](bridged.md), this may be done by sliding the **Bridged AP mode** toggle, saving settings and restarting the hotspot. Be aware that when the hotspot restarts
you will no longer be able to access the web interface from the default `10.3.141.1` address. Refer to this [explanation and tips](bridged.md#accessing-the-web-interface) for administering your bridged AP. 

### WiFi repeater mode
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](../features-insiders/index.md)

RaspAP is capable of acting as a [wireless repeater](repeater.md) to connect to your wireless network and rebroadcast an existing signal. This requires configuring interface metrics and default routes with DHCP. Alternatively, enabling the **WiFi repeater mode** toggle will create these settings for you automatically.

![WiFi repeater mode](https://github.com/RaspAP/raspap-webgui/assets/229399/fce68f76-2770-4d3e-99e1-ee9132408a0a){: style="width:420px"}

Save settings and choose **Restart hotspot** to active the wireless repeater. As with AP-STA mode, described below, this option is disabled or "greyed out" until a wireless client is configured. 

### WiFi client AP mode
RaspAP lets you enable this special mode, also known as a **micro-AP** or simply **AP-STA**. Before using this mode, it's essential that users familiarize themselves with [how AP-STA works](../features-experimental/ap-sta.md).

!!! warning "Important"
    This mode is experimental and _completely unsupported_. Issues or discussions related to AP-STA in RaspAP's GitHub repository will be moderated. 

Users of AP-STA mode should also be aware of its limitations, and understand that performance and stability of this AP mode will not be equal to using a second wireless adapter bound to a separate interface. For the latter, refer to [this FAQ](../faq.md#can-i-use-wlan0-and-wlan1-rather-than-eth0-for-my-ap). 

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
    The default setting is 2007, but this is merely the value set by `hostapd` from the IEEE 802.11 specification. It should _not_ be interpreted as a guarantee that RaspAP can support this many simultaneous clients. In practice, this number depends on several factors and is a much lower value, as discussed in [this FAQ](../faq.md#maxclients).  

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

## Discussions
Questions or comments about using access point settings? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).

