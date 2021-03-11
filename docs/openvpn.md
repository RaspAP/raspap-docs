# OpenVPN

## Overview

OpenVPN may be optionally installed by the [Quick Installer](/quick/). Once this is done, you can create a client configuration and manage the `openvpn-client` service with RaspAP.

## Enabling OpenVPN

To configure an OpenVPN client, upload a valid `.ovpn` file from your provider and, optionally, specify your login credentials. For clarity, these steps are described below:

1. Enter your credentials, if needed, into the **Username** and **Password** fields.
2. Browse to your provider's `.ovpn` file and choose **Save settings**.
3. Confirm that the OpenVPN client.conf uploaded successfully.
4. Choose **Start OpenVPN**.

The video walkthrough below illustrates the steps of configuring an OpenVPN client from start to finish.

<video width="640" height="480" controls>
  <source src="https://user-images.githubusercontent.com/229399/104086753-d6403b00-525a-11eb-9734-ad7e3ddb22bb.mov" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Tunneling traffic

RaspAP will store your client configuration and add firewall rules to forward traffic from OpenVPN’s `tun0` interface to your configured wireless interface.
In the example below, the default AP interface `wlan0` is used: 

```
iptables -A POSTROUTING -o tun0 -j MASQUERADE
iptables -A FORWARD -i tun0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i wlan0 -o tun0 -j ACCEPT
```

## Public IP address

After a page reload, your new public IPv4 address will be indicated. Click or tap the :fontawesome-solid-external-link-alt: icon to open a new window with details about your 
public IP.

## Multiple client configs
:fontawesome-solid-flask: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](/insiders/)

[Insiders](/insiders/) are able to manage multiple OpenVPN configurations. This includes the ability to upload, activate and delete any number of valid `.ovpn` files and
associated login credentials. Thereafter, switching between them is done by simply activating the desired profile. 

![](https://user-images.githubusercontent.com/229399/110756490-8fff5c00-824a-11eb-852b-858759b5dacb.png){: style="width:450px"}

Activating a profile will restart the `openvpn-client` service automatically. Additionally, `openvpn-service` activity may be tracked in the **Logging** tab. 


## Mitigating DNS leaks

Remote hosts use a variety of methods to defeat VPNs, some more aggressively than others. Many VPN providers will advise you to configure custom DNS servers to mitigate DNS leaks,
which you can do from RaspAP's **DHCP > Advanced** tab. You can also test for this with [https://dnsleaktest.com/](https://dnsleaktest.com/).

Other providers have specific VPN nodes to use with popular streaming services. It's recommended to check with your provider and follow their suggestions.

When an OpenVPN client is configured, RaspAP adds NAT rules with `iptables` to forward all packets from the AP interface to `tun0`.
If you suspect network traffic is not being routed through `tun0` (or any other interface) for some reason, you can monitor this directly from your RPi with `iftop`:

```
sudo apt install iftop
sudo iftop -i [interface]
```

## Browser considerations

The Mozilla Foundation recently added a **DNS over HTTPS (DoH)** proprietary service to its Firefox browser. As of this writing, this "feature" is enabled by default for users in the United States.
A consequence of DoH is that DNS requests will be resolved by Mozilla's DNS servers, instead of your VPN provider's. Instructions for disabling this DoH may be found [here](https://support.mozilla.org/en-US/kb/firefox-dns-over-https#w_manually-enabling-and-disabling-dns-over-https).

