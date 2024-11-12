# Dynamic DNS

![dynamic-dns](https://github.com/user-attachments/assets/ac4fa7b4-a485-4696-9a25-238cd896cdc8){: style="width:640px"}

## Overview
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

Accessing your device from anywhere in your local network is great, but there are times when you might want it to be reachable from remote locations. This is particularly true for projects such as media servers, network attached storage (NAS) and VPNs such as those provided by RaspAP. However, due to the [shortage of IPv4 addresses](https://en.wikipedia.org/wiki/IPv4_address_exhaustion), it's likely that you will receive a new and different external IP address from your ISP each time your router is rebooted.

Some ISPs offer a static external IP address, although often at an additional cost above a basic subscription. This is where using a **Dynamic DNS** (or **DDNS**) service on your home network can be extremely useful. 

## Solution
Dynamic DNS solves this problem by providing a domain name that always points to the current IP address of your device, regardless of how often it changes. With DDNS, the IP assigned to your domain name is automatically updated by a piece of software (known as a _daemon_) running on your device. This means that you can access the server using the same domain name, without having to constantly update settings each time the IP address changes.

The daemon running on your device resolves your external IP address using one of several methods, then reports this to your DDNS provider. There are a number of different providers that offer Dynamics DNS free of charge. If you currently own a custom domain name, chances are your registrar provides DDNS or has a partner to support this.

## Installation
The [Quick installer](quick.md) will give you the option to add the required packages to your system, and enable the configuration page in RaspAP. Simply press ++enter++ at the prompt to accept the default "Y" (yes) response:

```
Install ddclient and enable DDNS configuration? [Y/n]:
```

When the installer completes, you will be able to administer the `ddclient` service as described in the sections below.

## Basic settings
All the configuration settings needed to enable Dynamic DNS on your device are available on the **Basic settings** tab. These are described in the next section.

### Service provider
RaspAP makes use of the proven **[ddclient](https://github.com/ddclient/ddclient)** open source software for Linux to update dynamic DNS entries. The `ddclient` software is highly configurable and provides a daemon that updates your external IP at scheduled intervals. Many popular [Dynamic DNS services](https://github.com/ddclient/ddclient#supported-services) are supported by `ddclient` and RaspAP. 

Instructions on how to setup your domain for DDNS vary by provider, but the process is generally similar. Begin by selecting a **Service provider** from the dropdown. RaspAP will assist you by automatically populating the **Protocol** and **Server** fields. You may also manually configure the details for your service if so desired.

![](https://user-images.githubusercontent.com/229399/234258065-cc75df63-5e39-4cfd-ba1b-ed533b3982d6.png){: style="width:520px"}

!!! note "Note"
    Some DDNS providers, such as NoIP, distribute their own Linux client to use with their service. It isn't necessary to install this software because the `ddclient` daemon already includes this functionality.

### Method to obtain IP
There are a variety of different methods to determine your external IP address. A popular one involves a discovery page on the web that resolves your IP. If you choose this method, enter it in the **Web address** field after selecting this option from the **Method to obtain IP** select.

!!! tip "Tip"
    There are many freely available external IP discovery pages you can use. Examples include [ChangeIP](http://ip.changeip.com/) and this one from [Namecheap](https://dynamicdns.park-your-domain.com/getip). Each of these pages perform the same basic function.

Alternatively, you may want to use an IP address from a network interface, your router's firewall status page, or an external command. Each of these options can be specified, thereby giving you a great deal of flexibility.  

### Login and domain
Enter your DDNS service credentials in the **Username** and **Password** fields. Finally, specify the **Domain** to be updated that will be associated with your device. DDNS providers may also refer to this as a "zone" or "host". These definitions may take several forms, for example:

```
myhost.dyndns.org
mydomain.com
@.mydomain.com
```

Check with your DDNS service provider to determine which entry is best for your configuration. To complete your setup, choose **Save settings** now or proceed with advanced options.

## Advanced settings
A subset of advanced options are provided for your configuration. These are not required for the DDNS service to be functional, but may be adjusted to suit your needs.

![](https://user-images.githubusercontent.com/229399/234574539-da424b27-4489-40bf-88e7-0e42988bce8a.png){: style="width:520px"}

### Enable SSL
You may wish to **Enable SSL** to ensure that your credentials are not sent over the internet unencrypted. Not all providers support this, however, so this option is disabled by default. Enabling this option for a non-SSL supported provider may result in a connection timeout. Errors such as these [have been reported](https://github.com/ddclient/ddclient/issues/309): 

```
WARNING:  cannot connect to checkip.dyndns.org:443 socket: Connection timed out SSL connect attempt failed
WARNING:  found neither IPv4 nor IPv6 address
DEBUG:    get_ip: using web, http://checkip.dyndns.org/ reports <undefined>
WARNING:  unable to determine IP address
```

For this reason, it's recommended to check with your DDNS service provider before enabling this.

### Daemon check interval
Finally, you may define the **Daemon check interval** to control the length of time between updates performed by `ddclient` in the background. This value is specified in milliseconds and defaults to 300.

When you've completed your configuration, choose **Save settings** and **Start Dynamic DNS**.

## Troubleshooting
Behind the scenes, the `ddclient` daemon will determine your external IP using the method you've defined and send this to your DDNS provider. Your provider will then update the IP address corresponding to the DNS "A" (or "address") record for your domain.

If your DDNS provider fails to report your current IP address, or you suspect there might be a problem with the `ddclient` configuration on your device, you may generate a detailed debug log.

From the **Logging** tab, use the **Generate log** button to invoke the `ddclient` daemon and output a troubleshooting log: 

![](https://user-images.githubusercontent.com/229399/234276204-5d3e2640-7166-47ec-ac3c-6a4034be8060.png){: style="width:520px"}

This will provide a verbose output of everything `ddclient` is doing. If it ends with a `SUCCESS` message this indicates that the daemon successfully checked and updated the DNS "A" record with your provider, if neccessary. An example of this is shown below: 

```
RECEIVE:  140.82.121.3
DEBUG:    get_ip: using web
 dynamicdns.park-your-domain.com/getip reports 140.82.121.3
SUCCESS:  @.mydomain.com: skipped: IP address was already set to 140.82.121.3.
```

If the daemon doesn’t reply with `SUCCESS`, the debug output should give you some clues as to what the problem is.

## Port forwarding
If `ddclient` has successfully updated your DDNS provider's "A" record with your IP address, but you are unable to access your device remotely, it's likely your router needs to be configured for **port forwarding**. This instructs the router to send, or forward, data packets from the external WAN interface to the internal IP address belonging to your device.

You can enable this by using your router's port mapping/forwarding setup. This procedure allows remote computers to connect to a specific device within your internal LAN's private address space. Specifics are highly dependent on the router you have, although the steps are generally straightforward. Consult your router's documentation for details.

## Demilitarized zone
An alternative to forwarding specific ports to an internal IP is using a **demilitarized zone** (DMZ). A home router DMZ is a host on an internal network that has all UDP and TCP ports open and exposed, except those ports otherwise forwarded. By using this method, all the ports (and services) of your device will be directly accessible from the internet, with the attendant security risks that this implies.

This setup is often desirable when a host is running multiple public-facing services that need to be accessed over the internet. In this context, a DMZ provides greater isolation and granular control than is possible with port forwarding. It's also possible to configure different security policies for various DMZ segments. For these reasons, a properly configured DMZ can be a _more secure_ way to expose services to the internet than port forwarding. 

The specifics of creating a DMZ are beyond the scope of this document, although at minimum a [firewall](firewall.md) is strongly advised. 

## Discussions
Questions or comments about using Dynamic DNS? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).
