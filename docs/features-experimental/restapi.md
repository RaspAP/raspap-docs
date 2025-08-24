# RestAPI

![restful-api](https://github.com/user-attachments/assets/51b6ae1b-5cbf-4552-ad30-210cc68f854b){: style="width:640px"}

## Overview
:octicons-beaker-24: Experimental 

RaspAP includes support for stateless client-server data exchange via a high performance RESTful API. This allows clients to communicate with the API over HTTP with standard methods such as GET and POST and receive responses in JSON. RaspAP's API is powered by [FastAPI](https://fastapi.tiangolo.com/), one of the [fastest Python frameworks available](https://fastapi.tiangolo.com/#performance).

FastAPI makes use of the [Uvicorn](https://www.uvicorn.org/) ASGI web server implementation for Python. This is a minimal, low-level server interface for asynchronous frameworks.

## Use cases
A RESTful API operates asynchronously, making it suited for building microservices&#151;small, independent services that function in the context of larger applications. Examples might include a dashboard widget or other integration that consumes JSON data from the API to perform live monitoring of RaspAP's operational state.

Using the API's POST methods (to be announced soon), RaspAP's functions may even be remotely controlled outside of its regular web interface. 

## Installation
The RestAPI may be optionally installed by the [Quick installer](../get-started/quick-installer.md). To install RestAPI support, respond by pressing ++enter++ to accept the default ++y++ option at the following prompt:

```
RaspAP Install: Configure RestAPI
Install and enable RestAPI? [Y/n]:
```

!!! tip "Tip"
    The RestAPI is enabled by default in RaspAP's [Docker container](../features-experimental/restapi.md#docker-support), so if you choose this option there is nothing more for you to do.

The Python language is a requirement for the RestAPI. The Quick installer will detect if Python is not installed on your system and install it for you (Python 3 is installed by default on Raspberry Pi OS). In addition, Python's package manager `pip` will also be installed. The following Python packages are requirements for the RestAPI:

```
fastapi
uvicorn
psutil
python-dotenv
```

!!! note "Note"
    From Bookworm onwards, packages installed via `pip` must be installed into a Python Virtual Environment using `venv`. This has been introduced by the Python community, not by Raspberry Pi; see [PEP 668](https://peps.python.org/pep-0668/) for more details. The Python modules listed above are installed system-wide with the `--break-system-packages` flag.

With the software requirements installed, the systemd `restapi.service` control file will be enabled on your system, as well as the RestAPI management UI: 

```
Moving restapi systemd unit control file to /lib/systemd/system/
Enabling RestAPI management option
[ ✓ ok ]
```

Proceed with the Quick installer and accept the default ++y++ prompt to reboot your system as a final step.

## Configuration
Following a reboot, the RestAPI service should be up and running. You may check and control its current state by visiting RaspAP's **&nbsp;:fontawesome-solid-puzzle-piece: RestAPI** administration page. The **Status** tab will display the operational status of the `restapi.service`.

### Generate an API key
While the API server is operational, you must generate an API key to authenticate with the service before interacting with it. These steps are described below.

1. In the **API Key** field, use the magic icon :fontawesome-solid-wand-magic-sparkles: to generate a 32-character key.
2. Alternatively, you may create your own key&#151;just be sure it's of a sufficient length and complexity.
3. Choose **Save settings**. Your API key is stored in `/etc/raspap/api/.env`.
4. Copy your API key to the clipboard for use in the Authorization section.

![restapi-settings](https://github.com/RaspAP/raspap-webgui/assets/229399/07fd0203-0fec-4600-84f3-88dc013abcae){: style="width:520px"}

The `restapi.service` will be automatically restarted when updating your API key. At this stage, you have a valid API key that may be used to authenticate with the RestAPI. This is described in the next section.

### Authorization
Now, click or tap the RestAPI docs :octicons-link-external-16: link to open the documentation in a new window. The API docs are fully interactive, meaning you may test any of the available endpoints and receive a valid server response. Begin by choosing the green **Authorize &nbsp;:fontawesome-solid-lock:** button, shown below:

![restapi-docs](https://github.com/RaspAP/raspap-webgui/assets/229399/f5a1bd5d-8dda-4b94-96e5-94f159a2b85c){: style="width:520px"}

This will open a dialog where you may enter your API key, which will be passed as an `access_token` in the HTTP request header. Paste the key you created in the previous step into the "Value" text field and choose the **Authorize** button: 

![restapi-dialog](https://github.com/RaspAP/raspap-webgui/assets/229399/28023ea4-428a-49db-ad3e-3575ff109582){: style="width:520px"}

At this stage, the dialog should indicated "Authorized". Dismiss the dialog by choosing **Close**. You may now proceed with testing the API interactively.

## Testing endpoints
With authorization done, you may test any of RaspAP's available RestAPI endpoints. Start with the first available `/system` (Get System) endpoint. Click or tap anywhere in this endpoint's header area and choose the **Try it out** button. This endpoint takes no parameters, so you may simply use the **Execute** button to query the API. An example client request and corresponding server response are shown below.

### Client requests
Here, we can see a `curl` `GET` command with the `-H` (header) option used to specify the `access_token` and the API key as the value. The request URL in this example is `http://raspberrypi.local:8081/system` (yours may differ):

```
curl -X 'GET' \
  'http://raspberrypi.local:8081/system' \
  -H 'accept: application/json' \
  -H 'access_token: o2eycsnwzacgcukkdkxulmvcva7hou5q'
```


### Server responses
The `/system` API endpoint responds to the above request with several key pieces of data in JSON format:

```
{
  "hostname": "raspberrypi",
  "uptime": "up 23 hours, 2 minutes",
  "systime": "Sun 10 Mar 11:11:11 CET 2024",
  "usedMemory": 35.46,
  "processorCount": 4,
  "LoadAvg1Min": 0.14,
  "systemLoadPercentage": 3.5,
  "systemTemperature": 46.16,
  "hostapdStatus": 1,
  "operatingSystem": "Debian GNU/Linux 12 (bookworm)",
  "kernelVersion": "6.1.0-rpi4-rpi-v8",
  "rpiRevision": "Pi 3 Model B"
}
```

The `hostapdStatus` indicates the current state of the Linux `hostapd` service, which provides the AP or hotspot. You may copy this data to the clipboard or download it from the test console, if you wish.

## Systemd service
During the RestAPI [installation](../features-experimental/restapi.md#installation), the Python modules installed by `pip` are stored in the current user's home directory. For the default `pi` user in Raspberry Pi OS, this path is `/home/pi/.local/bin`. In order for the `uvicorn` module to be found by Python, the `systemd` service control file specifies the `pi` user.

If your current user is something other than `pi`, edit the control file with:

```
sudo nano /lib/systemd/system/restapi.service
```

Modify the `User` line to reflect your current user, if necessary:

``` py hl_lines="6"
[Unit]
Description=raspap-restapi
After=network.target

[Service]
User=pi
WorkingDirectory=/etc/raspap/api
LimitNOFILE=4096
ExecStart=/usr/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 8081
ExecStop=/bin/kill -HUP ${MAINPID}
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

Save and exit the file, then reload the daemon with `sudo systemctl daemon-reload`.

## Docker support
The RestAPI is installed by default in RaspAP's [Docker container](../get-started/docker.md). This includes configuration of port `8081` used by the server to respond to client requests. Note that the API is also exposed on your system's WAN interface.

## Troubleshooting
The current status of the `restapi.service` is available on the **RestAPI > Status** tab. This is generally the best starting point when diagnosing common problems, such as authorization errors. Note that the service records the most recent API queries, including the requesting IPv4 client address:

```
raspberrypi python3[3033]: INFO: 192.168.0.102:58844 - "GET /clients/wlan0 HTTP/1.1" 200 OK
```

If a remote client is using an invalid API key, for example, this will appear as a `403 Forbidden` server response in the **Status** console. A successful response, like the one above, will return a `200 OK` code.

You may also obtain journal entries from the service by executing `journalctl -xeu restapi.service` from the shell.

## Discussions
Questions or comments about using the RestAPI? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).
