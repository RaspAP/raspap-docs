# Docker support

![](https://github.com/RaspAP/raspap-docker/assets/229399/e2adcee8-2f7d-490c-8d37-7a705bb5a320){: style="width:480px"}

## Overview
As an alternative to the [Quick installer](quick.md) or [manual installation](manual.md) steps, you may also deploy RaspAP in an isolated and portable **Docker** container.

A **container** is an isolated environment for code. This means that a container has no knowledge of the host operating system, dependencies, or its files. It runs on the environment provided to you by either Docker Desktop or the Docker Engine. Containers have everything needed to run an application, down to a base operating system.

Here, we'll focus on using [Docker Engine](https://docs.docker.com/engine/) to deploy and manage a [containerized RaspAP](https://github.com/RaspAP/raspap-docker) application stack.

## Why a container?
Docker containers have several advantages over other methods of deploying code. As a [sandboxed](https://en.wikipedia.org/wiki/Sandbox_(software_development)) process, containers are isolated from all other processes running on a host machine. That isolation leverages things like [kernel namespaces and cgroups](https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504), features that have been in Linux for a long time.

A RaspAP Docker container is a runnable instance of an image. This container can be started, stopped, moved or deleted using the [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/). It can be run on a local device, virtual machines or deployed to the cloud. Isolation from other containers also means that it runs its own software, binaries and so on.

## Installing Docker Engine
Since RaspAP is built for Debian-based systems, the instructions here will focus on this OS family. To get started with Docker Engine on Debian, make sure you meet the [prerequisites](#prerequisites), and then follow the [installation steps](#install-using-the-apt-repository).

### Prerequisites
To install Docker Engine, begin with the 64-bit version of one of these Debian versions:

- Debian Bookworm 12 (stable)
- Debian Bullseye 11 (oldstable)

Docker Engine for Debian is compatible with x86_64 (or amd64), armhf, arm64, and ppc64le (ppc64el) architectures.

### Uninstall old versions
Before installing Docker Engine, we must first uninstall any conflicting packages.

Distro maintainers provide unofficial distributions of Docker packages in their repositories. These packages must be uninstalled prior to installing the official version of Docker Engine.

The unofficial packages to uninstall are:

- `docker.io`
- `docker-compose`
- `docker-doc`
- `podman-docker`

Run the following command to uninstall these packages and their dependencies:

```
for pkg in docker.io \
    docker-doc \
    docker-compose \
    podman-docker \
    containerd \
    runc; do \
    sudo apt-get remove $pkg;
done
```

!!! note "Note"
    `apt-get` might report that you have none of these packages installed.

### Install using the convenience script

Docker provides a convenience script at [https://get.docker.com/](https://get.docker.com/) to install Docker non-interactively. Prior to executing it, be sure to familiarize yourself with the potential [risks and limitations](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script) associated with this script.

!!! tip "Tip"
    You can run the script with the `--dry-run option` to learn what steps the script will run when invoked:
    ```
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh ./get-docker.sh --dry-run
    ```

1. Begin by changing into your home directory, then download and execute the convenience script to install the latest stable release of Docker:
```
cd ~/
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
2. Verify that the installation is successful by running the `hello-world` image:
```
sudo docker run hello-world
```
This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits. The output should appear similar to the example below:
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
478afc919002: Pull complete
Digest: sha256:4bd78111b6914a99dbc560e6a20eab57ff6655aea4a80c50b0c5491968cbc2e6
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

You have now successfully installed and tested Docker Engine. The docker service starts automatically on Debian based distributions.

!!! note "Note"
    If the test container fails to run or you encounter any errors, refer to the [Docker Engine](https://docs.docker.com/engine/install/troubleshoot/) documentation for troubleshooting tips.

### Post-installation steps
The Docker daemon binds to a Unix socket, not a TCP port. By default it's the `root` user that owns the Unix socket, and other users can only access it using `sudo`. The Docker daemon always runs as the `root` user.

If you don't want to preface the `docker` command with `sudo`, create a Unix group called `docker` and add users to it. When the Docker daemon starts, it creates a Unix socket accessible by members of the `docker` group.

To create the `docker` group and add your user:

1. Create the docker group.
```
sudo groupadd docker
```
2. Add your user to the `docker` group.
```
sudo usermod -aG docker $USER
```
3. Log out and log back in so that your group membership is re-evaluated.

With these steps completed, you have successfully installed and started Docker Engine. We're now ready to deploy RaspAP.

## Deploying RaspAP
With Docker Engine installed, you have two ways of deploying RaspAP in a Docker container. Each of these methods is described in the sections below.

### Using Docker compose
This method lets us deploy the entire RaspAP application stack with a single command (`docker-compose up`) as well as configure things like environment variables, network settings and so on in a centralized manner. Advanced users may also use this option to define a multi-container environment of which RaspAP is one component. This may be done with the `docker-compose.yml` file.

Begin by cloning the `raspap-docker` [GitHub repository](https://github.com/RaspAP/raspap-docker) into your home directory, then change into it:

```
cd ~/
git clone https://github.com/RaspAP/raspap-docker.git
cd raspap-docker
```

For ARM devices, such as the Raspberry Pi, we must uncomment the `cgroup: host` line in the `docker-compose.yaml` file:

``` py hl_lines="9"
version: "3.8"
services:
  raspap:
    container_name: raspap
    image: ghcr.io/raspap/raspap-docker:latest
    #build: .
    privileged: true
    network_mode: host
    cgroup: host # uncomment when using an ARM device 
    cap_add:
      - SYS_ADMIN
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
    restart: unless-stopped
```

Edit this file with `nano docker-compose.yaml`, change the line to appear as above, then use ++ctrl+o++ and press ++enter++ to save and exit the file.

!!! warning "Important"
    Do not use `docker-compose` but rather `docker compose`. If the latter isn't present on your system, refer to Docker's [installation steps](https://docs.docker.com/compose/install/).

With this configuration done, execute Docker compose like so:

```
docker compose up -d
```

You should see output similar to below to indicate the progress of RaspAP's Docker image being built: 

```
docker compose up -d
[+] Running 2/8
 ⠇ raspap 7 layers [⠀⡀⣿⣿⠀⠀⠀] 12.83MB/337.8MB Pulling
   ⠋ 5665c1f9a9e1 Downloading [===>                        ]  3.547MB/49.59MB
   ⠋ 4311202aff18 Downloading [=========>                  ]   4.98MB/24.95MB
   ✔ ac4d205394f0 Download complete
   ✔ baf57b850085 Download complete
   ⠋ 18a1ed9b4ba8 Downloading [=>                          ]  4.307MB/263.3MB
   ⠋ 5bed08c889b9 Waiting
   ⠋ 09ed3fdeed88 Waiting
```

During this process, a Docker image containing RaspAP's application stack will be created on your system. This build always pulls the [latest RaspAP release](https://github.com/RaspAP/raspap-webgui/releases/latest) from the main [GitHub repository](https://github.com/RaspAP/raspap-webgui/). 

Behind the scenes, Docker has used the image it created to start a containerized RaspAP application stack. You may confirm this by executing the following:

```
docker container ls
CONTAINER ID   IMAGE           COMMAND                  CREATED        STATUS        PORTS     NAMES
8d7b32b8373a   raspap:latest   "/bin/bash -c '/home…"   2 hours ago    Up 2 hours             raspap
```

At this stage, the RaspAP application is running and you may access the web interface as you would normally. This will depend on the method you use to access your device, but is usually one of the following:

- `http://raspberrypi.local`
- `http://10.3.141.1`
- `http://localhost`

Take note that RaspAP and all its dependencies are wholly contained within the running Docker container. That is, the host system does not have any of the `apt` packages or application files used by RaspAP, unless you've explicitly installed them.

### Using the container registry
As an alternative to `docker compose`, described above, you may also deploy RaspAP using its hosted Docker container image. This is available as a `raspap-docker` package hosted on the [GitHub Container registry](https://ghcr.io/). With this method, a single container is defined from its base image, the environment is setup and the application is configured within the container.

Given that everything needed to deploy RaspAP is stored within this package, it isn't necessary to clone the `raspap-docker` respository. Instead, you may simply execute one of the following `docker run` commands:

1. For ARM devices, the `cgroups` must be made writable.
```
docker run --name raspap -it -d --privileged --network=host --cgroupns=host -v /sys/fs/cgroup:/sys/fs/cgroup:rw --cap-add SYS_ADMIN ghcr.io/raspap/raspap-docker:latest
```
2. For non-ARM devices, execute the following.
```
docker run --name raspap -it -d --privileged --network=host -v /sys/fs/cgroup:/sys/fs/cgroup:ro --cap-add SYS_ADMIN ghcr.io/raspap/raspap-docker:latest
```

With either of the above commands, you should see output as below followed by progress indicating the state of the various package components as they are downloaded to your system:

```
Unable to find image 'ghcr.io/raspap/raspap-docker:latest' locally
latest: Pulling from raspap/raspap-docker
```

When the container image download is completed, you may verify its operational state like so:
```
docker container ls
CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS          PORTS     NAMES
4257b8aa3c7e   ghcr.io/raspap/raspap-docker:latest   "/bin/bash -c '/home…"   32 minutes ago   Up 32 minutes             raspap
```

At this stage, the RaspAP application stack is running and you may access the web interface as you would normally. This will depend on the method you use to access your device, but is usually one of the following:

- `http://raspberrypi.local`
- `http://10.3.141.1`
- `http://localhost`

Take note that RaspAP and all its dependencies are wholly contained within the running Docker container. That is, the host system does not have any of the `apt` packages or application files used by RaspAP, unless you've explicitly installed them.

## Tips and tricks
The following section has some general advice that users of RaspAP's Docker container have found useful. If you have a tip or trick to contribute, feel free to join our [discussions](#discussions). 

### Allocating a terminal
While RaspAP's Docker container is running, you may obtain an interactive pseudo-TTY, or Linux terminal, connected to standard input. Do so by executing the following:

```
docker exec -it raspap bash
```

The above command combines the `-i` (interactive) and `-t` (tty) options together with the `raspap` named container. The `bash` command starts an interactive Bash shell within the running container. From here you can perform most of the same shell operations and commands within Docker's pseudo-TTY as you would in a regular Linux environment. 

### iptables rules and NAT
With either of the above methods, `iptables` [Network Address Translation (NAT) rules](https://github.com/RaspAP/raspap-docker/blob/master/firewall-rules.sh) will automatically be applied on the Docker host. It's necessary to add these rules on the host device due to Docker's network isolation and security defaults.

If your host's network interfaces are anything other than `wlan0` and `eth0`, you may customize [these rules](https://github.com/RaspAP/raspap-docker/blob/master/firewall-rules.sh) to suit your own specific needs. After editing this file on your device, set execute permissions and run it like so:

```
sudo chmod +x firewall-rules.sh
./firewall-rules.sh
```

### Installer options
The goal of the initial Docker rollout for RaspAP is to have a "one shot" command to get a container up quickly with minimal user input. For this reason, the RaspAP application stack is installed with some common options enabled by default. These optional components are [Ad blocking](adblock.md), [OpenVPN](openvpn.md) and [WireGuard](wireguard.md).

You may change this behavior by removing any or all of the [Quick installer](quick.md) flags from RaspAP's [Dockerfile](https://github.com/RaspAP/raspap-docker/blob/master/Dockerfile). For example, to skip the WireGuard install option, remove the `--wireguard 1` flag on the line below:

``` py hl_lines="2" 
RUN apt update && apt install -y sudo wget procps curl systemd iproute2 && rm -rf /var/lib/apt/lists/*
RUN curl -sL https://install.raspap.com | bash -s -- --yes --wireguard 1 --openvpn 1 --adblock 1
COPY firewall-rules.sh /home/firewall-rules.sh
RUN chmod +x /home/firewall-rules.sh
CMD [ "/bin/bash", "-c", "/home/firewall-rules.sh && /lib/systemd/systemd" ]
```

With this done, you may proceed with building your Docker image as usual. 

!!! note "Note"
    Alternatively, you may choose to install these optional components and disable them in RaspAP's [configuration file](defaults.md#managing-config-values), `config.php`.

## Troubleshooting
The `docker logs` command shows information logged by a running container and is generally the best starting point for troubleshooting. To obtain logs for the `raspap` container, execute `docker logs raspap`.

The Docker daemon logs may also help you diagnose problems. Use the command `journalctl -xu docker.service` (or read `/var/log/syslog` or `/var/log/messages`, depending on your Linux Distribution).

For issues related to Docker Engine, refer to [Docker's troubleshooting](https://docs.docker.com/engine/install/troubleshoot/) section.

## Discussions
Questions or comments about using RaspAP's Docker container? Join the [discussions here](https://github.com/RaspAP/raspap-docker/discussions/).

