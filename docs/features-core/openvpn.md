# OpenVPN

![openvpn](https://github.com/user-attachments/assets/23e6eb70-5fab-4d71-b6d6-1f08238dfb22){: style="width:640px"}

## Overview
OpenVPN may be optionally installed by the [Quick Installer](../get-started/quick-installer.md). Once this is done, you can create a client configuration and manage the `openvpn-client` service with RaspAP.

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

After a page reload, your new public IPv4 address will be indicated. Click or tap the :octicons-link-external-16: icon to open a new window with details about your 
public IP.

## Multiple client configs

RaspAP lets you manage multiple OpenVPN client configurations. This includes the ability to upload, activate and delete any number of valid `.ovpn` files and
associated login credentials. Thereafter, switching between them is done by simply activating the desired profile. Traffic is automatically routed to clients connected on the AP interface. 

![](https://user-images.githubusercontent.com/229399/147851803-ba8747f0-9c73-43ae-97ea-99be23b98861.png){: style="width:450px"}

Activating a profile will restart the `openvpn-client` service automatically. Additionally, `openvpn-service` activity may be tracked in the **Logging** tab. 

## Certificate authentication

Alternatively, you may also authenticate with a signing **certification authority (CA) certificate**. This is an alternative to the default username and password authentication, and is
often used with a private or self-hosted OpenVPN server.
 
![](https://user-images.githubusercontent.com/229399/113760359-68e75d80-9716-11eb-82ea-5ed1307e8496.png){: style="width:450px"}

To use this method, upload an OpenVPN configuration file (.ovpn) with the certificate authority (CA) certficate, client certificate and client private key enclosed in tags as described above.

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

## Troubleshooting
See the [FAQ section](../faq.md#openvpn) for OpenVPN.

## Discussions
Questions or comments about using OpenVPN? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).
