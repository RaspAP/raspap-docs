# Ad blocking

![ad-blocking](https://github.com/user-attachments/assets/34e7a67c-2ce4-4e0f-9afd-7403a0f895df){: style="width:640px"}

RaspAP has introduced a new DNS based filter to stop ads, trackers, malware and other undesirable hosts in their tracks. 

In the best of times, ads are usually just annoying. When access to online services served by our AP is hampered by ads, malware and trackers, the best tool in our arsenal is DNS blacklisting.
RaspAP already uses `dnsmasq` to manage both DHCP and DNS, so we have the foundation for a highly effective ad blocking facility.

## Quick installer
To install ad blocking with DNS blacklists, simply respond with ++y++ or press ++enter++ when prompted by the installer:

```
Install ad blocking and enable list management? [Y/n]
```

The installer will download the blocklists, configure RaspAP to use them and enable the **Ad blocking** management page.

![Ad block install option](https://user-images.githubusercontent.com/229399/127268555-5e397b12-a123-4a15-a58f-e339b517ac0a.png){: style="width:540px"}

Ad blocking is enabled and active for clients connected to your AP. You may update the blocklists or disable ad blocking with the management page. These actions are described below. 
 
## Manual installation
Ad blocking may also be installed manually. Refer to the detailed [installation steps](manual.md#ad-blocking).

## Blocklist sources
Blocklists are sourced from multiple, continuously updated open source projects. These are divided into two groups: **hosts** and **domain** blocklists. By default, RaspAP's ad block facility uses [StevenBlack's hosts](https://github.com/StevenBlack/hosts) as the primary hosts blocklist. This repository is a hosts file aggregator that consolidates several reputable hosts files and merges them into a unified, optimized hosts file with duplicates removed.

![StevenBlack's hosts file aggregator](https://raw.githubusercontent.com/StevenBlack/hosts/master/aggregator.png){: style="width:640px"}

Alternatively, users may choose from a number of host blocklist sources maintained by the [badmojr/1Hosts](https://github.com/badmojr/1Hosts) GitHub project. These lists are compiled daily into Mini, Lite, Pro and Xtra versions depending on specific user needs. Refer to the [GitHub project](https://github.com/badmojr/1Hosts) for an explanation of these different blocklists.

In addition to blocking hosts, domain blocking gives us the ability to use wildcards with `dnsmasq` to block an entire domain (for example, `baddomain.org`) with a single rule. This includes all known and unknown subdomains, such as `*.baddomain.org`. Domain blocklists are provided by the [OISD](https://oisd.nl/) project. Similar to hosts lists, these are continuously updated and curated into several lists: Small, Big and NSFW. Refer to the [OISD](https://oisd.nl/) project for an explanation of these lists. 

## Updating lists 
Each of the hosts and domains blocklists are updated daily, so it's a good practice to refresh them periodically. You can do this from the **Ad Blocking** management page in RaspAP. Simply select the list from the dropdown and choose **Update now**. 

![Manage blocklists](https://user-images.githubusercontent.com/229399/224507022-f71e9a8f-ad73-437b-81cd-c59b27ad3dc3.png){: style="width:420px"}

Next to the update button, a gear icon :fontawesome-solid-gear:{ style="color: var(--md-default-fg-color--light)" } will appear to indicate that the selected list is being downloaded. Thereafter, a timestamp after each list will indicate when it was last updated.

!!! note "Note"
    To apply the latest blocklists, be sure to **Restart Ad Blocking**.

### Automatic updates
Alternatively, you may wish to automate the process of keeping the ad block source lists up-to-date. A method to achieve this is described in [this FAQ](faq.md#adblockauto). 

## Custom blocklist
In addition to the notracking blocklists, you may create your own host blocklist by adding entries on the **Custom blocklist** tab. 
Define custom hosts to be blocked by entering an IPv4 or IPv6 address followed by any whitespace (spaces or tabs) and the host name. An IPv4 example would take the form `0.0.0.0 badhost.com`.
Choose **Save settings** and **Restart Ad Blocking**.

!!! note "Note"
    As the name suggests, this is effective at blocking individual hosts, but not entire domains (or subdomains). 


## Enabling logging
By default, DNS logging is disabled. If you'd like to see which hosts are being blocked, enable it on the **DHCP Server > Logging** tab by selecting the **Log DNS queries** toggle. **Save settings** and **Restart Ad Blocking**. The **Logging** tab on the **Ad Blocking** page will display blacklisted DNS queries with host addresses of `0.0.0.0`. A sample of blocked ad/tracker requests is below.

```
dnsmasq[9633]: config static.ads-twitter.com is 0.0.0.0
dnsmasq[9633]: config tag.bounceexchange.com is 0.0.0.0
dnsmasq[9633]: config cdn.boomtrain.com is 0.0.0.0
dnsmasq[9633]: config securepubads.g.doubleclick.net is 0.0.0.0
dnsmasq[9633]: config c.amazon-adsystem.com is 0.0.0.0
dnsmasq[9633]: config pixel.adsafeprotected.com is 0.0.0.0
dnsmasq[9633]: config ad.doubleclick.net is 0.0.0.0
dnsmasq[9633]: config www.summerhamster.com is 0.0.0.0
dnsmasq[9633]: config c2.taboola.com is 0.0.0.0
dnsmasq[9633]: config ads.servebom.com is 0.0.0.0
dnsmasq[9633]: config s.cpx.to is 0.0.0.0
dnsmasq[9633]: config pixel.quantserve.com is 0.0.0.0
dnsmasq[9633]: config cdn.taboola.com is 0.0.0.0
dnsmasq[9633]: config sdk.iad-01.braze.com is 0.0.0.0
```

## Disabling ad block
To disable the ad blocking service, slide the **Enable blocklists** toggle to its off position, then choose **Save settings**. You may then restart your hotspot for the changes to take effect.

## About blocklist policies
The blocklist sources chosen for RaspAP adhere to these policies:

- Should not break useful websites or apps
- Blocks tracking servers
- Blocks advertising servers
- Blocks analytics servers
- Blocks scam websites
- Blocks malware servers
- Blocks webminers
- Blocks phishing servers

Users may tailor RaspAP's ad blocking to suit their needs by selecting from multiple blocklist sources. Furthermore, domain blocklists enable full use of domain name based wildcard filtering (for example, `*.baddomain.org`). This reduces the chance of missing any new subdomains and significantly reduces the size of the blocklists.

## Discussions
Questions or comments about using Ad blocking? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).

