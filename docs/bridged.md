# Bridged AP mode

## Overview

By default RaspAP configures a routed AP as its hotspot, where your RPi creates a subnet and assigns IP addresses to its hotspot clients.
If you would rather have your upstream router assign IP addresses, RaspAP lets you change the hotspot configuration to an alternative bridged AP. This is also useful if you want your RPi and its hotspot clients to be visible to other devices in your router's network.

## Toggling bridged AP mode
In the RaspAP web interface, go to **Hotspot** > **Advanced** tab, then slide the **Bridged AP mode** toggle. **Save settings** then **Restart hotspot**.

![](https://user-images.githubusercontent.com/229399/224494216-af49936e-feb3-4932-b987-34505f0f54a7.png){: style="width:420px"}

## Limitations
Bridged AP mode has some limitations compared to RaspAP's default routed AP.

On the **Hotspot** > **Advanced** tab the **Wifi Client AP** mode option is disabled. Your RPi cannot connect as a client to another Wifi network while simultaneously hosting its own bridged AP (hotspot).

The **DHCP Server** page is disabled. The reason for this is in bridged AP mode, your upstream router is the DHCP server. Use your router's web interface to configure DHCP settings.

Clients connected to a bridged AP with **OpenVPN** enabled will not have their traffic routed through the VPN server. Your RPi itself will still have its own traffic routed through the VPN server.

!!!note Note
    Bridged AP mode is not currently supported on Ubuntu Server. 


## Accessing the web interface
In bridged AP mode, you will no longer be able to access RaspAP's web interface using the default 10.3.141.1 address. This is because your RPi no longer creates its own 10.3.141.0/24 subnet for its hotspot. Instead, access RaspAP's web interface by entering your RPi's hostname followed by `.local`. By default this will look like `raspberrypi.local`.

Some browsers have trouble resolving `.local` addresses. You might have to modify the address depending on your browser: `http://raspberrypi.local` or `raspberrypi.local/`.

If the above methods don't work, the `nmap` command (Network Mapper) can be used to scan your subnet for devices connected to your network. For example, invoke `namp` with the `-sn` flag (ping scan) 
on your subnet range:

```
nmap -sn 192.168.1.0/24
```

This scan pings all the IP addresses in a subnet to see if they respond. For each device that responds to the ping, the output will show the hostname and IP address like so:

```
Starting Nmap 7.80 ( https://nmap.org ) at 2021-01-23 10:04 CET
Nmap scan report for iPhone 192.168.1.31
Host is up (0.037s latency).
Nmap scan report for raspberrypi 192.168.1.8
Host is up (0.031s latency).
Nmap scan report for Chromecast 192.168.1.45
Host is up (0.0015s latency).
Nmap scan report for mbp15 192.168.1.48
Host is up (0.074s latency).
Nmap done: 256 IP addresses (4 hosts up) scanned in 6.08 seconds
```

More information on finding your RPi's IP address can be found [here](https://www.raspberrypi.org/documentation/remote-access/ip-address.md).

## Troubleshooting
If you are unable to connect clients to your bridged AP, start by following the recommendations in [this FAQ](/faq/#bridged-ap-mode-is-unstable-or-clients-cant-connect-help).
Client connectivity issues in bridged AP mode are most often the result of your router, not RaspAP. Check your router's web interface and DHCP settings _before_ reporting a bug.

