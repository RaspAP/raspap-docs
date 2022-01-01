# WireGuard

![](https://i.imgur.com/5YDv37e.png)

## Overview
WireGuard<sup>®</sup> is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be considerably more performant than OpenVPN,
and is generally regarded as the most secure, easiest to use, and simplest VPN solution for modern Linux distributions.

WireGuard may be optionally installed by the [Quick Installer](quick.md). Once this is done, you can manage both local and remote server settings, create a peer configuration and control the `wg-quick` service with RaspAP.

## Securing your wireless network
RaspAP gives you two ways to create a secure WireGuard tunnel: **1)** by uploading a `.conf` file from your VPN provider, or **2)** by creating a manual configuration. Each method is described and demonstrated with a short video below.

### File upload
This method may be used if you are using a commerical WireGuard VPN provider, a self-hosted or other remote WG server. In these cases, it's assumed you have an existing WireGuard `.conf` file and wish
to upload this to RaspAP.

> :information_source: **Note:** The term "server" is used here as a convenience. WireGuard does not make a distinction between client and server roles. Instead, each node is considered a "peer" in a WireGuard network.

To do this, select the **Upload file** option under **Configuration Method**, select a valid WireGuard configuration file and choose **Save settings**. If your `.conf`
file does not contain `iptables` `PostUp` or `PostDown` rules and you wish to route traffic through the active AP interface, select the **Apply iptables rules for AP interface** option before uploading your
configuration file.

> :warning: **Attention:** For security reasons, your WireGuard `.conf` file must have a Linux MIME type of `text/plain`. Windows ignores MIME types, relying instead on extensions. To avoid errors, be sure your file has a `text/plain` 
MIME type embedded in it before uploading.

The complete process of creating a WireGuard configuration with [Mullvad](https://mullvad.net/) and activating it with RaspAP is demonstrated in the video below. 

<video src="https://user-images.githubusercontent.com/229399/128004140-1b006c5a-d758-4cbd-b051-48182c846fbc.mov" data-canonical-src="https://user-images.githubusercontent.com/229399/128004140-1b006c5a-d758-4cbd-b051-48182c846fbc.mov" controls="controls" muted="muted"></video>

It should be noted that RaspAP has no affiliation whatsoever with Mullvad. In fact, Mullvad [does not use affiliates](https://mullvad.net/en/help/policy-reviews-advertising-and-affiliates/) or pay for reviews. 
Members of RaspAP's [Insiders community](/insiders/) have requested support for this VPN provider.

#### Starting WireGuard
RaspAP will handle uploading your `.conf` file and, optionally, applying any `iptables` rules. To enable the tunnel, choose **Start WireGuard**. The WireGuard protocol is extremely fast, so in most cases
your new public IPv4 address will be indicated almost immediately. Click or tap the :fontawesome-solid-external-link-alt: icon to open a new window with details about your public IP.

#### Verifying client connections
If you have chosen to route traffic from the `wg0` interface to the AP interface, you may verify that your clients are secured by the WireGuard VPN. Start by connecting a client to your AP while
WireGuard is enabled. Again, using Mullvad as an example, visit their [connection check](https://mullvad.net/en/check/) page on your client device. If the tunnel is working correctly, you should see
a result like the following: 

![](https://user-images.githubusercontent.com/229399/125700202-5cace3a0-3c54-48ff-8bd4-113a2eef5f1b.png){: style="width:225px"}

If any of the above checks fail, enable WireGuard service logging in RaspAP and check the output. You may also consult your VPN provider's support. 

#### IPv6 considerations
RaspAP currently handles routing of IPv4 traffic only. For this reason, WireGuard server connections and traffic tunneled on IPv6 are incompatible. The solution is to specify IPv4 in your
WireGuard VPN provider's advanced options (Mullvad is shown below): 


![](https://user-images.githubusercontent.com/229399/125697709-d61720a5-fdc6-4d36-8085-563e54d259e1.png){: style="width:375px"}

Alternatively, open your `.conf` file in a text editor and ensure that the `Address` and `AllowedIPs` settings use IPv4 addresses only, like so:

```
[Interface]
PrivateKey = ░░░░░░░░░░░░░░░░░░░░░░░░░
Address = 10.64.171.100/32
DNS = 193.138.218.74

[Peer]
PublicKey = /pS3lXg1jTJ7I58GD/s/4GNL2B0U8JNbjbH9Ddh0myw=
AllowedIPs = 0.0.0.0/0
Endpoint = 185.254.75.3:51820
```

When this is done, you are ready to upload your configuration to RaspAP. 

### Manual configuration
Alternatively, RaspAP gives you full control over creating a manual WireGuard configuration. This method is useful if you wish to secure your local wireless network&#151;that is, between your
device running RaspAP and the clients connected to it.

WireGuard requires a public and private keypair for each device you wish to have access to the VPN tunnel. RaspAP simplifies this process with a
magic button :fontawesome-solid-magic: associated with each public key input field. Simply click or tap this button to securely generate a cryptographic keypair for both the server and peer.

Several [default values](defaults.md) are provided for you as a starting point. These are intended to get a VPN tunnel up and running quickly. They may be modified to suit your needs.

After the keypairs are generated, simply choose **Save settings** followed by **Start WireGuard**.

The video walkthrough below illustrates the steps of configuring a WireGuard tunnel from start to finish.

<video width="640" height="480" controls>
  <source src="https://user-images.githubusercontent.com/229399/110525356-c89d1980-8114-11eb-81f5-8cb5558cb664.mov" type="video/mp4">
  Your browser does not support the video tag.
</video>

Due to WireGuard’s design, both computers on either end of the VPN tunnel will need to have each other's public key. This is discussed below.

> :information_source: **Note:** For security reasons, the local (server) private key is not displayed in the UI. The peer private key is encoded in the QR code and available to download in the `client.conf` file.

If you wish to regenerate local or peer keypairs (or both), simply tap or click the magic button :fontawesome-solid-magic: and choose **Save settings**. Alternatively, to 
remove a server or peer configuration entirely, disable the desired toggle and **Save settings**. This will delete the public/private keypair and the associated configuration.

#### Peer configuration
RaspAP processes the values in the WireGuard **Settings** and **Peer** tabs and creates two configurations for you: `wg0.conf` and `client.conf`.
The former is used to configure the local (server) side of the VPN tunnel. The latter peer configuration is generated as a QR code on the **Peer** tab. Clients such as mobile devices
may scan the QR code to transfer `client.conf` and import it into an associated WireGuard client application.

> :information_source: **Note:** For this experimental release, a single peer configuration may be created. The ability to manage multiple peer configurations is on the project roadmap.

Your peer will need to have WireGuard installed as well. For installing WireGuard on other systems, please see Wireguard's [website](https://www.wireguard.com/install/).

## Tunneling traffic
RaspAP uses WireGuard's `PostUp` and `PostDown` firewall rules to forward traffic from the `wg0` interface to your configured wireless interface.
In the example below, the default AP interface `wlan0` is used: 

```
iptables -A FORWARD -i wlan0 -o wg0 -j ACCEPT
iptables -A FORWARD -i wg0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -t nat -A  POSTROUTING -o wg0 -j MASQUERADE
```

These `iptables` rules are defined in WireGuard's [default settings](defaults.md) and may be modified if you wish.

> :information_source: **Note:** If your VPN server is behind a NAT, you will need to open a UDP port of your choosing (51820 is the default). 

## Low overhead
Due to its low overhead compared with OpenVPN, WireGuard is well-suited for applications where battery longevity is a concern. As [described by its developer](https://www.wireguard.com/quickstart/#nat-and-firewall-traversal-persistence),
WireGuard isn't a chatty protocol. For the most part, it only transmits data when a peer wishes to send packets. When it's not being asked to send packets, it stops sending packets until it is asked again.

As a result, your wireless adapter has a higher likelihood of being able to idle down, which leads to better battery life.

## Troubleshooting
See the [FAQ section](/faq/#wireguard) for WireGuard.
