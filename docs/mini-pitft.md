# Mini PiTFT stats display

## Overview

The [Adafruit Mini PiTFT](https://www.adafruit.com/product/4393) is an affordable 135x240 color TFT display for the Raspberry Pi. The PiTFT connects to the 'top' 2x12 headers on the Pi's 2x20 GPIO header connection. It comes pre-assembled and tested so it can simply be attached to the Pi's header pins (no soldering required). Its low cost, form factor and bright display make it well suited as an add-on for RaspAP.

Using the display is straightforward with Adafruit's [CircuitPython library for the ST7789 chipset](https://github.com/adafruit/Adafruit_CircuitPython_ST7789). For this application we will use the Python imaging library (PIL) to output some useful stats for RaspAP. The Mini PiTFT's small size complements the Pi Zero W, although for this example we're using a Pi Model 4. 

![Adafruit Mini PiTFT](https://user-images.githubusercontent.com/229399/224494563-d13e8c09-95b4-4a73-9521-d745973b311c.jpg)

## Setup
With the Mini PiTFT attached to your Pi's GPIO pins, follow Adafruit's [setup guide for Python](https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi/python-setup). You will need to verify that Serial Peripheral Interface (SPI) is enabled on your Pi and that you are running Python 3.

Check that SPI is enabled on your Pi with `grep "^dt.*" /boot/config.txt`:
```
dtparam=spi=on
...
```
If you don't see the above, edit this file with `sudo nano /boot/config.txt`, add this line, save the file and reboot your Pi.

> :information_source: **Note:** Some users have followed Adafruit's setup guide and installed the kernel module, which is useful if you want to draw to the framebuffer and output a [mini console](https://cdn-learn.adafruit.com/assets/assets/000/082/874/large1024/adafruit_products_4393_demo_ORIG_2019_10.jpg?1571860426). However, the TFT kernel driver can't be run alongside the Python install. So you should choose one method, not both.

Install RaspAP using the [Quick Installer](quick.md):
```
curl -sL https://install.raspap.com | bash
```  
Alternatively, you can follow the [manual setup](manual.md) instructions.

With the preliminary setup done, execute RaspAP's [stats.py](https://github.com/RaspAP/raspap-webgui/blob/master/app/pitft/stats.py) with: `sudo python3 stats.py`. Your Mini PiTFT should output a summary of RaspAP's status, like so:

![](https://user-images.githubusercontent.com/229399/224494592-1b76482e-4bc7-4448-9319-f0f1b064b769.jpg)

This program updates the display every 100 milliseconds until exited. Interrupt its execution with ++ctrl+c++. 

## Running on boot
It's easy to run this each time your Pi starts up. There are a few ways to do this, but the simplest method is to edit `/etc/rc.local`. Assuming a typical install of RaspAP, the stats.py path is `/var/www/html/app/pitft/stats.py`. In the example below, we've copied this to Pi user's home directory with `cp stats.py /home/pi`. You may then edit rc.local with `sudo nano /etc/rc.local` and add the line below before `exit 0`:

```
sudo /usr/bin/python3 /home/pi/stats.py &
exit 0
```

Save and exit, then reboot your Pi to confirm that the stats display runs on boot.

