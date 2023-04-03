# Firewall

![](https://user-images.githubusercontent.com/229399/229590714-32a916b7-0c72-4080-8d32-3d6dff064499.jpg){: style="width:640px"}

## Overview
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

If your device is exposed to the outside world, firewall rules can provide a layer of security against intruders to your network. A firewall also gives us granularity in terms of what is allowed to be forwarded across interfaces. Using the rule sets described below, we can effectively control which packets
are allowed to be inputted to, and outputted from, the RaspAP router itself. 

[Insiders](insiders.md) have access to a UI designed for this purpose. 

## Basic rule set
As with every other aspect of RaspAP's [default settings](defaults.md), the application `iptables` rules are stored in an external JSON file, so they may be modified without touching code. 
During the install, the file `iptables_rules.json` is copied from `/config` to `/etc/raspap/networking/firewall`. Thereafter, they may be administered from the UI, shown below.

![](https://user-images.githubusercontent.com/229399/224494422-f9c14384-18b9-4bd2-8058-2c810e9876e2.png){: style="width:420px"}

By default, the firewall will only allow outgoing and already established traffic. There are no restrictions to the currently configured AP interface (`wlan0` is the default).
The remaining firewall rules are grouped into four distinct classes. These are described below.

### Pre-rules
These rules define pre- and post-routing network address translation (NAT) policies, allow ping requests (IPv4 and IPv6), the loopback device, NTP requests via UDP and DNS requests via TCP and UDP.   

### Main rules
Main rules cover many functions, including allowing unrestricted traffic over the AP interface, rules for client interfaces including the tunnel device (`tun0` for OpenVPN) and
WireGuard (`wg0`, for example). RaspAP will check for the presence of an active OpenVPN or WireGuard connection and automatically apply these rules. 

### Exception rules
These types of rules include service exceptions, such as allowing `ssh` access on port 22 and `http` or `https` on ports 80 and 443, respectively. In addition, user-defined exception rules may be added
to allow incoming or outgoing traffic from specific IP addresses or interfaces. These exception values may be entered in the UI, separated by a blank character or comma.

This rule type is required for OpenVPN via UDP and WireGuard. A list of currently active VPN server IP addresses is provided in the firewall UI.

### Restriction rules
By contrast, restriction rules allow the user to block access from specific IP addresses.

## JSON rules syntax
Most entries in `iptables_rules.json` are descriptive and should be straightforward. An optional entry for each set of rules called `dependson` allows for creation of rules that depend on device
names and whether a service is active.

Each dependency refers to an entry in the firewall config file. For example, `ap-device` or `openvpn-enabled`, followed by a type definition (bool, string or list). The `replace` tag defines which
variable in the actual `iptables` rule should be replaced. To illustrate this, the `wireguard` rule set is shown below:

```
"name": "wireguard",
	"comment": "Rules for wireguard device (wg)",
    "ip-version": 4,
    "dependson": [
        { "var": "wireguard-enable", "type": "bool" },
        { "var": "wireguard-serverip", "type": "string", "replace": "$IPADDRESS$" },
        { "var": "client-device", "type": "string", "replace": "$INTERFACE$" }
    ],
    "rules": [
        "-A INPUT -p udp -s $IPADDRESS$ -j ACCEPT",
        "-A FORWARD -i wg+ -j ACCEPT",
        "-t nat -A POSTROUTING -o $INTERFACE$ -j MASQUERADE"
    ]
```

In this way, interdependent firewall rules may be defined and administered by RaspAP. 
