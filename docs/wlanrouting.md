# Wireless LAN routing

![wlan-routing](https://github.com/RaspAP/raspap-webgui/assets/229399/2553804b-f147-49b6-b471-4a2724810452){: style="width:640px"}


## Overview
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

RaspAP is often used to share internet from an Ethernet connection or other [network device](net-devices.md) through a wireless access point (AP), or act as a [wireless repeater](repeater.md). However, in certain scenarios, it can be extremely useful to share internet from a wireless LAN (WLAN) with clients connected via an Ethernet or USB-Ethernet connection. Many RaspAP users have requested this functionality, so an easy-to-use solution was developed to fulfill this need.

## Solution
To create this setup, the target interface must be configured with a static IP address and have DHCP enabled. This is similar to how RaspAP's [default wireless access point](defaults.md#networking-defaults) is configured. To simplify this process, RaspAP uses predefined subnets for the `eth0` and predictable `enx` interfaces. The relevant portions of this configuration are shown below:

```
"dhcp": {
    ...
    "eth0": {
      "static ip_address": [ "192.168.55.1/24" ],
      "static routers": [ "192.168.55.1" ],
      "static domain_name_server": [ "1.1.1.1 8.8.8.8" ],
      "subnetmask": [ "255.255.255.0" ]
    },
    "enx": {
      "static ip_address": [ "192.168.60.1/24" ],
      "static routers": [ "192.168.60.1" ],
      "static domain_name_server": [ "1.1.1.1 8.8.8.8" ],
      "subnetmask": [ "255.255.255.0" ]
    }
```

```
"dnsmasq": {
    ...
    "eth0": {
      "dhcp-range": [ "192.168.55.50,192.168.55.150,12h" ]
    },
    "enx": {
      "dhcp-range": [ "192.168.60.50,192.168.60.150,12h" ]
    }
  }
```

These default settings are applied automatically, however you may modify them as you wish from the **DHCP Server** administration page.

In addition to these settings, Network Address Translation (NAT) rules must be applied to enable packet routing between the desired interfaces. These `iptables` rules also need to be added when the connection is active, and removed when the connection is deactivated. This is roughly analogous to how WireGuard's [PostUp and PostDown rules](wireguard.md#tunneling-traffic) function. 

## Steps to enable WLAN routing

![wlan-routing-diagram](https://github.com/RaspAP/raspap-webgui/assets/229399/aa88a477-3a78-43e3-ae70-b6de99414452){: style="width:640px"}


### Configure wireless client
To create this configuration, begin by configuring your device as a wireless client, or station, with RaspAP's **WiFi client** page or by preconfiguring your OS for wireless LAN operation. Optionally, connect an external wireless adapter to an available USB port.

### Check wireless connectivity
Ensure that you have a stable wireless connection to your router. The **Wireless Client** widget on RaspAP's dashboard will indicate its status and link quality. 
![wifi-client](https://github.com/RaspAP/raspap-webgui/assets/229399/9b60a72e-1199-4b26-a080-4e10ec3d0cca){: style="width:460px; padding-left:10px; padding-top:10px"}

### Attach Ethernet or USB-Ethernet adapter
Next, attach an Ethernet cable or a USB-Ethernet adapter to an available port, and connect a device you wish to provide internet connectivity to. This could be a laptop, hub or other Ethernet-capable network device. This device will typically be assigned a network interface name by the operating system, such as `eth0` or `eth1`. If your system is configured to use [predictable interface names](https://wiki.debian.org/NetworkInterfaceNames), it may incorporate the interfaces's MAC address (for example, `enx78e7d1ea46da`).

Verify your attached device by checking the output on RaspAP's **Networking > Summary** tab.
!!! tip "Tip"
    ![adapter](https://github.com/RaspAP/raspap-webgui/assets/229399/7fa8ea1a-c10f-4c91-99c3-998b3a177b58){ align=left style="width:200px; padding-left:30px; padding-top:0px"} Many USB-Ethernet adapters are available at low cost. If you choose this option, buy one from a reputable brand. When in doubt, verify your adapter by testing it with a laptop or other device. Note that a regular USB cable, rather than a USB-Ethernet adapter, is not designed for direct Ethernet communication.

### Configure RaspAP's settings
Now, from RaspAP's **Networking > WLAN Routing** tab, choose your wireless client interface and output interface (typically, `eth0` or `enx`). Select the "Configure a static IP address and DHCP for output interface" option toggle, choose **Save settings**  and lastly **Start WLAN routing**.

![wlan-routing](https://github.com/RaspAP/raspap-webgui/assets/229399/f721a4bc-0aad-400e-aec1-ef10ce2a12a5){: style="width:520px; padding-left:0px; padding-bottom:10px; padding-top:10px"}

A system configured with predictable interface names is shown, above.

!!! note "Note"
    If a wireless client connection is not detected on your system, it will be indicated as "not configured" in the interface. The **Start WLAN routing** button will also be disabled until an active wireless client connection is present. 

### Check ethernet connectivity
Finally, confirm internet connectivity on your Ethernet-equipped client device. Optionally, you may wish to perform a [speed test](speedtest.md). If you want to stop wireless LAN routing, simply choose **Stop WLAN routing**. The `iptables` NAT rules added by RaspAP will be removed from your system. The associated DHCP and `dnsmasq` configurations will be removed as well.

!!! tip "Tip"
    RaspAP's default subnets are added for convenience. If you wish to create a custom configuration for your clients, you may do so from the **DHCP Server** page. Be sure to **Save settings** and restart `dsnmasq` to apply your changes. If your interface is named something other than `eth0` or `enx` you must create your own DHCP configuration.

### Troubleshooting
If clients do not have internet connectivity, ensure that the attached Ethernet device appears on the **Networking > Summary** tab. Faulty Ethernet cables and USB-Ethernet adapters are common culprits.

Be sure that you've selected the option to configure a static IP address and DHCP for the output interface on the **Networking > WLAN Routing** tab. If you've configured your own subnet for this purpose, ensure that the settings are correct on the **DHCP server** page and that the `dnsmasq` service was restarted after saving them.

Finally, while wireless LAN routing is active, you may confirm that the `iptables` NAT rules are active by executing the following:

```
sudo iptables -t nat -L -v
```

This should output the `POSTROUTING`, `MASQUERADE` and `FORWARD` rules for the interfaces you've selected. If not, confirm that this option is active on the **Networking > WLAN Routing** tab, then choose **Restart WLAN routing**.

## Discussions
Questions or comments about using wireless LAN routing? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).



