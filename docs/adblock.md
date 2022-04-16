# Ad blocking

![adblock](https://user-images.githubusercontent.com/229399/163673637-e65c507b-19fa-4e78-8139-098ee8bcad55.png){: style="width:100px"}

RaspAP has introduced a new DNS based filter to stop ads, trackers and other undesirable hosts in their tracks. 

In the best of times, ads are usually just annoying. When access to online services served by our AP is hampered by ads, malware and trackers, the best tool in our arsenal is DNS blacklisting.
RaspAP already uses `dnsmasq` to manage both DHCP and DNS, so we have the foundation for a highly effective ad blocking facility.

## Quick installer
As a beta feature, we invite testing and encourage feedback from users of RaspAP. To install ad blocking with DNS blacklists, simply respond with 'Y' or press [Enter] when prompted by the installer:

```
Install ad blocking and enable list management? [Y/n]
```

The installer will download the blocklists, configure RaspAP to use them and enable the **Ad blocking** management page.

![Ad block install option](https://user-images.githubusercontent.com/229399/127268555-5e397b12-a123-4a15-a58f-e339b517ac0a.png){: style="width:500px"}

Ad blocking is enabled and active for clients connected to your AP. You may update the blocklists or disable ad blocking with the management page. These actions are described below. 
 
## Manual installation
Ad blocking may also be installed manually. Refer to the detailed [installation steps](manual.md#ad-blocking).

## Blocklist source
For the public beta release, blocklists are sourced from the [notracking project](https://github.com/notracking/hosts-blocklists) on GitHub. This "list of lists" is gathered from multiple, actively maintained sources and automatically updated, cleaned, optimized and moderated on a daily basis. A complete list of sources is available [here](https://github.com/notracking/hosts-blocklists/blob/master/SOURCES.md).

## Updating lists 
The notracking project maintains two blocklists; hostnames and domains. These are updated daily, so it's a good practice to refresh them periodically. You can do this from the **Ad Blocking** management page in RaspAP. Simply select the list from the dropdown and choose **Update now**. 

![Manage blocklists](https://i.imgur.com/7enu97T.png){: style="width:550px"}

> :information_source: **Note:** to apply the latest blocklists, be sure to **Restart Ad Blocking**.

## Custom blocklist
In addition to the notracking blocklists, you may create your own host blocklist by adding entries on the **Custom blocklist** tab. 
Define custom hosts to be blocked by entering an IPv4 or IPv6 address followed by any whitespace (spaces or tabs) and the host name. An IPv4 example would take the form `0.0.0.0 badhost.com`.
Choose **Save settings** and **Restart Ad Blocking**.

> :information_source: **Note:** As the name suggests, this is effective at blocking individual hosts, but not entire domains (or subdomains). 


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
The notracking blocklists chosen for RaspAP adhere to these policies:

- Should not break useful websites or apps
- Blocks tracking servers
- Blocks advertising servers
- Blocks analytics servers
- Blocks scam websites
- Blocks malware servers
- Blocks webminers
- Blocks phishing servers

Furthermore, notracking makes full use of domain name based wildcard filtering (for example, `*.adhost.net`). This reduces the chance of missing any new subdomains and significantly reduces the size of the blocklists.
