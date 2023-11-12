# Default settings

## Overview

Creating a software routed access point (AP) requires the installation and setup of several related Linux services.
RaspAP uses a known-good default configuration as a starting point. This facilitates a faster setup by not prompting the user for various network 
settings during the installation. More importantly, it eliminates guesswork that can lead to conflicts down the road. When the [manual](manual.md) or [quick installation](quick.md) is completed,
you will have a functional AP that you may then administer with RaspAP's web interface.

While this project handles every facet of this process for you, it's still recommended that users familiarize themselves with the [steps involved](https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-routed-wireless-access-point) in building a software AP from start to finish.

## Configuration directory

To every extent possible, RaspAP's default settings are contained within the project's `/config` folder. The networking defaults, DNS servers, wireless regulatory data and so on are found here.
In this way, the user may modify RaspAP's baseline application settings without touching code.

The exception to this is `hostapd.conf` which is managed by `includes/hostapd.php` and effectively rewritten depending on user input. This is due to the [complexity of this configuration](https://w1.fi/cgit/hostap/plain/hostapd/hostapd.conf)
relative to other services managed by the project. For this reason, manual edits to this file will not be preserved.

Baseline configurations for `dhcpcd`, `dnsmasq` (described below) and bridged AP configurations are contained here.
 

## Managing config values

The interface itself, default Linux file paths and so on may be changed by modifying the project's configuration file `config.php`. 

!!! note "Note"
    The file `config/config.php` is copied during the installation to `includes/config.php` and ignored by Git. This way, users can modify `includes/config.php` without `git pull` or upgrades complaining about local changes. The file `includes/defaults.php` loads corresponding default values if they are not set.

For example, you can change the brand text that appears in the interface header simply by modifying the value of this constant:

```
define('RASPI_BRAND_TEXT', 'RaspAP');
```

RaspAP's interface may be further customized by changing the following values:

```
// Optional services, set to true to enable.
define('RASPI_WIFICLIENT_ENABLED', true);
define('RASPI_HOTSPOT_ENABLED', true);
define('RASPI_NETWORK_ENABLED', true);
define('RASPI_DHCP_ENABLED', true);
define('RASPI_ADBLOCK_ENABLED', false);
define('RASPI_OPENVPN_ENABLED', false);
define('RASPI_WIREGUARD_ENABLED', false);
define('RASPI_TORPROXY_ENABLED', false);
define('RASPI_CONFAUTH_ENABLED', true);
define('RASPI_CHANGETHEME_ENABLED', true);
define('RASPI_VNSTAT_ENABLED', true);
define('RASPI_SYSTEM_ENABLED', true);
define('RASPI_MONITOR_ENABLED', false);
```

The constants defined for Linux configuration file paths are typical and needn't be changed, in most cases. However, you could easily do so simply by modifying this file.

## Networking defaults

The default AP interface used by RaspAP is `wlan0`. This is a typical setting if you are using the RPi's onboard wireless adapter. You can change this to a different interface by modifying
the following value in `config.php`:

```
define('RASPI_WIFI_AP_INTERFACE', 'wlan0');
```

!!! info "Info"
    If a second wireless adapter is configured for your device, for example bound to the `wlan1` interface, RaspAP will automatically detect it and assign it as the default
wireless client interface. You may change this setting simply by selecting `wlan1` as the AP interface in the **Hotspot > Basic** panel. After restarting the hotspot, RaspAP will use `wlan0`
as the client interface.

Default values for the `dnsmasq` and `dhcpcd` services can be modified as well. The file `config/defaults.json` was introduced with the [version 2.6 release](https://github.com/RaspAP/raspap-webgui/releases/tag/2.6).
This file is copied during the installation to `/etc/raspap/networking/`, so any changes to it must be made here.

The `defaults.json` file uses the standard JSON data-interchange format. For example, the default `dhcp` settings for `wlan0` are displayed below:

```
"dhcp": {
    "wlan0": { 
      "static ip_address": [ "10.3.141.1/24" ],
      "static routers": [ "10.3.141.1" ],
      "static domain_name_server": [ "1.1.1.1 8.8.8.8" ],
      "subnetmask": [ "255.255.255.0" ]
    }
```

Likewise, the DHCP ranges for both `wlan0` and the virtual `uap0` interface are shown below:

```
"dnsmasq": {
    "wlan0": {
      "dhcp-range": [ "10.3.141.50,10.3.141.254,255.255.255.0,12h" ]
    },
    "uap0": {
      "dhcp-range": [ "192.168.50.50,192.168.50.150,12h" ]
    }
```

These default settings are defined as fallback values. That is, if a user-defined value is missing these will be used in their place.

## DNS servers

The list of hosted DNS servers available in the **Upstream DNS servers** panel in **DHCP > Advanced** may be modified to suit your needs. The file `config/dns-servers.json` contains
a JSON formatted collection of hostnames and IPv4 addresses, like so:

```
"Google": [
    "8.8.4.4",
    "8.8.8.8"
  ],
  "OpenDNS": [
    "208.67.220.220",
    "208.67.222.222"
  ],
  "Quad9": [
    "9.9.9.9"
  ],
```

Edits to this file in place will immediately be reflected in the user interface.

## VPN providers
RaspAP [version 3.0](https://github.com/RaspAP/raspap-webgui/releases/tag/3.0) introduced beta support for a select number of [VPN providers](providers.md). These services are largely defined in the `config/vpn-providers.json` file. An example provider definiton is shown below:

```
"id": 1,
"name": "ExpressVPN",
"bin_path": "/usr/bin/expressvpn",
"install_page": "https://www.expressvpn.com/support/vpn-setup/app-for-linux/",
"account_page": "https://www.expressvpn.com/subscriptions",
"cmd_overrides": {
   "countries": "list all",
   "log": "diagnostics",
   "version": "-v"
}
```

It is not necessary to modify these definitions, unless you would like to experiment by adding a provider not currently supported by RaspAP.

## Restoring settings

If you've modified RaspAP's default configuration and the AP no longer works as expected, the defaults may be restored by performing a system reset. From the **System > Tools** tab, click or tap the **Perform reset** button. A dialog will appear to confirm this action.

![](https://github.com/RaspAP/raspap-webgui/assets/229399/66bf5cb5-3d77-44aa-92b8-5ebca6f003ad){: style="width:480px"}

Alternatively, you may follow the steps described in the [manual installation](manual.md#default-configuration).

