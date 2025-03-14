# NTP Service

![ntp-service](https://github.com/user-attachments/assets/9bd23465-5fd2-4a58-98e2-ab28ccc22a16){: style="width:640px"}

## Overview
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

One of the limitations of devices such as the Raspberry Pi is that it lacks an onboard **real-time clock (RTC)** to accurately keep track of the time, including when the device is powered off. To overcome this, two solutions are generally available: 1) install a hardware RTC module, or 2) synchronize time from the network. 

The **Network Time Protocol (NTP)** is widely used to fulfill this need. This is a protocol that, together with its associated daemon and related tools, is able to keep all the system clocks in a local network in sync with authoritative millisecond precision.

## Use cases
There are many scenarios in which accurate and synchronized timekeeping across networked devices can be extremely useful, if not essential. For example, a robotic controller or sensor may need to perform an operation at a specific interval but, for one reason or another, doesn't have reliable internet connectivity.

In this situation, a single internet connected device (the NTP server) will synchronize the time of the robot or sensor (NTP clients). These devices may already receive control instructions and/or exchange data with the server via a wireless network, such as the one provided by RaspAP. In this way, NTP functions as an additional service layer on top of an existing WiFi network.

Alternatively, a standalone configuration may be needed in which precision timekeeping is required for a network device.

## Installation
The NTP server is available as an Insiders-only plugin that may be installed from the **System > Plugins** tab. Simply choose **Details** corresponding to the plugin, then **Install now** from the modal dialog. The plugin installer will automatically refresh the UI; the NTP server plugin will then appear in the sidebar and be immediately available to configure.

## Configuration
Following the installation, the NTP service should be up and running. You may check and control its current state by visiting RaspAP's **&nbsp;:fontawesome-regular-clock: NTP Server** administration page. Basic **Settings** as well as **Advanced** controls are available on their respective tabs. The **Status** tab will display the operational state of connected peers by using the `ntpq` query tool. These status queries are [examined in detail](ntp.md#peer-status-queries) to assist you with interpreting them.

### Standalone device
In a standalone configuration, a single device will be automatically kept in sync by communicating with remote NTP servers tied to high quality clocks. As long as the `ntpd.service` is running (enabled on boot by default), the protocol will largely handle the time syncronization for you with its default settings. This of course assumes the device has internet connectivity.

The **NTP Server > Settings** tab will report the current system time synchronized from its remote NTP server peers.

![ntp-configuration](https://github.com/RaspAP/raspap-webgui/assets/229399/fd11db3e-091f-4d46-868a-a2d77c4d23cd){: style="width:420px"}

You may add any number of public NTP servers by entering their IP address or fully qualified domain name (FQDN) under **Add an NTP server**.

!!! tip "Tip"
    Public NTP servers that support **Network Time Security (NTS)** may be specified by appending the `nts` suffix.

Click or tap the :fontawesome-solid-plus: icon to add an entry to your list of servers and choose **Save settings**. The `ntpd.service` will be automatically restarted.

### Multiple devices
In an environment with multiple networked devices, some of which may lack internet connectivity, an NTP server on your local network may be used to keep them synchronized. To create this configuration, under **Add an NTP server** (shown above) specify a private IP address or local network host address, for example `time.raspberrypi.local`, of the NTP server on your local network. Click or tap the :fontawesome-solid-plus: icon to add it to your list of servers and choose **Save settings**. The `ntpd.service` will automatically restart for you.

Repeat this process for each of the devices you wish to keep synchronized on your network. 

## Advanced settings
For users who are familiar with the NTP protocol and [configuration file](https://docs.ntpsec.org/), the **NTP Server > Advanced** tab permits you to view and edit this file directly. This gives you full control over the NTP server settings, beyond the basic configuration provided on the **Settings** tab.

![ntp-advanced](https://github.com/RaspAP/raspap-webgui/assets/229399/161e7c44-31ef-4784-924b-7d40999cdc90){: style="width:420px"}

To enable `ntp.config` editing, simply slide the **Edit mode** toggle. You may then make your edits to the configuration directly. When you are finished editing, choose **Save settings**. The `ntpd.service` will restart automatically. 

!!! warning "Caution"
    Editing the `ntp.config` file may lead to unpredictable results and/or cause the NTP service to enter a failed state. For this reason, it's recommended to preserve a backup of your original NTP configuration.

## Peer status queries

The NTP query utility `ntpq` is used to monitor NTP daemon `ntpd` operations and give useful performance metrics. The `-p` or `--peers` option is used with `ntpq` to output a list of the peers known to the server as well as a summary of their state. This is available on the **NTP Server > Status** tab. Example output is shown below:

```
     remote           refid      st t when poll reach   delay   offset   jitter
===============================================================================
+time.cloudflare 10.109.8.98      3 u  723 1024  377  27.6182   1.8467   3.5095
+185.198.109.227 150.214.94.10    2 u  403 1024  377  37.3427   0.1535   2.6619
+time.cloudflare 10.56.8.4        3 u  433 1024  377  21.7662   2.6731   7.5725
-ntp01.pingless. 189.97.54.122    2 u  181 1024  377  70.1582  -5.9882   3.3870
-185.90.148.209  150.214.94.10    2 u  861 1024  337  63.1452   4.4984   6.3479
*ip94-143-139-21 150.214.94.10    2 u  289 1024  377  36.6112   0.3700   2.5709
```

Looking at the column headers, this status output may be interpreted with the following:

| Identifier | Description                                                  |
| ---------- | ------------------------------------------------------------ |
|`remote` | The address of a remote NTP server your local server is talking to. | 
|`refid` | A reference to where the remote server is synced from. |
|`st` | An abbreviation for "stratum" – the number of hops between that server and a high quality clock source, such as nuclear or GPS. Stratum 1 is the highest level, 15 the lowest. |
|`t` | An abbreviation for the peer "type" – local, unicast, multicast or broadcast. Most peers are accessed in unicast mode. |
|`when` | The number of seconds since your local server last polled the remote. |
|`poll` | The interval in seconds between polling of the remote server. |
|`reach` | An octal representation of the success/failure over time, 377 being 100% success. |
|`delay` | A measure of network latency to the remote server in milliseconds. |
|`offset` | The current offset, or time difference, between the peer and local system time, expressed in milliseconds. |
|`jitter` | A measure of the variation in latency or time delay over the network. |
|`*` | This marks the current preferred server as determined by the protocol. |

In the above example, our local NTP server is within 0.37ms of the preferred remote server, which itself is closely tied (`stratum=2`) to a high quality clock source. Our local server is within +/- 6ms of the other remotes.

## Firewall settings
If your system uses a network [firewall](firewall.md), such as the one provided by RaspAP, you will need to be sure that it's configured for the NTP protocol. NTP uses UDP port 123 to communicate with peers. Therefore, you must ensure that the port is open in any firewall. To enable NTP traffic with `iptables` execute the following:

```
iptables -A INPUT -p udp --dport 123 -j ACCEPT
```

Alternatively, you may use `ufw` to achieve the same result:

```
ufw allow 123/udp
```

!!! note "Note"
    If you're using RaspAP's [firewall](firewall.md), an exception is already present to allow NTP traffic by default.

## Troubleshooting
Output from the NTP system calls `ntp_gettime()` and `ntp_adjtime()` is displayed prominently on the **NTP Server > Settings** page. If present, the current synchronized timekeeping data are displayed with their associated status codes. A `code 0 (OK)` indicates that these system calls are functioning as expected, as shown below:

```
ntp_gettime() returns code 0 (OK)
  time e9b1283b.89c0db28 2024-03-29T11:44:59.538Z, (.538099359),
  maximum error 997469 us, estimated error 167 us, TAI offset 37
ntp_adjtime() returns code 0 (OK)
  modes 0x0 (),
  offset 456.591 us, frequency -1.317 ppm, interval 1 s,
  maximum error 997469 us, estimated error 167 us,
  status 0x2001 (PLL,NANO),
  time constant 6, precision 1.000 us, tolerance 500 ppm,
```

On the other hand, the kernel may occasionally report NTP clock errors like the following:

```
raspberrypi ntpd[1279]: kernel reports TIME_ERROR: 0x2041: Clock Unsynchronized"
```

The NTP system calls shown above may also return a `code 5 (ERROR)` result. In most cases, this will resolve itself in a few minutes while the system clock is synchronized. Persistent errors may indicate a misconfiguration of the NTP protocol or a general networking problem. Refer to the [firewall settings](ntp.md#firewall-settings), above.

Detailed metrics from [peer status queries](ntp.md#peer-status-queries) are also useful for troubleshooting purposes. 

Finally, ensure that no other time synchronization application is in use, such as `timesyncd` or any third party software.

## Discussions
Questions or comments about time synchronization with NTP? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).
