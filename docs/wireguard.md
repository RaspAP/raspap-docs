# WireGuard

## Overview
:fontawesome-solid-flask: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](/insiders/)

WireGuard<sup>®</sup> is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be considerably more performant than OpenVPN,
and is generally regarded as the most secure, easiest to use, and simplest VPN solution for modern Linux distributions.

WireGuard may be optionally installed by the [Quick Installer](/quick/). Once this is done, you can manage local (server) settings, create a peer configuration and control the `wg-quick` service with RaspAP.

## Creating a WireGuard tunnel

WireGuard requires a public and private keypair for each device you wish to have access to the VPN tunnel. RaspAP simplifies this process with a
magic button :fontawesome-solid-magic: associated with each public key input field. Simply click or tap this button to securely generate a cryptographic keypair for both the server and peer.

Several [default values](/defaults/) are provided for you as a starting point. These are intended to get a VPN tunnel up and running quickly. They may be modified to suit your needs.

After the keypairs are generated, simply choose **Save settings** followed by **Start WireGuard**.

The video walkthrough below illustrates the steps of configuring a WireGuard tunnel from start to finish.

<video width="640" height="480" controls>
  <source src="https://user-images.githubusercontent.com/229399/110251359-63182400-7f80-11eb-98d0-2055a38fccbc.mov" type="video/mp4">
  Your browser does not support the video tag.
</video>

Due to WireGuard’s design, both computers on either end of the VPN tunnel will need to have each other's public key. This is discussed below.

> :information_source: **Note:** For security reasons, the local (server) private key is not displayed in the UI. The peer private key is encoded in the QR code and available to download in the `client.conf` file.
If you wish to regenerate local or peer keypairs (or both), simply tap or click the magic button :fontawesome-solid-magic: and choose **Save settings**.

## Peer configuration
RaspAP processes the values in the WireGuard **Settings** and **Peer** tabs and creates two configurations for you: `wg0.conf` and `client.conf`.
The former is used to configure the local (server) side of the VPN tunnel. The latter peer configuration is generated as a QR code on the **Peer** tab. Clients such as mobile devices
may scan the QR code to transfer `client.conf` and import it into an associated WireGuard client application.

> :information_source: **Note:** For this experimental release, a single peer configuration may be created. The ability to manage multiple peer configurations is on the project roadmap.

Your peer will need to have WireGuard installed as well. For installing WireGuard on other systems, please see Wireguard's [website](https://www.wireguard.com/install/).

## Tunneling traffic
RaspAP uses WireGuard's `PostUp` and `PostDown` firewall rules to forward traffic from the `wg0` interface to your configured wireless interface.
In the example below, the default AP interface `wlan0` is used: 

```
iptables -A POSTROUTING -o tun0 -j MASQUERADE
iptables -A FORWARD -i wg0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -t nat -D  POSTROUTING -o wg0 -j MASQUERADE
```

These `iptables` rules are defined in WireGuard's [default settings](/defaults/) and may be modified if you wish.

> :information_source: **Note:** If your VPN server is behind a NAT, you will need to open a UDP port of your choosing (51820 is the default). 

## Low overhead
Due to its low overhead compared with OpenVPN, WireGuard is well-suited for applications where battery longevity is a concern. As [described by its developer](https://www.wireguard.com/quickstart/#nat-and-firewall-traversal-persistence),
WireGuard isn't a chatty protocol. For the most part, it only transmits data when a peer wishes to send packets. When it's not being asked to send packets, it stops sending packets until it is asked again.

As a result, your wireless adapter has a higher likelihood of being able to idle down, which leads to better battery life.

