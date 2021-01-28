# Manual installation

These steps apply to the [latest release of RaspAP](https://github.com/billz/raspap/releases/), [Raspberry Pi OS Lite](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit), Debian and Armbian. Notes for previous versions, Ubuntu Server 18.04 TLS and 19.10 are provided, where applicable.
Please refer to [this](/#compatible-operating-systems) regarding operating systems support.

Start off by following the [project prerequisites](/#quick-start), updating your kernel, firmware and packages to their latest versions:

```
sudo apt-get update
sudo apt-get dist-upgrade
sudo reboot
```

On Ubuntu Server, add a dependency and the `ppa:ondrej/php` apt package.

```
sudo apt-get install software-properties-common 
sudo add-apt-repository ppa:ondrej/php
```

On Debian, Armbian and Ubuntu, install `dhcpcd5`. **Note:** skip this step if using RPi OS.

```
sudo apt-get install dhcpcd5
```

Install git, lighttpd, php7, hostapd, dnsmasq and some extra packages. **Note:** for Ubuntu, you may replace `php7.3-cgi` with `php7.4-cgi`. For Raspbian Stretch, replace `php7.3-cgi` with `php7.0-cgi`. php5 is no longer supported.

```
sudo apt-get install lighttpd git hostapd dnsmasq iptables-persistent vnstat qrencode php7.3-cgi
```

Enable PHP for lighttpd and restart it for the settings to take effect.
```
sudo lighttpd-enable-mod fastcgi-php    
sudo service lighttpd force-reload
sudo systemctl restart lighttpd.service
```

Prepare the web destination and git clone the files to `/var/www/html`.

> ⚠️  **Caution:** If this is _not_ a clean installation, be sure you do not have existing files or directories in the web root before executing the `rm -rf` command.

```
sudo rm -rf /var/www/html
sudo git clone https://github.com/billz/raspap /var/www/html
```

Now comes the fun part. For security reasons, the `www-data` user which `lighttpd` runs under is not allowed to start or stop daemons, or run commands like `ip link`,
all of which we want RaspAP to do. So we will add the `www-data` user to sudoers, but with restrictions on what commands the user can run. Copy the sudoers rules to their destination:

```
cd /var/www/html
sudo cp installers/raspap.sudoers /etc/sudoers.d/090_raspap
```

Create the RaspAP configuration directories:

```
sudo mkdir /etc/raspap/
sudo mkdir /etc/raspap/backups
sudo mkdir /etc/raspap/networking
sudo mkdir /etc/raspap/hostapd
sudo mkdir /etc/raspap/lighttpd
```

Move RaspAP's auth control file to the correct location.

```
sudo cp raspap.php /etc/raspap 
```

Set the files ownership to `www-data` user for the web files and RaspAP config.

```
sudo chown -R www-data:www-data /var/www/html
sudo chown -R www-data:www-data /etc/raspap
```

Move the hostapd logging and service control shell scripts to the correct location.

```
sudo mv installers/*log.sh /etc/raspap/hostapd 
sudo mv installers/service*.sh /etc/raspap/hostapd
```

Set ownership and permissions for the logging and service control scripts.

```
sudo chown -c root:www-data /etc/raspap/hostapd/*.sh 
sudo chmod 750 /etc/raspap/hostapd/*.sh 
```

Copy and set ownership of the lighttpd control scripts.
```
sudo cp installers/configport.sh /etc/raspap/lighttpd
sudo chown -c root:www-data /etc/raspap/lighttpd/*.sh
```

Move the raspapd daemon to the correct location and enable it.

```
sudo mv installers/raspapd.service /lib/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable raspapd.service
```

Copy the configuration files for dhcpcd, dnsmasq, hostapd and `defaults.json`. Optionally, backup your existing `hostapd.conf`.

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

> :information_source: **Note:** If you wish to modify RaspAP's default configuration for dnsmasq and dhcp, you may do so by editing `config/defaults.json`.

Disable `systemd-networkd` and copy the bridge configuration.

```
sudo systemctl stop systemd-networkd
sudo systemctl disable systemd-networkd
sudo cp config/raspap-bridge-br0.netdev /etc/systemd/network/raspap-bridge-br0.netdev
sudo cp config/raspap-br0-member-eth0.network /etc/systemd/network/raspap-br0-member-eth0.network 
```

(Optional) Optimize PHP, replacing `php7.3-cgi` with your installed version.

```
sudo sed -i -E 's/^session\.cookie_httponly\s*=\s*(0|([O|o]ff)|([F|f]alse)|([N|n]o))\s*$/session.cookie_httponly = 1/' /etc/php/7.3/cgi/php.ini
sudo sed -i -E 's/^;?opcache\.enable\s*=\s*(0|([O|o]ff)|([F|f]alse)|([N|n]o))\s*$/opcache.enable = 1/' /etc/php/7.3/cgi/php.ini
sudo phpenmod opcache
```

Enable IP forwarding.

```
echo "net.ipv4.ip_forward=1" | sudo tee /etc/sysctl.d/90_raspap.conf > /dev/null
sudo sysctl -p /etc/sysctl.d/90_raspap.conf
sudo /etc/init.d/procps restart
```

Create iptables NAT rules and persist them.

```
sudo iptables -t nat -A POSTROUTING -j MASQUERADE
sudo iptables -t nat -A POSTROUTING -s 192.168.50.0/24 ! -d 192.168.50.0/24 -j MASQUERADE
sudo iptables-save | sudo tee /etc/iptables/rules.v4
```

Unmask and enable hostapd.service.

```
sudo systemctl unmask hostapd.service
sudo systemctl enable hostapd.service
```

(Optional) Install OpenVPN, enabling the option in RaspAP's config and enable the openvpn-client service.

```
sudo apt-get install openvpn
sudo sed -i "s/\('RASPI_OPENVPN_ENABLED', \)false/\1true/g" /var/www/html/includes/config.php
sudo systemctl enable openvpn-client@client
```

(Optional) Create OpenVPN auth control scripts, set ownership and permissions.

```
sudo mkdir /etc/raspap/openvpn/
sudo cp installers/configauth.sh /etc/raspap/openvpn/
sudo chown -c root:www-data /etc/raspap/openvpn/*.sh 
sudo chmod 750 /etc/raspap/openvpn/*.sh
```

(Optional) Install Ad blocking, enabling the option in RaspAP's config.

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

Reboot and it should be up and running.

```
sudo reboot
```

The default username is "admin" and the default password is "secret". It is recommended that you change this in RaspAP's **Authentication** panel.


