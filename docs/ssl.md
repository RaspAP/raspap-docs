# SSL certificates

![ssl-certificates](https://github.com/user-attachments/assets/b7dd2965-8b2e-408a-ac97-f205b913fbe2){: style="width:640px"}

## Overview
HTTPS prevents network attackers from observing or injecting page contents. This is desirable for server applications like RaspAP &#151; or indeed any locally hosted web application. But HTTPS requires [TLS certificates](https://en.wikipedia.org/wiki/Transport_Layer_Security), and while deploying public websites is largely a solved issue thanks to the ACME protocol and Let's Encrypt, local web servers still mostly use HTTP because no one can get a universally valid certificate for localhost.

## Locally trusted certificates 
Managing your own Certificate Authority (CA) is the best solution, but this usually requires an involved manual setup routine. An excellent solution for local websites is [mkcert](https://github.com/FiloSottile/mkcert). This is a zero-config tool for making locally-trusted certificates with any name you like. `mkcert` automatically creates and installs a local CA in the system root store and generates locally-trusted certificates. It also works perfectly well with RaspAP. This allows you to generate a trusted certificate for a hostname (for example, `raspap.local`) or IP address because it only works for you. 

![raspap.local](https://user-images.githubusercontent.com/229399/228976581-34beed42-9f08-4ece-9c1b-e5a865415dab.png){: style="width:450px"}

Here's the twist: it doesn't generate self-signed certificates, but certificates signed by your own private CA. This tool does not automatically configure servers or mobile clients to use the certificates, though &#151; that's up to you. These steps are covered in detail below.

Read more about mkcert [here](https://blog.filippo.io/mkcert-valid-https-certificates-for-localhost/) and [follow the project on GitHub](https://github.com/FiloSottile/mkcert).

## Creating a certificate
There are two options to go about creating a self-signed certificate with mkcert: 1) [manually](#manual-steps), or 2) with the [Quick installer](#quick-installer). Both methods are described below.

### Manual steps
Follow the steps below to generate and install a locally-trusted certificate for RaspAP. The local domain `raspap.local` is used in the examples below. You may substitute this with the default `raspberrypi.local` or your own hostname. 

!!! tip "Tip"
    If you've changed your hostname prior to starting this process, be sure to reboot your device for the change to take effect.

Start by installing the pre-built binary for Arch Linux ARM on your Raspberry Pi:
```
sudo wget https://github.com/FiloSottile/mkcert/releases/download/v1.3.0/mkcert-v1.3.0-linux-arm -O /usr/local/bin/mkcert
sudo chmod +x /usr/local/bin/mkcert
mkcert -install
```
You should see output like the following:
```
Using the local CA at "/home/pi/.local/share/mkcert" ✨
The local CA is now installed in the system trust store! ⚡️
```
Generate a certificate for `raspap.local`:
```
cd /home/pi
mkcert raspap.local "*.raspap.local" raspap.local
```
You should see output like the following:
```
Using the local CA at "/home/pi/.local/share/mkcert" ✨

Created a new certificate valid for the following names 📜
 - "raspap.local"
 - "*.raspap.local"
 - "raspap.local"

Reminder: X.509 wildcards only go one level deep, so this won't match a.b.raspap.local ℹ️
The certificate is at "./raspap.local+2.pem" and the key at "./raspap.local+2-key.pem" ✅
```
Next, combine the private key and certificate:
```
cat raspap.local+2-key.pem raspap.local+2.pem > raspap.local.pem
```
Create a directory for the combined `.pem` file in lighttpd:
```
sudo mkdir /etc/lighttpd/ssl
```
Set permissions and move the `.pem` file:
```
chmod 400 /home/pi/raspap.local.pem
sudo mv /home/pi/raspap.local.pem /etc/lighttpd/ssl
```
Edit the lighttpd configuration with `sudo nano /etc/lighttpd/lighttpd.conf`. Add the following block to enable SSL with your new certificate:

```
server.modules += ("mod_openssl")
$SERVER["socket"] == ":443" {
  ssl.engine = "enable"
  ssl.pemfile = "/etc/lighttpd/ssl/raspap.local.pem"
  ssl.ca-file = "/home/pi/.local/share/mkcert/rootCA.pem"
  server.name = "raspap.local"
  server.document-root = "/var/www/html"
}
```

Optionally, you can redirect all HTTP requests to HTTPS like so:
```
$SERVER["socket"] == ":80" {
  $HTTP["host"] =~ "(.*)" {
    url.redirect = ( "^/(.*)" => "https://%1/$1" )
  }
}
```
Save your changes and quit out of the editor with ++ctrl+x++ followed by ++y++ and finally ++enter++.

Restart the lighttpd service:
```
sudo systemctl restart lighttpd
```
Verify that lighttpd has restarted without errors:
```
sudo systemctl status lighttpd
```
You should see a response like the following:
```
● lighttpd.service - Lighttpd Daemon
     Loaded: loaded (/lib/systemd/system/lighttpd.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2023-03-26 10:09:46 CEST; 5 days ago
   Main PID: 1080 (lighttpd)
      Tasks: 6 (limit: 779)
        CPU: 5min 17.332s
     CGroup: /system.slice/lighttpd.service
             ├─1080 /usr/sbin/lighttpd -D -f /etc/lighttpd/lighttpd.conf
             ├─1168 /usr/bin/php-cgi
             ├─1185 /usr/bin/php-cgi
             ├─1186 /usr/bin/php-cgi
             ├─1187 /usr/bin/php-cgi
             └─1188 /usr/bin/php-cgi

Mar 30 18:23:38 raspap lighttpd[1433]: Syntax OK
Mar 30 18:23:38 raspap systemd[1]: Started Lighttpd Daemon.
```
Now, copy `rootCA.pem` to your lighttpd web root:
```
sudo cp /home/pi/.local/share/mkcert/rootCA.pem /var/www/html
```

!!! warning "Important"
    Do *not* share the `rootCA-key.pem` file.

Finish by following the [client configuration](#client-configuration) steps below.

### Quick installer
The [Quick Installer](quick.md) may also be used to generate SSL certs with `mkcert`. The installer automates the manual steps described above, including configuring lighttpd with SSL support. It's recommended to review these steps to have an idea of what is happening behind the scenes. 

Invoke the Quick installer and specify the `-c` or `--cert` option, like so:

```
curl -sL https://install.raspap.com | bash -s -- --cert
```

!!! note "Note"
    Executing the Quick installer only installs `mkcert` and generates an SSL certificate with the input you provide. It does _not_ (re)install RaspAP. 

```
$ curl -sL https://install.raspap.com | bash -s -- --cert


 888888ba                              .d888888   888888ba
 88     8b                            d8     88   88     8b
a88aaaa8P' .d8888b. .d8888b. 88d888b. 88aaaaa88a a88aaaa8P
 88    8b. 88    88 Y8ooooo. 88    88 88     88   88
 88     88 88.  .88       88 88.  .88 88     88   88
 dP     dP  88888P8  88888P  88Y888P  88     88   dP
                             88
                             dP      version 3.2.1

The Quick Installer will guide you through a few easy steps


RaspAP mkcert: Configure a new SSL certificate
Current system hostname is raspap
Create an SSL certificate for raspap.local? (Recommended) [y/N] y
Install to lighttpd SSL directory: /etc/lighttpd/ssl? [y/N]: y
***************************************************************
A new SSL certificate for: raspap.local
will be installed to lighttpd SSL directory: /etc/lighttpd/ssl
***************************************************************
Complete installation with these values? [y/N]: y
RaspAP mkcert: Fetching mkcert binary
RaspAP mkcert: Installing mkcert
Using the local CA at "/home/pi/.local/share/mkcert" ✨
The local CA is already installed in the system trust store! 👍
Warning: "certutil" is not available, so the CA can't be automatically installed in Firefox and/or Chrome/Chromium! ⚠️
Install "certutil" with "apt install libnss3-tools" and re-run "mkcert -install" 👈

RaspAP mkcert: Generating a new certificate for raspap.local
Using the local CA at "/home/pi/.local/share/mkcert" ✨
Warning: the local CA is not installed in the Firefox and/or Chrome/Chromium trust store! ⚠️
Run "mkcert -install" to avoid verification errors ‼️
Created a new certificate valid for the following names 📜
 - "raspap.local"
 - "*.raspap.local.local"
 - "raspap.local"

Reminder: X.509 wildcards only go one level deep, so this won't match a.b.raspap.local.local ℹ️

The certificate is at "./raspap.local+2.pem" and the key at "./raspap.local+2-key.pem" ✅
```

The installer will guide you through the steps of creating a certificate, as shown above. Complete the installation by following the [client configuration](#client-configuration) steps below.

## Client configuration
Open a browser and enter the following address, substituting the domain name you chose in the steps above: `http://raspap.local/rootCA.pem`. Download the root certificate to your client and add it to your system keychain. Examples below illustrate this process on macOS:

![](https://user-images.githubusercontent.com/229399/228977507-45efefa9-c2e1-4ed5-a298-a8aca5e3c7b7.png){: style="width:450px"}

Be sure to set this certificate to "Always trust" to avoid browser warnings. 

![](https://user-images.githubusercontent.com/229399/228977568-08db7696-677a-47b3-bca1-33c7a4d34792.png){: style="width:450px"}

Finally, enter the address `https://raspap.local` in your browser. Enjoy an encrypted SSL connection to RaspAP.

## Mobile devices
For the certificates to be trusted on mobile devices and remote clients, you will have to install the root CA using the method described above. Alternatively, on iOS, you can either use AirDrop or email the CA to yourself. After installing it, be sure to enable full trust. 

More advanced topics are [covered at mkcert](https://github.com/FiloSottile/mkcert#advanced-topics).
 
## Discussions
Questions or comments about using SSL certificates? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).

