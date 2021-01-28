# SSL certificates (installer)

## Overview

The Quick Installer may be used to generate SSL certs with `mkcert`. The installer automates the manual steps [described here](/ssl-manual/), including configuring lighttpd with SSL support. It's recommended to review the [manual setup](/ssl-manual/) to get an idea of what is happening behind the scenes. 

Simply append the `-c` or `--cert` option to the Quick Installer, like so:

`curl -sL https://install.raspap.com | bash -s -- --cert` 

**Note:** this only installs `mkcert` and generates an SSL certificate with the input you provide. It does _not_ (re)install RaspAP. 

![](https://i.imgur.com/980pfUG.gif)

The advantage with this method is it generates valid certificates signed by your own private CA, rather than self-signed certificates. The Quick Installer does not automatically configure clients to trust the certificates, however — that's up to you. See the steps below.

## Client configuration
Open a browser and enter the address: http://raspberrypi.local/rootCA.pem (this URL may be your IP address or a different hostname, depending on your unique setup). Download the root certificate to your client and add it to your system keychain. Examples below illustrate this process on OSX:

![](https://i.imgur.com/RCJJPYL.png)

Be sure to set this certificate to "Always trust" to avoid browser warnings. 

![](https://i.imgur.com/Lx8Plqi.png)

Finally, enter the address https://raspberrypi.local in your browser. Enjoy an encrypted SSL connection to RaspAP.  

## Mobile devices
For the certificates to be trusted on mobile devices and remote clients, you will have to install the root CA using the method described above. Alternatively, on iOS, you can either use AirDrop or email the CA to yourself. After installing it, be sure to enable full trust. 

More advanced topics are [covered at mkcert](https://github.com/FiloSottile/mkcert#advanced-topics).
 
