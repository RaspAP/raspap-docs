# Network Devices

## Overview
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](/insiders/)

[Insiders](/insiders/) are able to manage a variety of physical network devices as a source of data connectivity for RaspAP.
Broadly, this includes devices such as tethered phones, USB modems/routers, WLAN adapters and so on. This expands the practicality of RaspAP as a truly mobile AP for travel and/or field applications. 

## Supported device types
The following network devices are supported:

- Ethernet interface (eth)
- Wireless adapter (wlan)
- Mobile data modem (ppp)
- Mobile data adapter with built-in router
- USB connected smartphone (USB tethering)  

All devices require a driver in order to be available for use with RaspAP. 

## Listing detected devices
The **Networking > Network Devices** tab displays a list of available devices with their attributes and assumed adapter type. The adapter type as well as the device name can be changed.
Incorrect device types might appear for some devices, which advertize themselves to the system as an ethernet (e.g. `eth0`) or usb (e.g. `usb0`) device. This often happens for USB connected phones and external routers.  

![Networking: Network devices](https://user-images.githubusercontent.com/229399/116096642-bf0e4780-a6a9-11eb-9794-6935b0858b9b.png)

### Changing the device name
Changing the name helps to distinguish different devices. This is especially important if, for example, the **Access Point** device is connected via USB and the automatically assigned name is changed.
This can sometimes occur when devices are connected in varying order.

To modify a device's name, enter a value in the **Fixed name** field and choose **Change**.

The only restriction for the device name is that it must contain only lowercase letters and numbers. The maximal length is limited to 20 characters. Devices names are automatically filtered accordingly. 

## Ethernet interfaces
The built-in ethernet adapter as well as USB adapters are usually detected automatically. In these cases no configuration is required.
Devices such as USB tethered phones might appear as an ethernet device as well. The same applies to mobile data adapters that also contain a router.

In these cases, the type may be adjusted in the device list and a name assigned to the device. This will have an effect on the network device widget shown on the dashboard.

## Wireless network devices
These devices are usually listed with the automatically assigned device name prefix **wlan**, for example `wlan0`. If multiple wlan interfaces are used, it can be advantageous to assign a unique
name to the device.
 
Wireless devices will only appear if a supported driver exists in the currently installed OS. If your device does not appear in the list, this usually indicates that a required device driver is missing.
The helper script [install_wlan_driver_modules.sh](https://github.com/RaspAP/raspap-tools/blob/main/install_raspap_ram_wlan.sh) in [RaspAP/raspap-tools](https://github.com/RaspAP/raspap-tools)
can be used to search for and install existing driver modules. 

## Mobile data modems
Modems or Point-to-Point Protocol (ppp) devices require login data. This includes a PIN number to unlock the SIM card, the Access Point Name (APN) and login data of your mobile network provider. 
These values may be entered under the **Networking > Mobile Data Settings** tab. 

![image](https://user-images.githubusercontent.com/229399/116100321-182baa80-a6ad-11eb-9fd5-4a3bc22b9388.png){: style="width:375px"}

Values entered here are stored in the file `/etc/wvdial.conf`. This configuration file contains the basic configuration needed to unlock the SIM card and connect
to the network. This has been tested with a Huawei E1550. If your device requires different AT-commands, you will need to manually change this configuration. 

For a correctly connected modem, the connection mode, signal quality and network provider will be displayed on the dashboard.

![image](https://user-images.githubusercontent.com/33725910/115954368-ec63c580-a4f0-11eb-8f4b-3a8830ee1d35.png){: style="width:450px"}

> :information_source: **Note:** The names of modems cannot be changed. The reason is that the device name `ppp0` is directly coupled with the required system services.

### What if my modem device doesn't appear?
In this case your connected modem device is not recognized by the OS, or it has not been switched into modem mode by [usb_modeswitch](https://www.draisberghof.de/usb_modeswitch/).
Check the log file (`journalctl`) for problems with the device. 

## Mobile data adapters with built-in routers
Mobile data USB devices which provide router functionality will usually appear as an ethernet device, for example `eth1`. This implies that the device has to be pre-configured
to work without a PIN for the SIM card and without login data. Typically, this can be done via a browser based administration interface on any computer.

### Huawei Hilink Device
A special case are Huawei Hilink devices (e.g. Huawei E3372h-320). RaspAP can communicate directly with these devices. Be sure that the administration interface is _not_ locked with a user/password.
The PIN number entered on the **Networking > Mobile Data Settings** tab will be used to unlock the SIM card. In addition, connection information (mode, signal quality and network provider) are
extracted from the device and displayed on the dashboard. The dashboard button to stop/start the device is active and will disconnect/connect the mobile network.

![image](https://user-images.githubusercontent.com/33725910/115952612-3a73cb80-a4e7-11eb-8998-cbb66fb108c4.png){: style="width:450px"}

The model E3372h-320 will be detected as a **Hilink** device and appears with the name `hilink0`. Other Hilink devices require a corresponding assignment on the **Networking > Network Devices** tab.

## USB tethered phones
A phone connected via USB and with USB tethering enabled will appear as either an ethernet device (e.g. `eth1`), or as a USB network device (e.g. `usb0`).
Changing the device type to **phone** will result in a corresponding display on the dashboard. In this case the default name is `phone0`.

![image](https://user-images.githubusercontent.com/33725910/115953764-96415300-a4ed-11eb-9d5c-de4f27550874.png){: style="width:450px"}

## Configuration files
- All device specific settings are stored as UDEV rules in the file `/etc/udev/rules.d/80-raspap-net-devices.rules`.
- The templates for the UDEV rules are stored in `/etc/raspap/networking/client_udev_prototypes.json`. This file contains the list of recognized device types.
- Mobile data settings are stored in: `/etc/raspap/networking/mobiledata.ini`
- Modem AT-commands and login data are stored in: `/etc/wvdial.conf`

