# Captive portal setup

The [nodogsplash project](https://github.com/nodogsplash/nodogsplash) is a lightweight, highly configurable captive portal solution. It integrates nicely with RaspAP and is recommended over other methods. No configuration changes are needed with RaspAP, however you will need to modify some default settings in the nodogsplash config. This step-by-step guide assumes you have already installed RaspAP, either with the [Quick Installer](https://github.com/billz/raspap-webgui/wiki/Quick-Installer-usage) or [manual setup instructions](https://github.com/billz/raspap-webgui/wiki/Manual-installation). 

> ℹ️  **Note:** This walkthrough is provided as a courtesy only; there is no support for NDS or any integration with this project.

## Installing the software

Begin by updating your RPi with the latest package information:
```
sudo apt-get update
```

With our package manager up to date, install a dependency required by nodogsplash:
```
sudo apt-get install libmicrohttpd-dev
```

Next, clone the nodogsplash GitHub repository to your home directory:
```
cd ~/
git clone https://github.com/nodogsplash/nodogsplash.git
```

We can now compile nodogsplash from the source:
```
cd nodogsplash
make
sudo make install
```

## Configuration changes
With nodogsplash installed in the Pi's system, we will make two small changes to its configuration. The nodogsplash `GatewayInterface` should be set to the interface RaspAP runs on (`wlan0` is the default). You will also need to change the `GateWayAddress` to `10.3.141.1`. **Note:** if you have modified RaspAP's default config, be sure this setting reflects your changes.

```
sudo nano /etc/nodogsplash/nodogsplash.conf
```

```
# GatewayInterface is not autodetected, has no default, and must be set here.
# Set GatewayInterface to the interface on your router
# that is to be managed by Nodogsplash.
# Typically br-lan for the wired and wireless lan.
#
GatewayInterface wlan0
#
# Parameter: GatewayAddress
# Default: Discovered from GatewayInterface
#
# This should be autodetected on an OpenWRT system, but if not:
# Set GatewayAddress to the IP address of the router on
# the GatewayInterface.  This is the address that the Nodogsplash
# server listens on.
GatewayAddress 10.3.141.1
```
Save and quit out of the editor by pressing **Ctrl+X** and then pressing **Y** and finally **Enter**.

## Starting the captive portal
We are now ready to start up the software. This can be done by simply executing the binary with `sudo nodogsplash`. However, we'll make things a bit easier by adding a `systemd` service provided by the project. Copy the service control file and enable it:
```
sudo cp ~/nodogsplash/debian/nodogsplash.service /lib/systemd/system/
sudo systemctl enable nodogsplash.service 
```

Next, start the service and check its status:
```
sudo systemctl start nodogsplash.service 
sudo systemctl status nodogsplash.service
```

You should see output similar to the following:
```
● nodogsplash.service - NoDogSplash Captive Portal
   Loaded: loaded (/lib/systemd/system/nodogsplash.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2020-02-11 09:19:44 GMT; 34min ago
 Main PID: 10539 (nodogsplash)
    Tasks: 4 (limit: 1599)
   Memory: 1.7M
   CGroup: /system.slice/nodogsplash.service
           └─10539 /usr/bin/nodogsplash

Feb 11 09:19:44 raspberrypi systemd[1]: Starting NoDogSplash Captive Portal...
Feb 11 09:19:44 raspberrypi nodogsplash[10538]: [5][Tue Feb 11 09:19:44 2020][10538](src/main.c:496) Starting as daemon, forking to background
Feb 11 09:19:44 raspberrypi nodogsplash[10538]: [5][Tue Feb 11 09:19:44 2020][10539](src/main.c:271) Detected gateway wlan0 at 10.3.141.1 (dc:a6:32:3d:ff:9d)
Feb 11 09:19:44 raspberrypi nodogsplash[10538]: [5][Tue Feb 11 09:19:44 2020][10539](src/main.c:275) MHD Unescape Callback is Disabled
Feb 11 09:19:44 raspberrypi nodogsplash[10538]: [5][Tue Feb 11 09:19:44 2020][10539](src/main.c:305) Created web server on 10.3.141.1:2050
Feb 11 09:19:44 raspberrypi nodogsplash[10538]: [5][Tue Feb 11 09:19:44 2020][10539](src/main.c:319) Using config options for FAS or Templated Splash.
Feb 11 09:19:44 raspberrypi systemd[1]: Started NoDogSplash Captive Portal.
Feb 11 09:19:46 raspberrypi nodogsplash[10538]: [5][Tue Feb 11 09:19:46 2020][10539](src/fw_iptables.c:382) Initializing firewall rules
```

**Note:** The captive portal may be stopped with `sudo systemctl stop nodogsplash.service` or disabled completely with `sudo systemctl disable nodogsplash.service`.

## Connecting clients
Connect a client to RaspAP's hotspot. You should now see nodogsplash's captive portal screen:

![captive portal screen](https://i.imgur.com/qS9mgTr.png)

Optional: you can customize the captive portal screen by modifying the files located in `/etc/nodogsplash/htdocs/`. 

