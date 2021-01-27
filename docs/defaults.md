# Default settings

## Overview

Creating a software routed access point (AP) requires the installation and setup of several Linux services. While this project handles every facet of this process for you, it's still
recommended that users of RaspAP familiarize themselves with the [steps involved](https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md).

RaspAP uses a "known-good" default configuration as a starting point. This facilitates a faster setup by not prompting the user for various network 
settings during the installation. More importantly, it eliminates guesswork that can lead to conflicts down the road. When the [manual](/manual/) or [quick installation](/quick/) is completed,
the user will have a functional AP that they can then administer with RaspAP's web interface.

## Managing config values

The interface itself, default Linux file paths and so on may be changed by modifying the project's configuration file `config.php`. 

> :information_source: **Note:** The file `config/config.php` is copied during the installation to `includes/config.php` and ignored by Git. This way, users can modify `includes/config.php`
without upgrades or `git pull` complaining about local changes. The file `includes/defaults.php` loads corresponding default values if they are not set.

For example, RaspAP's interface may be customized simply by changing the following values:

```
// Optional services, set to true to enable.
define('RASPI_WIFICLIENT_ENABLED', true);
define('RASPI_HOTSPOT_ENABLED', true);
define('RASPI_NETWORK_ENABLED', true);
define('RASPI_DHCP_ENABLED', true);
define('RASPI_ADBLOCK_ENABLED', false);
define('RASPI_OPENVPN_ENABLED', false);
define('RASPI_TORPROXY_ENABLED', false);
define('RASPI_CONFAUTH_ENABLED', true);
define('RASPI_CHANGETHEME_ENABLED', true);
define('RASPI_VNSTAT_ENABLED', true);
define('RASPI_SYSTEM_ENABLED', true);
define('RASPI_MONITOR_ENABLED', false);
```

The constants defined for Linux configuration file paths are typical and needn't be changed, in most cases. However, you could easily do so simply by modifying this file.

## Networking defaults

Default values for the `dnsmasq` and `dhcpcd` services can be modified as well. The file `config/defaults.json` was introduced with the [version 2.6 release](https://github.com/billz/raspap-webgui/releases/tag/2.6).
This file is copied during the installation to `/etc/raspap/networking/`, so any changes to it must be done here.

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
      "dhcp-range": [ "10.3.141.50,10.3.141.255,255.255.255.0,12h" ]
    },
    "uap0": {
      "dhcp-range": [ "192.168.50.50,192.168.50.150,12h" ]
    }
```

These default settings are defined as fallback values. That is, if a user-defined value is undefined these will be used in their place. 

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

## Restoring settings

If you've modified RaspAP's default configuration and the AP no longer works as expected, the defaults may be restored by simply running the [Quick installer](/quick/) again or by following
the steps described in the [manual installation](/manual/).
  
