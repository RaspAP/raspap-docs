# Speed testing 

![](https://user-images.githubusercontent.com/229399/228899043-4ddb0cee-687e-4e88-ba0d-e5883d821d72.jpg){: style="width:640px"}

## Overview
An internet **speed test** measures the connection speed and quality of your connected device to a remote host. Many speed test services perform multiple consecutive tests that evaluate different aspects of your internet connection, including **ping** (latency), **download** and **upload speed**. A fourth metric, known as **jitter**, measures variation in the latency of a flow of packets between two systems. Jitter is said to occur when some packets take longer to travel from one system to the other. The most common causes of jitter are network congestion, timing drift and changes in packet routing.

## Troubleshooting
The speed of your connection may vary for a variety of reasons, including the time of day. This is especially true of places such as educational or work environments where many users may be sharing the same internet connection. Known as a **contention ratio**, this refers to how many other users are contending for their share of available bandwidth. The higher the contention the more likely you are to experience a slow connection at peak times. Periodic [speed tests](https://speedtest.raspap.com/) can help you identify the best time of day to perform your tasks.

Speed tests can be useful in diagnosing other issues, such as a fault with a service provider or a misconfigured device on your network. The ability to share your test results authoritatively with a provider or network engineer is also highly useful.  

## RaspAP's speedtest server
<figure markdown>
 ![RaspAP Speedtest](https://user-images.githubusercontent.com/229399/228870882-99206d3f-a96d-487e-80a6-748fee9f2210.jpg){: style="width:640px"}
 <figcaption>RaspAP Speedtest - <a href="https://speedtest.raspap.com/" target="_blank">https://speedtest.raspap.com/</a></figcaption>
</figure>

RaspAP provides a simple, fast and mobile-friendly [public speedtest server](https://speedtest.raspap.com/) that evaluates your internet speed using the criteria mentioned above. In addition, it reports your public IP address, ISP and distance from the speedtest server. When the test is complete, you can share the results of your test with a generated image and a link to results.

Importantly, and notably different from other services, RaspAP's Speedtest is 100% [open source](https://github.com/RaspAP/speedtest) and privacy focused &#151; meaning we do not share your data with third-parties or attempt to monetize results in any way.

## WiFi speed test 
:octicons-beaker-24: Experimental · :octicons-heart-fill-24:{: .heart } [Insiders only](insiders.md)

A tool to evaluate your local WiFi network's performance is available on the **Networking > Diagnostics** tab. This permits testing of both local WiFi network throughput (that is, data transferred between the device hosting RaspAP and your wirless clients) and internet speed (data transfer between wireless clients and a remote host). A WiFi speed test is an extremely useful diagnostic tool to determine if connectivity issues are due to your ISP, your wireless connection or an issue with the device hosting your AP. 

<video src="https://user-images.githubusercontent.com/229399/214792331-4656d482-7c4d-4ca9-853d-2d1718ddf62d.mov" controls="controls" muted="muted"></video>

The WiFi speed test uses a local speedtest instance hosted by your RaspAP installation. The test is performed on a device connected to RaspAP's wireless [access point](ap-basics.md). The remote host is RaspAP's public [speedtest server](https://speedtest.raspap.com/) located in the United States. Additional speedtest hosts distributed in other geographic centers are forthcoming.


