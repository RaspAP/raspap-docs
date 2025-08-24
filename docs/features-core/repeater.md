# WiFi repeater

![](https://user-images.githubusercontent.com/229399/224082441-d9db2204-2ea5-434a-b96a-c23aef581a80.jpg){: style="width:640px"}

## Overview
A popular use case for RaspAP is to connect to your wireless network and rebroadcast an existing wireless signal. Often known as a *wireless repeater* or *extender*, this setup is particularly useful if you are 
experiencing problems with "dead spots" in your WiFi network. This step-by-step walkthrough will assist you in creating this configuration. 

## How a WiFi repeater works
A WiFi repeater receives an existing WiFi signal, amplifies it and then transmits the boosted signal. With this arrangment you can effectively double the coverage area of your WiFi network &#151; reaching far corners of your home or office, different floors, or even extend coverage outside to a yard or garage. A repeater effectively contains two wireless routers and a minimum of two antennas. One of these wireless routers picks up the existing WiFi network. It then transfers the signal to the other wireless router, which retransmits the boosted signal.

???+ note "Note"
    A wireless repeater will restrict your maximum throughput. This is because WiFi is a half-duplex system, meaning only one device may transmit data at any given time. The repeater must accept incoming and outgoing packets from clients and forward those packets on to the next WiFi router and accept replies. In practice, you can expect half the bandwidth as a non-boosted signal, as each packet must go over the air twice.

We will create this setup with a WiFi-capable Raspberry Pi (or similar device) and an external USB wireless adapter, or dongle.

## Steps to create a repeater

![](https://user-images.githubusercontent.com/229399/223980087-08c788b7-5f26-434e-8b1d-753956e37195.png){: style="width:640px"}

Refer to the diagram above as we walk through the steps of creating this configuration.

### Connect a USB WiFi dongle
Begin by connecting an external wireless adapter to a USB port on your device. Your choice of adapter is important &#151; external WiFi adapters (ie, "dongles") vary greatly in terms of hardware capabilities and driver support. Many do not have support for AP mode, require a powered USB hub, manual driver and/or firmware installation or are otherwise not well suited for this application.

To determine if your USB WiFi adapter is capable of hosting an AP, execute the following:

```
$ iw list
...
	Supported interface modes:
		 * IBSS
		 * managed
		 * AP
		 * P2P-client
		 * P2P-GO
		 * P2P-device
```

If "AP" does not appear in the list above, save yourself some time and find another adapter.

You should also pair an adapter with the wireless mode you intend to operate from your device's onboard wireless chipset. For example, if you wish to use a Raspberry Pi 4's 802.11ac 5 GHz wireless mode, make sure your adpater also supports this mode. 

We strongly recommend [this resource](https://github.com/morrownr/USB-WiFi) which lists USB WiFi adapters with in-kernel Linux drivers. These will work out of the box on Debian-based devices without
installing third-party drivers. You may also wish to skip directly to this [short list](https://github.com/morrownr/USB-WiFi/blob/main/home/The_Short_List.md) of "superstar" USB WiFi adapters for Linux. Pay special attention to those that are excellent choices for 5 GHz AP mode, if this
is desired.

### Create the access point
After [installing RaspAP](../get-started/index.md) your device will broadcast an 802.11g 2.4 GHz access point with the SSID `RaspAP`. By default, this uses your device's onboard wireless adapter and the `wlan0` interface. Your AP configuration may be changed at any time, however it's recommended to change the default password at minimum before proceeding. You may also wish to change the SSID and wireless mode.

!!! note "Note"
    The 802.11ac 5 GHz option is disabled until you configure your device's wireless regulatory domain. See [this FAQ](../faq.md#80211ac) for more information.  

### Connect device to WiFi
With your USB dongle connected and AP active, use RaspAP's **WiFi client** interface to select and authenticate with your existing wireless router. 

![](https://user-images.githubusercontent.com/229399/229068398-25525131-7262-4aed-a5ac-4cd8e9b7782f.png){: style="width:520px"}

Alternatively, if you've used software such as the [Raspberry Pi imager](https://www.raspberrypi.com/software/) to install an OS on your microSD card, you may choose the "Configure wireless LAN" option
before booting your device for the first time. This will configure your `wpa_supplicant.conf` and your device should already be connected to your WLAN. In this case, you may skip this step.

### Configure routing
Your current network configuration will display two default routes. This may be confirmed by checking the **Routing table** output on RaspAP's **Networking** interface. In the example below, `wlan0` is the
AP interface and has a default route (identified by the `default` label) and a metric value of `303`:

![](https://user-images.githubusercontent.com/229399/224091327-2481764c-3b39-48f7-b7a2-26b3587db8e2.png){: style="width:520px"}

Note that our USB adapter is on the `wlan1` interface and has a higher metric value of `304`. It also has a default route. Until we configure these metrics, our WiFi repeater does not know how to route
packets from `wlan1` (the client interface) to `wlan0` (the AP interface) and vice versa. Clients connected to the AP will *not* have internet connectivity. Fortunately, this is easily fixed.

Metrics and default routes are used by `dhcpcd`, the [DHCP daemon](https://man.archlinux.org/man/core/dhcpcd/dhcpcd.8.en). Contrary to [popular belief](https://www.reddit.com/r/RaspAP/comments/10601do/issues_with_raspap_and_routing_traffic_from_wlan0/), RaspAP does not manipulate the IP routing table or set interface priorities without user input. The Linux kernel sets default metric values when 
the interface is brought up and will usually choose the network routes it decides is best. The DHCP daemon uses these metrics to prioritize interfaces, where lower values are given a higher priority.

To configure routing for our repeater, select `wlan0` (the AP interface, in this example) from the **DHCP Server settings** interface. Be sure that the "Install a default route for this interface" option is disabled. 

![](https://user-images.githubusercontent.com/229399/147859041-5abaab36-b474-43a4-98f6-5aebfca5c9bf.png){: style="width:520px"}

Scroll to the bottom and set a metric value of `305` for this interface, then choose **Save settings**:

![](https://user-images.githubusercontent.com/229399/224007041-f1f11f60-0545-4673-a87d-7c6297d2b129.png){: style="width:520px"}

This instructs the DHCP daemon to treat the `wlan0` interface with a lower priority than the `wlan1` interface. There's nothing magic about the value "305" in this example &#151; the important thing is that the AP interface has a higher value, and thus a lower priorty, than the `wlan1` interface. 

For your changes to take effect, choose **Restart hotspot** from the **Hotspot** interface.

Behind the scenes, RaspAP has configured the `wlan0` interface in `/etc/dhcpcd.conf` like so:

```
# RaspAP wlan0 configuration
interface wlan0
static ip_address=10.3.141.1/24
static routers=10.3.141.1
metric 305
nogateway
```

This is reflected in the updated routing table, visible on the **Networking** interface. In the example below, the `wlan0` interface hosting the AP no longer has a default route and shows a higher metric
value (lower priority) than the `wlan1` interface:

![](https://user-images.githubusercontent.com/229399/224091951-2ec46f45-c552-4cf4-87f4-384fa6f52ada.png){: style="width:520px"}

If you don't see these changes in the routing table, be sure to restart the hotspot. 

### Alternate routing method
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](../features-insiders/index.md)

As a convenience, [Insiders](../features-insiders/index.md) are able to configure routing automatically by enabling the **WiFi repeater mode** toggle on the **Hotspot > Advanced** tab.

![WiFi repeater mode](https://github.com/RaspAP/raspap-webgui/assets/229399/fce68f76-2770-4d3e-99e1-ee9132408a0a){: style="width:420px"}

Save settings and choose **Start hotspot** or **Restart hotspot** to activate the wireless repeater.

!!! info "Info"
    As with [WiFi client AP mode](../features-experimental/ap-sta.md), the **WiFi repeater mode** option is disabled or "greyed out" until a wireless client is configured. 

### Connecting clients
At this stage, you may connect clients to the AP as you would normally. Two different methods are [described here](ap-basics.md#connecting-clients).

### Switching interfaces
If you would like to switch the wlan interfaces, select a different interface for the AP on the **Hotspot > Basic** tab, then choose **Save settings**. Reverse the DHCP settings in the previous step, then restart the AP or reboot your device. In order to still be able to access the web UI, connect your device via an ethernet cable.

### Troubleshooting
If your clients do not have internet connectivity, start by following these [troubleshooting steps](../get-started/troubleshooting.md). In most cases, problems may be diagosed and fixed by checking the service 
logs and RaspAP's **Networking** interface. Help is available from the sources [mentioned here](../get-started/troubleshooting.md#diagnosing-problems).

## Speed testing
RaspAP hosts a fast, open source and privacy-focused [public speed test server](../features-insiders/speedtest.md) that you can use to evaluate your WiFi repeater's performance. The remote host is RaspAP's public [speedtest server](https://speedtest.raspap.com/) located in the United States. Additional speedtest hosts distributed in other geographic centers are forthcoming.

## Discussions
Questions or comments about configuring a WiFi repeater? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).
