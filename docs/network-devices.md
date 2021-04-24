# Handling and Configuration of Network Devices
The following network devices are supported 
* Ethernet interface (eth)
* Wireless adapter (wlan)
* Mobile data Modem (ppp)
* Mobile data adapter with build in router
* USB conncected Smartphone (USB tethering)  

All devices require a driver in order to be available for RaspAP. 

## List of detected Devices
Under Networking -> Network Devices the list of devices is available with their attributes and assumed adapter type. The adpapter type as well as the device name can be changed.
Incorrect device types might show up for devices, which advertize them to the system as an ethernet (e.g. `eth0`) or usb (e.g. `usb0`) device. This happens for USB connected phones and external routers.  
The only restriction for the name is, that it contains only lowercase letters and numbers. The maximal length is limited to 10 characters. The name is automatically filtered accordingly. 
Fixing the name helps to distinguish the different devices. This is especially important, if there is a risk, that the Access Point device is connected via USB and the automatically assigned name might change.

All settings are stored as UDEV rules in the file `/etc/udev/rules.d/80-raspap-net-devices.rules`.
The templates for the rules are stored in `/etc/raspap/networking/client_udev_prototypes.json`. This file contains the list of recognized device types.

## Ethernet Interface
The build in ethernet adapter as well as USB ones are usually detected automatically and no configuration is required.
Devices like USB tethered phones might show up as an ethernet device as well. The same applies to mobile data adpapters, which contain a router. In these cases the 
type can be adjusted in the device list and a name can be assigned to the device. This will have an effect on the display on the dashboard.

## Wireless Network device
The devices are listed usually with the automatically assigned device name prefix wlan(e.g. `wlan0`). If multiple wlan interfaces are used, it can be an advantage to fix the name of the devices in order to avoid changing names for the devices. Rhis might happen, if devices are connected in different order.

Devices will only show up, if a driver is existing in Raspian. If your device does not show up, a device driver is missing. Have a look at the script 
[raspap/raspap-tools/install_wlan_driver_modules.sh](https://github.com/RaspAP/raspap-tools/blob/main/install_raspap_ram_wlan.sh) 
to search for existing driver modules. 

## Mobile Data Modem
Modems or Point-to-Point Protocol (ppp) devices require login data. A PIN number to unlock the SIM card, the Access Point Name (APN) and login data of your mobile network provider. 
These data can be entered under Networking -> Mobile Data Settings. The data are written to the file /etc/wvdial.conf. This configuration file contains the basic configuration to unlock the SIM card and connect
to the network. This has been tested with a Huawei E1550. If your device requires different AT-commands, you need to manually change this configuration. 

For a correctly connected modem, the connection mode, signal quality and network provider will be displayed on the dashboard.

Be aware, that the name of modems can not be changed. The reason is, that the device name `ppp0` is directly coupled with the required system services.

## Mobile Data Adapter with build in Router
Mobile data USB devices, which provide router functionality will usually show up as a ethernet device (e.g. `eth1`). This implies, that the device has to be pre-configured
to work without a PIN for the SIM card and without login data, This usually can be done via the browser based administration interface on any computer.

A special case are Huawei Hilink devices (e.g. Huawei E3372h-320). RaspAP can communicate directly with these devices. Only the administration interface should not be locked with a user/password. The PIN number entered under Networking -> Mobile Data Settings will be used to unlock the SIM card. IN addition connection information (mode, signal quality and network provider) are listed 
on the dashboard. 

The model E3372h-320 will be detected as a Hilink device and shows up wth the name `hilink0`. Other Hilink devices require a corresponding assignment 
under Networking -> Network Devices.


