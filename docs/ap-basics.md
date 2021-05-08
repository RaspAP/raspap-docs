# Access point settings

## Basics

After running the [Quick installer](/quick/) or following the [manual installation](/manual/) steps, RaspAP will start up a routed wireless access point (AP) with a [default configuration](/defaults/).
As part of this initial setup, the `hostapd` service broadcasts an AP with the following settings:

**Interface:** `wlan0`  
**SSID:** `raspi-webgui`  
**Wireless Mode:** `802.11n - 2.4GHz`  
**Channel:** `1`  
**Security Type:** `WPA2`  
**Encryption Type:** `CCMP`  
**Passphrase:** `ChangeMe`  

> :information_source: **Note:** The **802.11 AC 5GHz** wireless mode option is disabled by default. It may be enabled by configuring a country that permits wireless operation on the 5GHz band. Refer to [this FAQ](/faq/#80211ac) for more information.

Each of these settings may be changed on the **Hotspot > Basic** and **Security** tabs to any values you wish. Your changes will be applied and made visible on the broadcasted AP by choosing
**Save settings** followed by **Restart hotspot**.

![](https://user-images.githubusercontent.com/229399/115685883-efc44900-a358-11eb-8b9b-95c1029a2cad.png)

At this point, a dialog will appear to indicate the progress of the RaspAP service. This is a Linux `systemd` process that is responsible for starting up several network services in a specific order and timing.

## Connecting clients
When the AP is operational, you may connect clients to it by using one of two methods:

1. Select the SSID from the list of available networks on your device and enter the passphrase.
2. Scan the QR code displayed on the **Hotspot > Security** tab and join the AP.

By default, clients are assigned IP addresses from the DHCP range `10.3.141.50 — 10.3.141.255`. These values may be changed in the **DHCP options** section of the **DHCP server** settings UI. If for some reason a client is unable to obtain an IP address from your AP, consult [this FAQ](/faq/#noip).

## Advanced options
The above sections cover everything you will need for a basic routed AP. The **Hotspot > Advanced** tab has several options that allow you to control advanced settings for the Linux `hostapd` service. These are discussed in the following sections.

### Bridged AP mode
If you wish to configure RaspAP as a [bridged AP](/bridged/), this may be done by sliding the **Bridged AP mode** toggle, saving settings and restarting the hotspot. Be aware that when the hotspot restarts
you will no longer be able to access the web interface from the default `10.1.141.1` address. Refer to this [explanation and tips](/bridged/#accessing-the-web-interface) for administering your bridged AP. 

### WiFi client AP mode
RaspAP has support for this special mode, also known as a **micro-AP** or simply **AP-STA**. Typically this can be difficult to configure manually, but RaspAP performs most of the config work behind the scenes for you.

> :information_source: **Note:** This option is disabled or "greyed out" until a wireless client is configured. This can be done via the **WiFi client** UI, or by manually [configuring a valid `wpa_supplicant.conf`](/faq/#how-do-i-prepare-the-sd-card-to-connect-to-wifi-in-headless-mode).

Before using this mode, it is recommended that users familiarize themselves with [how AP-STA works](/ap-sta/). Users of AP-STA mode should also be aware of its limitations, and understand that performance and stability of this AP mode will not be equal to using a second wireless adapter bound to a separate interface.
For the latter, refer to [this FAQ](/faq/#can-i-use-wlan0-and-wlan1-rather-than-eth0-for-my-ap). 

### Beacon interval
Wireless APs continuously send beacon frames to indicate their presence, traffic load, and capabilities. The default `hostapd` beacon interval is 100ms. If desired, you may change this to any value between 15 and 65535.

### Disable disassoc_low_ack
An AP may disassociate a client due to inactivity, transmission failures or other indications of connection loss. This phenomenon can usually be observed in the `hostapd` logs like so:

```
wlan0: AP-STA-DISCONNECTED 24:62:ab:fd:24:34
wlan0: STA 24:62:ab:fd:24:34 IEEE 802.11: disassociated
wlan0: STA 24:62:ab:fd:24:34 IEEE 802.11: deauthenticated due to inactivity (timer DEAUTH/REMOVE)
``` 

This option sets the `disassoc_low_ack` boolean value for `hostapd`. Be aware that this value is dependent on driver capabilities. Moreover, `hostapd` may disassociate a client (or station) for
a variety of reasons, so this is not a silver bullet.

### Transmit power
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](/insiders/)

[Insiders](/insiders/) are able to control the transmit power of the configured AP interface. The default "auto" setting will suffice for the vast majority of APs. A lower `txpower` value
can be useful to mitigate WiFi radio interference, for example if you are hosting multiple APs in a given area. It can also be advantageous to set `txpower` to a lower value in IoT or similar applications where reduced power consumption is needed.
 
![](https://user-images.githubusercontent.com/229399/115698577-0f616e80-a365-11eb-80e5-404527ca7bdb.png){: style="width:375px"}

Set the transmit power by selecting a value from the dropdown and choosing **Save settings**. The transmit power setting is expressed as dBm, or decibels (dB) with reference to one milliwatt (mW). 
It is not necessary to restart the AP for this to take effect. 

### Maximum number of clients
This option sets the `max_num_sta` value for `hostapd`, and is effective for placing a limit on the number of clients (stations) that can connect to your AP. When the limit is reached, new client connections will be rejected.

> :information_source: **Note:** The default setting is 2007, but this is merely the value set by `hostapd` from the IEEE 802.11 specification. It should _not_ be interpreted as a guarantee that RaspAP can support this many simultaneous clients.
In practice, this number depends on several factors and is a much lower value, as discussed in [this FAQ](/faq/#maxclients).  

## Troubleshooting
RaspAP gives you advanced control over several Linux networking-related services. As a result, your AP may fail to start for a variety of reasons. You may also encounter errors connecting clients to 
the AP, have no internet on AP clients, or observe clients being disconnected from the AP for no apparent reason. 

If any of the above happens, one of the best diagnostic tools at your disposal is RaspAP's built-in service logging facility. You may enable the `hostapd` service log by sliding the **Logfile output** toggle on the **Hotspot > Logging** tab and choosing **Save settings**. Finally, choose
**Restart hotspot** and check the log output.

![](https://user-images.githubusercontent.com/229399/116439036-5c56b080-a84f-11eb-87ee-318932347daf.png)

Similarly, you may also enable DHCP server activity by sliding either of the two logging options on the **DHCP server > Logging** tab.

### Diagnosing problems
Look for any reported errors logged by the `hostapd`, `dhcpcd` or `dnsmasq` services. In most cases, errors thrown by one or more of these services have been discussed in various online forums.
Start by searching the official [Raspberry Pi forums](https://www.raspberrypi.org/forums/) or [Raspberry Pi on Stack Exchange](https://raspberrypi.stackexchange.com/).
Chances are the problems with your AP have been discussed and answered before.

The RaspAP [FAQ](/faq/) is a rich source of troubleshooting info that is continuously updated with answers to the most commonly asked questions.  

> :information_source: **Protip:** Capture output from the Linux kernel's message buffer with `dmesg` to help diagnose failure events. Read the last 100 lines with `dmesg | tail -100` and look 
for any anomalies.

### Reverting to base settings
It is always advisable to begin with RaspAP's [default configuration](/defaults/), which has been rigorously tested and validated with the project's [supported operating systems](/#compatible-operating-systems).
If, after modifying RaspAP's default settings, your AP no longer functions as expected, simply run the [Quick installer](/quick/#usage) again to restore these defaults.

### Accessing backups
Each time you revert to RaspAP's base settings, your existing service configuration files are automatically backed up to `/etc/raspap/backups`. In this way, you can compare differences between your files and the default configuration, if needed.
There are many ways to do this in Linux, such as using the built-in GNU `diff` tool. Another option is to install `colordiff`, a wrapper for diff that produces the same output but with colored syntax highligting.
Install `colordiff` with `sudo apt-get install colordiff`.

Similarly, the web files located in the default `/var/www/html` root are backed up to `/var/www` in a directory named with a timestamp. Therefore, any changes you've made to RaspAP's internals are preserved. 

