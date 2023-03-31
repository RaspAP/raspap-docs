# Multiple APs

## Overview
:octicons-beaker-24: Experimental

Many users have asked if it's possible to create a second wireless access point on the same device. The answer is "yes" with an AP-capable external wireless adapter and the correct settings.
The [Edimax EW-7811Un USB adapter](https://www.edimax.com/edimax/merchandise/merchandise_detail/data/edimax/us/wireless_adapters_n150/ew-7811un/) works without additional drivers on many devices, including the Raspberry Pi.
For this reason it is used in this walkthrough.

## Scenario
In this setup, we will use an external Edimax 2.4GHz USB adapter together with the onboard wireless chipset of the Raspberry Pi 4 operating on the 5GHz band. The end result is displayed in the WiFi network scan below.

![](https://user-images.githubusercontent.com/229399/121822121-a380ef80-cc9d-11eb-94a1-d404adc07b78.png){: style="width:520px"}

It is not currently possible to create this configuration with RaspAP's UI, so these manual steps are provided below.

## Prerequisites
This tutorial assumes that you have followed the [Quick start](index.md#quick-start) or [manual installation](manual.md) instructions.
If an **802.11 AC 5GHz** wireless mode is desired with the RPi's onboard chipset, you must first configure a country that permits wireless operation on the 5GHz band. Refer to [this FAQ](faq.md#80211ac) for more information.

## Create the hostapd configs
The simplest method to achieve this is to use RaspAP's **Hotspot > Basic** tab to create the base configurations. Configure an AP for the onboard `wlan0` interface with the settings shown below. Choose **Save settings** to write this to the filesystem. 

![](https://user-images.githubusercontent.com/229399/121924564-5011ae80-cd3c-11eb-81c8-114972d1a05b.png){: style="width:420px"}

Open your preferred terminal program and enter the following command to copy this as a new `wlan0` configuration:

```
sudo cp /etc/hostapd/hostapd.conf /etc/hostapd/wlan0.conf
```

Next, configure a second AP for the external `wlan1` interface with the settings shown below. Again, choose **Save settings** to write this to the filesystem.

![](https://user-images.githubusercontent.com/229399/121924637-63247e80-cd3c-11eb-94b1-bf4e1f848fd3.png){: style="width:420px"}

Enter the following command to copy this as a new `wlan1` configuration:

```
sudo cp /etc/hostapd/hostapd.conf /etc/hostapd/wlan1.conf
```

!!! tip "Tip"
    If you decide to create two APs on the same band, for example 802.11n 2.4GHz, be sure to select two different channels for each interface.

## Configure dnsmasq
RaspAP's [default settings](defaults.md) includes a preconfigured `wlan0` file for the `dnsmasq` service. Execute `cat /etc/dnsmasq.d/090_wlan0.conf` to display its contents:

```
# RaspAP wlan0 configuration
interface=wlan0
domain-needed
dhcp-range=10.3.141.50,10.3.141.254,255.255.255.0,12h
```

Next, we will copy this file and make some modfications to it:

```
sudo cp /etc/dnsmasq.d/090_wlan0.conf /etc/dnsmasq.d/090_wlan1.conf
sudo nano /etc/dnsmasq.d/090_wlan1.conf
```

Edit this file so it looks like the example below, then save it and exit your editor.

```
# RaspAP wlan1 configuration
interface=wlan1
domain-needed
dhcp-range=10.4.141.50,10.4.141.254,255.255.255.0,12h
```

## Configure dhcpcd
Similar to `dnsmasq`, the `dhcpcd` service is preconfigured with RaspAP's [default settings](defaults.md). Open this file in an editor by executing `sudo nano /etc/dhcpcd.conf`, then add a `wlan1` block to the end of the file:

```
# RaspAP default configuration
hostname
clientid
persistent
option rapid_commit
option domain_name_servers, domain_name, domain_search, host_name
option classless_static_routes
option ntp_servers
require dhcp_server_identifier
slaac private
nohook lookup-hostname

# RaspAP wlan0 configuration
interface wlan0
static ip_address=10.3.141.1/24
static routers=10.3.141.1
static domain_name_server=9.9.9.9 1.1.1.1

# RaspAP wlan1 configuration
interface wlan1
static ip_address=10.4.141.1/24
static routers=10.4.141.1
static domain_name_server=9.9.9.9 1.1.1.1
```

!!! note "Note"
    RaspAP only manipulates `/etc/hostapd/hostapd.conf` so your custom hostapd configs won't be touched. The [version 2.6](https://github.com/billz/raspap-webgui/releases/tag/2.6-beta) release lets you manage the `dhcpcd` and `dnsmasq` configs from the UI, while also preserving any manual changes.

Finally, enable the **Log DHCP requests** toggle on RaspAP's **DHCP Server > Logging** tab. Be sure to restart the `dnsmasq` service. 
## Starting the hotspots
Ensure that `hostapd` is not already running before proceeding. You may stop the service with `sudo systemctl stop hostapd.service` or by using the **Stop hotspot** button in RaspAP's UI.
Now we are ready to run `hostapd` interactively with the configurations we've created above. The debug switch `-dd` is optional but useful for troubleshooting:

```
sudo hostapd -dd /etc/hostapd/wlan0.conf /etc/hostapd/wlan1.conf
```

Connect clients to each AP and monitor the output. You may stop `hostapd` from the terminal with the ++ctrl+c++ keystroke. Alternatively, you may send the process to the background with ++ctrl+z++ and restore it to the foreground with `fg`.

## Troubleshooting
With RaspAP's DHCP logging option enabled, it can be useful to monitor this service's activity from the terminal. Execute `tail -f /tmp/dnsmasq.log` and try associating and disconnecting client devices from each AP.

