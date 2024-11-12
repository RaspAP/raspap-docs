# VPN Providers

![vpn-providers](https://github.com/user-attachments/assets/ab600145-e2af-46da-85c9-d35d5b1df018){: style="width:640px"}

## Overview
:octicons-beaker-24: Experimental 

Several popular VPN providers include a Linux Command Line Interface (CLI) for interacting with their services. As a new beta feature, you may optionally control these VPN services from within RaspAP. In this way, after your preferred CLI is installed on your system you may administer it thereafter by using RaspAP's UI.

## Installation
To configure VPN provider support, respond by pressing ++enter++ to accept the default ++y++ option when prompted by the Quick installer:

```
RaspAP Install: Configure VPN provider support (Beta)
Enable VPN provider client configuration? [Y/n]:
```

Next, select an available VPN provider from the list. For the initial beta, we've identified three of the most popular VPN services that have Debian compatible Linux CLIs. Enter a number corresponding to your desired VPN provider followed by the ++enter++ key.

```
Select an option from the list:
  1) ExpressVPN
  2) Mullvad VPN
  3) NordVPN
  0) None
Choose an option: 3
Configuring support for NordVPN
Adding /usr/bin/nordvpn to raspap.sudoers
Enabling administration option for NordVPN
Adding VPN provider to /etc/raspap/provider.ini
[ ✓ ok ]
```

The installer will configure RaspAP to administer the corresponding Linux CLI. Choosing ++0++ (None) followed by ++enter++ will exit the VPN provider option and continue with the installer.

## Provider CLIs
RaspAP provides a visual interface to interact with your chosen VPN provider's CLI. To facilitate this, you must first install and configure the CLI on your system. Specific steps will depend on your VPN provider; consult the online documentation for your chosen VPN service.

!!! note "Note"
    The RaspAP project has no affiliation whatsoever with the supported VPN providers. Each provider was selected solely based on availability of their Debian compatible CLIs.

NordVPN is demonstrated in the following example. Begin by executing the install script:
```
sh <(curl -sSf https://downloads.nordcdn.com/apps/linux/install.sh)
```

After the installer completes, verify the CLI by checking its version:

```
nordvpn --version
NordVPN Version 3.16.6
```

Next, activate your account.  The `--callback` and `--token` methods are useful for headless setups. The latter is shown below:

```
nordvpn login --token [myToken]
Welcome to NordVPN! You can now connect to VPN by using 'nordvpn connect'.
```

Before establishing a VPN connection with the CLI, add a rule to whitelist port 22. This will prevent the VPN from disrupting access to the shell via SSH:
```
nordvpn whitelist add port 22
Port 22 (UDP|TCP) is allowlisted successfully.
```

Now, execute the following to connect to a recommended VPN server:
```
nordvpn connect
Connecting to France #817 (fr817.nordvpn.com)
You are connected to France #817 (fr817.nordvpn.com)!
```

With these setps completed, you are now ready to begin administering your VPN provider with RaspAP.

## Administer your provider
Continuing from the above example, access your VPN provider's UI page from RaspAP. From the **Settings** page, you can view your account status, connect to a recommended VPN server or choose a specific country from the select list.

Below, RaspAP displays the CLI output when a country is selected from the list followed by **Save settings**:

![](https://github.com/RaspAP/raspap-webgui/assets/229399/ad9f111d-a75b-4f3f-8e6c-f5aaa6ef053e){: style="width:400px"}

On the **Status** tab, information about your installed provider CLI and current connection status are displyed:

![](https://github.com/RaspAP/raspap-webgui/assets/229399/974d89e4-aaf7-464e-b6fd-38d780c1f565){: style="width:400px"}

You may perform the same operations with any of the supported VPN providers.

!!! tip "Tip"
    Many VPN providers have firewalls enabled by default that can disrupt access to your system via SSH. For this reason, it's recommended to perform these basic CLI functions from your terminal before using them with RaspAP. If your SSH session is disrupted, a reboot will usually restore the connection. Consult your VPN provider's documentation for more advice. 

If a configured provider's CLI is not found, RaspAP will detect this and give you a helpful pointer to the CLI's installation instructions:

![](https://github.com/RaspAP/raspap-webgui/assets/229399/6ef30536-0255-4f0d-a234-445dc02953c2){: style="width:400px"}

Likewise, if the CLI binary exists but RaspAP is unable to execute it, a diagnostic message will be displayed.

## Control scope
Each VPN provider's CLI offers different command sets to control various aspects of their service. For this beta release, RaspAP may be used to administer basic functions including connect, disconnect, status, account information and country (or city) selection for the remote VPN server. 

```
nordvpn settings
Technology: NORDLYNX
Firewall: disabled
Firewall Mark: 0xe1f1
Routing: enabled
Analytics: enabled
Kill Switch: disabled
Threat Protection Lite: disabled
Notify: disabled
Auto-connect: disabled
IPv6: disabled
Meshnet: disabled
DNS: disabled
LAN Discovery: disabled
Allowlisted ports:
       22 (UDP|TCP)
```

More advanced CLI settings such as whitelists, kill switches, firewalls, protocols and so on (shown above) should be administered with your CLI directly.

!!! tip "Tip"
    Support for provider CLIs is intended for typical setups with RaspAP's [default configuration](defaults.md), where the AP interface is `wlan0` and internet connectivity is provided by `eth0`. If you need to control settings beyond these defaults with your provider, it's recommended to install either [OpenVPN](openvpn.md) or [WireGuard](wireguard.md) and administer these services directly. 

## Public IP
After a VPN connection is established, your public IPv4 address will be displayed next to a globe icon :fontawesome-solid-earth-americas:{ style="color: var(--md-default-fg-color--light)" } below your provider name on the **Settings** tab. Click or tap on the external link icon :octicons-link-external-16:{ style="color: var(--md-default-fg-color--light)" } to see details about your IP location.

### AP clients
If your device is connected to the internet via Ethernet (`eth0`), clients connected on the AP interface (`wlan0` for example) will have their traffic automatically routed through the VPN connection. 

## Troubleshooting
RaspAP uses each CLI to fetch the most detailed available connection information and display this on the **Status** tab. The level of detail varies from one provider to the next. If you suspect a problem with your VPN service, it's recommended to check this output and use it for troubleshooting purposes with your VPN provider.

## Whitelisting services
Additionally, you might want to consider whitelisting other ports that are commonly used for essential network services. For instance, with NordVPN's CLI you may whitelist TCP port 53 and UDP port 67 with the following commands:

```
nordvpn whitelist add port 53
nordvpn whitelist add port 67
```
This will allow devices connecting to your AP to obtain an IP address.

Next, it's recommended to whitelist your network subnet. For example:

```
nordvpn whitelist add subnet 192.168.x.x/24
```
Substitute the placeholder value for your network. This will permit you to connect to the VPN while also preserving your access to SSH and RaspAP's web UI. Refer to your provider's CLI documentation for more information.

## Discussions
Questions or comments about using VPN providers? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).
