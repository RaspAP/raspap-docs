# Use cases

## Overview
RaspAP transforms your Raspberry Pi, or other Debian-compatible device, into a powerful and highly configurable wireless router. Two of the most common and well-supported uses cases for RaspAP are as a [dedicated wireless router](use-cases.md#dedicated-router) or a [wireless repeater](use-cases.md#wireless-repeater) for an existing wireless network. 

![connectivity](../images/connectivity.png){: style="width:640px"}

Each of these use cases supports wired and wireless connectivity sources for WAN (on the left side of the diagram, above) and wired or wireless LAN clients (on the right side of the diagram, above).

Sources of internet (WAN) connectivity may include wired Ethernet, WiFi, tethering via a mobile handset, or a cellular-capable HAT. In most scenarios, one of these connection sources is generally used at a time. An exception to this is a technique known as _connection bonding_ from [providers like Speedify](faq.md#speedify). This allows you to combine, or bond, multiple sources of internet connectivity into a single connection.

## Dedicated router
RaspAP is often used to share single wired or wireless connection with multiple clients. Additionally, RaspAP can help you protect your devices and enhance your online privacy with features like [Ad blocking](/features-core/adblock.md), [WireGuard](/features-core/wireguard.md), [OpenVPN](/features-core/openvpn.md), and a [Firewall](/features-core/firewall.md). 

## Wireless repeater
Alternatively, RaspAP can be used to connect to an existing wireless network and rebroadcast a signal. Often known as a _wireless repeater_ or _extender_, this configuration is frequently used to mitigate problems with "dead spots" in a WiFi network, or extend the range of a wireless network to a more distant area. See this [step-by-step walkthrough](/features-core/repeater.md) to get started in creating this configuration.

## Real-world scenarios
RaspAP has been installed millions of times in all corners of the globe. While the uses cases mentioned here are common ones, the ways that RaspAP can be used is limited only by your [specific needs and creativity](https://github.com/RaspAP/raspap-awesome). Below are some popular real-world setups reported by our users: 

### Travel & mobility
- Portable router for RVs and campers - create a secure, portable WiFi network while on the road, with VPN support for privacy.
- Hotel Ethernet connection sharing - Convert a single wired hotel connection into a secure WiFi network for all your devices
- Portable media server - Combine Plex/Jellyfin streaming with network access for offline entertainment anywhere

### Workshops & cybersecurity
- Packet capture & analysis - Network monitoring and debugging with integrated [Wireshark](/features-insiders/wireshark.md) support
- Wireless workshops - Dedicated network for 3D printers, CNC machines, OctoPrint, and maker equipment
- Network test bench - Isolated WLAN for testing IoT devices, network configurations, and wireless security

### Professional & technical
- Field research - Deploy in remote locations for scientific equipment, weather stations, or environmental monitoring
- Amateur radio gateway - Digital communications for ham radio operators
- Medical & healthcare monitoring - Wireless connectivity for medical devices and tele-health applications
- Subsea & marine connectivity - Wireless communication with underwater vehicles and maritime equipment

### Education & community
- Classroom network - Portable WiFi for educational environments, including Minecraft servers and collaborative learning
- Community hotspot - Provide internet access in underserved areas or temporary locations
- Public access point - Deploy in cafes, gathering places, or community centers with [captive portal](/features-insiders/captive.md) support

For more inspiration, check out just some of the ways RaspAP has been used [by our awesome community](https://github.com/RaspAP/raspap-awesome). 

## Next steps

Ready to get started? Head over to:

- [Simple setup guide](../get-started/simple-setup.md)
- [Repeater setup mode](../features-core/repeater.md)
- [AP Basics](../features-core/ap-basics.md)

Want to learn more? Explore RaspAP's features:

- [Core features](../features-core/index.md)
- [Experimental features](../features-experimental/index.md)
- [Insiders features](../features-insiders/index.md)

## Discussions

Questions or comments about use cases? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).
