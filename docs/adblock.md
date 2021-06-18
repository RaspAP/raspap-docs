# Ad blocking

RaspAP is introducing a new feature to block DNS requests for ads, trackers and other undesirable hosts.

In the best of times, ads are usually just annoying. When access to online services is hampered by requests for ads, the best tool in our arsenal is DNS blacklisting. RaspAP already uses `dnsmasq` to manage both DHCP and DNS, so implementing ad blocking was fairly straightforward.

## Enabling DNS blacklisting
As a beta feature, we invite testing and encourage feedback from users of RaspAP. To enable ad blocking with DNS blacklists, simply respond with 'Y' or press [Enter] when prompted by the installer:

```
Install ad blocking and enable list management? [Y/n]
```

The installer will download the blocklists, configure RaspAP to use them and enable the **Ad blocking** management page.

![Ad block install option](https://i.imgur.com/vzbQKnC.gif){: style="width:450px"}

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


