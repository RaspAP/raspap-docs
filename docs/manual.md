# Manual installation

## Overview
These steps apply to the [latest release of RaspAP](https://github.com/RaspAP/raspap-webgui/releases/), [Raspberry Pi OS Lite](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit), Debian and Armbian. Notes for previous versions, Ubuntu Server 18.04 TLS and 19.10 are provided, where applicable.
Please refer to [this](/#compatible-operating-systems) regarding operating systems support.

## Prerequisites

Start off by updating your system's package list, then upgrade the kernel, firmware and installed packages to their latest versions:

```
sudo apt-get update
sudo apt-get full-upgrade
```

Note that `full-upgrade` is used rather than a simple `upgrade`, as this also picks up any dependency changes that may have been made.
The kernel and firmware are installed as a Debian package, and so will also get updates when using the procedure above.
These packages are updated infrequently and after extensive testing.

## Enable wireless operation
Telecommunications radio bands are subject to [regulatory restrictions](/faq/#80211ac) to ensure interference-free operation. The Linux OS complies with these rules by requiring users
to configure a two-letter "WiFi country code". In RPi OS, 5 GHz wireless networking is disabled until this country code has been set, usually as part of the initial installation process.
If you have not set your country code or are unsure, check the "WLAN Country" setting in raspi-config's **Localisation Options**: 

```
sudo raspi-config
```

To ensure the WiFi radio is not blocked on the Raspberry Pi, execute the following command:

```
sudo rfkill unblock wlan
```

## Non-RPi OS dependencies
Operating systems other than RPi OS have some additional dependencies. If you are using RPi OS Lite, skip this section. On Ubuntu Server, add a dependency and the `ppa:ondrej/php` apt package:

```
sudo apt-get install software-properties-common 
sudo add-apt-repository ppa:ondrej/php
```

On Debian, Armbian and Ubuntu, install `dhcpcd5` with the following:

```
sudo apt-get install dhcpcd5
```

## Install packages
Install git, lighttpd, php7, hostapd, dnsmasq and some extra packages with the following:

```
sudo apt-get install lighttpd git hostapd dnsmasq iptables-persistent vnstat qrencode php7.3-cgi
```
> :information_source: **Note:** for Ubuntu, you may replace `php7.3-cgi` with `php7.4-cgi`. `php5` is no longer supported.

## Enable PHP
Next, enable PHP for `lighttpd` and restart the service for the settings to take effect:
```
sudo lighttpd-enable-mod fastcgi-php    
sudo service lighttpd force-reload
sudo systemctl restart lighttpd.service
```

## Create the web application
In these steps we will prepare the web destination and git clone the files to `/var/www/html`.

> :information_source:  **Caution:** If this is _not_ a clean installation, be sure you do not have existing files or directories in the web root before executing the `rm -rf` command.

```
sudo rm -rf /var/www/html
sudo git clone https://github.com/RaspAP/raspap-webgui /var/www/html
```

Now comes the fun part. For security reasons, the `www-data` user which `lighttpd` runs under is not allowed to start or stop daemons, or run commands like `ip link`,
all of which we want our app to do. So we will add the `www-data` user to sudoers, but with restrictions on what commands the user can run. Copy the sudoers rules to their destination:

```
cd /var/www/html
sudo cp installers/raspap.sudoers /etc/sudoers.d/090_raspap
```

## Configuration directories
RaspAP uses several directories to manage its own configuration. Create these with the following commands:

```
sudo mkdir /etc/raspap/
sudo mkdir /etc/raspap/backups
sudo mkdir /etc/raspap/networking
sudo mkdir /etc/raspap/hostapd
sudo mkdir /etc/raspap/lighttpd
```

Move RaspAP's auth control file to the configuration directory you created above:

```
sudo cp raspap.php /etc/raspap 
```

## Set permissions
Next, set the files ownership to the `www-data` user for the web files and RaspAP config:

```
sudo chown -R www-data:www-data /var/www/html
sudo chown -R www-data:www-data /etc/raspap
```

## Control scripts
RaspAP uses several shell scripts to manage various aspects of the application, including `hostapd` logging and `raspapd`, the RaspAP control service. Move these scripts to their destinations with the following:

```
sudo mv installers/*log.sh /etc/raspap/hostapd 
sudo mv installers/service*.sh /etc/raspap/hostapd
```

Set ownership and permissions for the logging and service control scripts:

```
sudo chown -c root:www-data /etc/raspap/hostapd/*.sh 
sudo chmod 750 /etc/raspap/hostapd/*.sh 
```

Copy and set ownership of the `lighttpd` control scripts:
```
sudo cp installers/configport.sh /etc/raspap/lighttpd
sudo chown -c root:www-data /etc/raspap/lighttpd/*.sh
```

Next, move the `raspapd` service file to the correct location and enable it:

```
sudo mv installers/raspapd.service /lib/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable raspapd.service
```

## Default configuration
To facilitate a faster setup, RaspAP uses a "known-good" [default configuration](/defaults/) as a starting point.
Copy the configuration files for `dhcpcd`, `dnsmasq`, `hostapd` and `defaults.json`. Optionally, backup your existing `hostapd.conf`:

```
sudo mv /etc/default/hostapd ~/default_hostapd.old
sudo cp /etc/hostapd/hostapd.conf ~/hostapd.conf.old
sudo cp config/default_hostapd /etc/default/hostapd
sudo cp config/hostapd.conf /etc/hostapd/hostapd.conf
sudo cp config/090_raspap.conf /etc/dnsmasq.d/090_raspap.conf
sudo cp config/090_wlan0.conf /etc/dnsmasq.d/090_wlan0.conf
sudo cp config/dhcpcd.conf /etc/dhcpcd.conf
sudo cp config/config.php /var/www/html/includes/
sudo cp config/defaults.json /etc/raspap/networking/
```

> :information_source: **Note:** If you wish to modify RaspAP's default configuration for `dnsmasq` and `dhcp`, you may do so by changing these files and editing `config/defaults.json`.

Next, disable `systemd-networkd` and copy the bridge configuration with the following:

```
sudo systemctl stop systemd-networkd
sudo systemctl disable systemd-networkd
sudo cp config/raspap-bridge-br0.netdev /etc/systemd/network/raspap-bridge-br0.netdev
sudo cp config/raspap-br0-member-eth0.network /etc/systemd/network/raspap-br0-member-eth0.network 
```

## Optimize PHP
Optionally, you may optimize PHP with the following, replacing `php7.3-cgi` with your installed version:

```
sudo sed -i -E 's/^session\.cookie_httponly\s*=\s*(0|([O|o]ff)|([F|f]alse)|([N|n]o))\s*$/session.cookie_httponly = 1/' /etc/php/7.3/cgi/php.ini
sudo sed -i -E 's/^;?opcache\.enable\s*=\s*(0|([O|o]ff)|([F|f]alse)|([N|n]o))\s*$/opcache.enable = 1/' /etc/php/7.3/cgi/php.ini
sudo phpenmod opcache
```

## Routing and IP masquerading
These steps allow WLAN clients to access computers on the main wired `eth0` network, and from there the internet. 
Begin by enabling IP forwarding with the following commands:

```
echo "net.ipv4.ip_forward=1" | sudo tee /etc/sysctl.d/90_raspap.conf > /dev/null
sudo sysctl -p /etc/sysctl.d/90_raspap.conf
sudo /etc/init.d/procps restart
```

To enable traffic between clients on the WLAN and the internet, we add two `iptables` network address translation (NAT) "masquerade" firewall rules.
Create these rules and persist them with the following:

```
sudo iptables -t nat -A POSTROUTING -j MASQUERADE
sudo iptables -t nat -A POSTROUTING -s 192.168.50.0/24 ! -d 192.168.50.0/24 -j MASQUERADE
sudo iptables-save | sudo tee /etc/iptables/rules.v4
```

## Enable hostapd
The `hostapd` service is disabled by default, as there is no configuration for it after its initial installation. Unmask and enable it with the following:

```
sudo systemctl unmask hostapd.service
sudo systemctl enable hostapd.service
```

## OpenVPN
Optionally, you may install OpenVPN, enabling the option in RaspAP's config and the `openvpn-client` service:

```
sudo apt-get install openvpn
sudo sed -i "s/\('RASPI_OPENVPN_ENABLED', \)false/\1true/g" /var/www/html/includes/config.php
sudo systemctl enable openvpn-client@client
```


Copy the OpenVPN auth control script to its destination, setting ownership and permissions with the following:

```
sudo mkdir /etc/raspap/openvpn/
sudo cp installers/configauth.sh /etc/raspap/openvpn/
sudo chown -c root:www-data /etc/raspap/openvpn/*.sh 
sudo chmod 750 /etc/raspap/openvpn/*.sh
```

## Ad blocking
Optionally, you may install Ad blocking, enabling the option in RaspAP's config. There are several steps involved here, including downloading the blocklists:

```
sudo mkdir /etc/raspap/adblock
wget https://raw.githubusercontent.com/notracking/hosts-blocklists/master/hostnames.txt -O /tmp/hostnames.txt
wget https://raw.githubusercontent.com/notracking/hosts-blocklists/master/domains.txt -O /tmp/domains.txt
sudo cp /tmp/hostnames.txt /etc/raspap/adblock
sudo cp /tmp/domains.txt /etc/raspap/adblock 
sudo cp installers/update_blocklist.sh /etc/raspap/adblock/
sudo chown -c root:www-data /etc/raspap/adblock/*.*
sudo chmod 750 /etc/raspap/adblock/*.sh
sudo touch /etc/dnsmasq.d/090_adblock.conf
echo "conf-file=/etc/raspap/adblock/domains.txt" | sudo tee -a /etc/dnsmasq.d/090_adblock.conf > /dev/null 
echo "addn-hosts=/etc/raspap/adblock/hostnames.txt" | sudo tee -a /etc/dnsmasq.d/090_adblock.conf > /dev/null
sudo sed -i '/dhcp-option=6/d' /etc/dnsmasq.d/090_raspap.conf
sudo sed -i "s/\('RASPI_ADBLOCK_ENABLED', \)false/\1true/g" includes/config.php
```

## Restart
Finally, restart your device and verify that the wireless access point is available:

```
sudo systemctl reboot
```

After your device has restarted, search for wireless networks with your wireless client. The default SSID is `raspi-webgui`. 
The default username is "admin" and the default password is "secret".

> :information_source: **Note:** It is strongly recommended that you change these default login credentials in RaspAP's **Authentication** panel.
APs managed by RaspAP in the wild have been administered by third parties with the default login.

If you have any difficulties with the manual install steps, [start a discussion](https://github.com/RaspAP/raspap-webgui/discussions) and refer to this page.


