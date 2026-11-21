# Pi-hole integration
![pi-hole](../images/pi-hole.png){: style="width:640px"}

## Overview

[Pi-hole](https://pi-hole.net/) is a popular network-wide ad blocker. Many users have asked to run it on the same device as RaspAP, so that a single Raspberry Pi provides both the access point and the ad blocking for its clients.

Until now this was difficult, because both projects need port `53`. RaspAP uses `dnsmasq` for DHCP and DNS, and Pi-hole's FTL engine is built on `dnsmasq` as well. When both try to start, one of them fails with:

```
failed to create listening socket for port 53: Address in use
```

RaspAP can now turn off its own DNS server while it keeps serving DHCP. Pi-hole then answers DNS on port `53`, and RaspAP gives AP clients the Pi-hole address as their DNS server.

```
AP client ──DHCP──▶ RaspAP (dnsmasq, DHCP only)
          ──DNS───▶ Pi-hole (port 53) ──▶ upstream DNS
```

!!! note "Note"
    This page describes Pi-hole v6. Pi-hole v5 wrote its own files to `/etc/dnsmasq.d`, which conflict with RaspAP's configuration.

## Requirements

* A working RaspAP installation with the **Disable DNS server (DHCP only)** option on the **DHCP Server > Advanced** tab.
* Pi-hole v6, installed _after_ the steps in [Configure RaspAP](#configure-raspap).

## Configure RaspAP

1. Go to **DHCP Server** and select your AP interface, for example `wlan0`.
2. On the **Advanced** tab, enable **Disable DNS server (DHCP only)**. This will automatically set the DNS Server on the **Server settings** tab to the IP address of the AP interface.
3. On the **Server settings** tab, be sure to leave **DNS Server 2** empty, so that clients cannot bypass Pi-hole.

4. Choose **Save settings**, then **Restart dnsmasq**.

!!! warning "Important"
    **DNS Server 1** must be the address of _this device_. The default configuration hands out public DNS servers such as `9.9.9.9` and `1.1.1.1`. With those, clients still have working DNS, but their queries never reach Pi-hole.

    The **Upstream DNS servers** option on the **Advanced** tab has no effect while the DNS server is disabled. Configure upstream servers in Pi-hole instead.

Check that `dnsmasq` no longer listens on port `53`:

```
sudo ss -lunp | grep ':53 '
```

This should return nothing. The `dnsmasq` log at `/var/log/dnsmasq.log` reports `DNS disabled` when it starts.

## Install Pi-hole

Install Pi-hole with its official installer:

```
curl -sSL https://install.pi-hole.net | bash
```

Accept the defaults. You may select any interface in the installer, since Pi-hole's default listening mode answers queries from all directly connected networks, including the AP subnet.

Pi-hole's web server tries ports `80` and `443` by default. RaspAP's `lighttpd` already uses port `80`, so move Pi-hole's web interface to another port:

```
sudo pihole-FTL --config webserver.port 8080
```

The Pi-hole dashboard is then available at `http://10.3.141.1:8080/admin/`, and RaspAP remains at `http://10.3.141.1`.

!!! tip "Tip"
    Alternatively, you may move RaspAP to another port as described in [this FAQ](../faq.md#webport).

## Verify the setup

On the RaspAP device, check that Pi-hole answers on the AP address:

```
dig +short @10.3.141.1 pi-hole.net
```

Then watch the Pi-hole query log while a client connected to the AP browses the web:

```
pihole tail
```

Queries should appear with the client's address from the AP subnet, for example `10.3.141.205`. You can also use the **Query Log** in the Pi-hole dashboard.

## Troubleshooting

### Pi-hole reports "Address in use"
If Pi-hole was started while RaspAP's `dnsmasq` still held port `53`, Pi-hole's DNS server does not start, although its web interface runs. Restart `dnsmasq` first, then Pi-hole:

```
sudo systemctl restart dnsmasq.service
sudo systemctl restart pihole-FTL.service
```

### Clients are not shown in the query log
If only a few queries appear, the client probably sends its DNS queries elsewhere. Common causes are:

* A VPN client on the device, which uses its own DNS server.
* Encrypted DNS in the browser (DNS over HTTPS). Disable it in the browser's privacy or security settings.
* iCloud Private Relay or "Limit IP address tracking" on Apple devices.
* A DHCP lease from before the change. Reconnect the client to the AP to renew it.

On macOS, `scutil --dns | grep nameserver` shows the DNS servers in use. The first entry should be the AP address.

### Settings that must stay at their defaults
* Pi-hole's own DHCP server must remain **disabled**. RaspAP provides DHCP.
* Pi-hole's `misc.etc_dnsmasq_d` option must remain **false** (the default). If it is enabled, Pi-hole loads RaspAP's files from `/etc/dnsmasq.d`, including the option that disables DNS.

## Limitations

* RaspAP's own [ad blocking](../features-core/adblock.md) and DNS query logging use RaspAP's DNS server, so they do not work while it is disabled. Use Pi-hole's blocklists and query log instead.
* The DNS server option applies to all interfaces that RaspAP serves with DHCP. Set **DNS Server 1** for each of them, for example for `uap0` in [AP-STA mode](../features-experimental/ap-sta.md).
