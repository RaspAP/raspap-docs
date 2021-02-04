# SSL certificates (manual)

**Update:** this process is now [automated by the Quick Installer](/ssl-quick/).

## Overview
HTTPS prevents network attackers from observing or injecting page contents. Clearly, this is a _good thing_ for RaspAP — given its function for creating and managing wireless networks. But HTTPS needs TLS certificates, and while deploying public websites is largely a [solved issue thanks to the ACME protocol and Let's Encrypt](https://www.leebutterman.com/2019/08/05/analyzing-hundreds-of-millions-of-ssl-connections.html), local web servers still mostly use HTTP because no one can get a universally valid certificate for localhost.

## Locally trusted certificates 
Managing your own Certificate Authority (CA) is the best solution, but this usually requires an involved manual setup routine. An excellent solution for local websites is [mkcert](https://github.com/FiloSottile/mkcert). This is a zero-config tool for making locally-trusted certificates with any name you like. mkcert automatically creates and installs a local CA in the system root store and generates locally-trusted certificates. It also works perfectly well with RaspAP. This allows you to generate a trusted certificate for a hostname (eg., raspap.local) or IP address because it only works for you. 

![raspap.local](https://i.imgur.com/kQoeh0S.png)

Here's the twist: it doesn't generate self-signed certificates, but certificates signed by your own private CA. This tool does not automatically configure servers or mobile clients to use the certificates, though — that's up to you (see the steps below).

Read more about mkcert [here](https://blog.filippo.io/mkcert-valid-https-certificates-for-localhost/) and [follow the project on GitHub](https://github.com/FiloSottile/mkcert).

## How-To
Follow the steps below to generate and install a locally-trusted certificate for RaspAP. The local domain `raspap.local` is used in the examples below. You may substitute this with the default `raspberrypi.local` or your own hostname. 

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
... and look for output like this:
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
Edit the lighttpd configuration:
```
sudo nano /etc/lighttpd/lighttpd.conf
```
... and add the following block to enable SSL with your new certificate:
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
   Loaded: loaded (/lib/systemd/system/lighttpd.service; enabled)
   Active: active (running) since Mon 2019-07-01 11:56:15 UTC; 1s ago
  Process: 1433 ExecStartPre=/usr/sbin/lighttpd -t -f /etc/lighttpd/lighttpd.conf (code=exited, status=0/SUCCESS)
 Main PID: 1443 (lighttpd)
   CGroup: /system.slice/lighttpd.service
           ├─1443 /usr/sbin/lighttpd -D -f /etc/lighttpd/lighttpd.conf
           ├─1453 /usr/bin/php-cgi
           ├─1454 /usr/bin/php-cgi
           ├─1455 /usr/bin/php-cgi
           ├─1456 /usr/bin/php-cgi
           └─1457 /usr/bin/php-cgi

Jul 01 11:56:15 raspap lighttpd[1433]: Syntax OK
Jul 01 11:56:15 raspap systemd[1]: Started Lighttpd Daemon.
```
Now, copy `rootCA.pem` to your lighttpd web root (**important:** do *NOT* share `rootCA-key.pem`):
```
sudo cp /home/pi/.local/share/mkcert/rootCA.pem /var/www/html
```
Open a browser and enter the address: http://raspap.local/rootCA.pem. Download the root certificate to your client and add it to your system keychain. Examples below illustrate this process on OSX:

![](https://i.imgur.com/RCJJPYL.png)

Be sure to set this certificate to "Always trust" to avoid browser warnings. 

![](https://i.imgur.com/Lx8Plqi.png)

Finally, enter the address https://raspap.local in your browser. Enjoy an encrypted SSL connection to RaspAP.

## Mobile devices
For the certificates to be trusted on mobile devices and remote clients, you will have to install the root CA using the method described above. Alternatively, on iOS, you can either use AirDrop or email the CA to yourself. After installing it, be sure to enable full trust. 

For Android, you will have to install the CA and then enable user roots. See [this StackOverflow answer](https://stackoverflow.com/a/22040887/749014).

More advanced topics are [covered at mkcert](https://github.com/FiloSottile/mkcert#advanced-topics).
 
