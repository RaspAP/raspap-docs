# Authentication

## Overview
RaspAP's authentication module uses HTTP's built-in framework to limit access to authorized users. Known as the HTTP "Basic" scheme, when first accessing RaspAP on your device the server will respond with a `401` (unauthorized) status. Authentication is then handled with a response header that presents a login challenge in the browser.

The default administrator login is:

  **Username:** `admin`  
  **Password:** `secret`  

After performing the initial login, it's _strongly recommended_ to change these default credentials. This is a first-line countermeasure against unauthorized users taking control of your wireless network.

!!! Note
    The "Basic" HTTP authentication scheme is defined in [RFC 7617](https://datatracker.ietf.org/doc/html/rfc7617), which transmits credentials as user ID/password pairs, encoded using base64.

### How secure is basic auth?
The HTTP Basic Authentication scheme is not considered to be secure on its own, especially over plain HTTP. This is because it sends the username and password in an easily decodable Base64-encoded format. Without an additional encryption layer, credentials are sent over the network in plain text. This makes it highly vulnerable to interception by attackers via man-in-the-middle (MITM) attacks or by packet sniffing. 

### Using HTTPS/TLS
Basic Authentication can be used securely if transmitted over HTTPS, which encrypts the entire communication channel. For this reason, RaspAP has simplified the process of creating [locally-trusted SSL certificates](ssl.md) with the [Quick installer](ssl.md#quick-installer). When HTTPS/TLS is enabled with a RaspAP install, this authentication process is significantly more secure. 

## Best security practices
In most scenarios, a potential attacker can only access RaspAP's admin login prompt if they are already associated with your wireless access point. To mitigate this, change the default `raspap-webgui` SSID and generate a strong pre-shared key (PSK) or passphrase.

![](https://github.com/user-attachments/assets/416d32fc-0163-40d9-9e7f-c4d256d3f715){: style="width:480px"}


RaspAP will automatically generate a secure passphrase, or PSK, for you. On the **Hotspot > Security** tab, click or tap the magic icon :fontawesome-solid-wand-magic-sparkles: next to the PSK input. Choose **Save settings** followed by **Restart hotspot**. Thereafter, you may share RaspAP's QR code with your wireless clients.

!!! tip Tip
    Given RaspAP's popularity, assume that both the default admin login credentials _and_ the default access point SSID and password are well known to third-parties. Failure to change these default settings is an invitation to attackers.

## Limited privilege user
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

The administrator may enable a user that is able to access RaspAP's management interface, but is limited in their ability to modify the existing configuration. In this case, the limited privilege user may configure a wireless client connection on the **WiFi client** page, but is unable to change any other settings. 

![](https://github.com/user-attachments/assets/7adbee61-b3e1-4bbb-856f-b90e5b54cd0a){: style="width:480px"}

This is useful in any multi-user environment where the admin user may want to initially configure a wireless router, and then delegate client connection duties to other users of the network.

To enable the limited privilege user, slide the corresponding toggle on the **Basic** tab and choose **Save settings**. The current admin user will be prompted to logout. Thereafter, the limited privilege user will be active. To disable the limited privilege user, simply login with the administrator account again.

## Custom user avatars
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

The default administrator user icon may be replaced with a custom one of your choosing. From the **Avatar** tab, click or tap on the existing avatar to upload a new one. The new custom avatar will be displayed in RaspAP's header.

![](https://github.com/user-attachments/assets/ff7f1974-4411-4113-8130-f7ad4d9d9411){: style="width:480px"}

Image files of type `.jpg`, `.gif` or `.png` up to a maximum of 2 MB are supported. To restore the avatar to the default, choose **Reset avatar**.

## Restoring defaults
Login credentials are stored in `/etc/raspap/raspap.auth`. The password is encrypted and cannot be edited manually. If you've forgotten your admin login or wish to temporarily reset the defaults, you may do so by simply deleting this file:

```
sudo rm /etc/raspap/raspap.auth
```

This will restore the default admin login and password pair.

!!! note Note
    RaspAP uses PHP's built-in `password_hash` function which leverages the Blowfish (`CRYPT_BLOWFISH`) algorithm. Blowfish is an adaptive hashing algorithm that is widely considered to be _very secure_.

## Discussions
Questions or comments about RaspAP's authentication? Join the [discussions here](https://github.com/RaspAP/raspap-webgui/discussions/).

