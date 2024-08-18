# Quick installer

## Overview
The Quick installer has been designed to assist users with creating an instance of RaspAP both quickly and with a great deal of flexibility.
The [install loader](https://github.com/RaspAP/raspap-webgui/blob/master/installers/raspbian.sh) will respond to several command line arguments, or [switches](#switches), to customize your installation in a variety of ways, or install one of RaspAP's optional [helper](minwrite.md) [tools](ssl.md).

## Alternatives
The installer gives you the greatest level of flexibility for creating an instance of RaspAP. However, if your goal is to use RaspAP as a component of a larger project, or wish to isolate its dependencies from existing software on your system, consider deploying RaspAP in a [Docker container](docker.md) instead.

## Usage
The [Quick installer](https://github.com/RaspAP/raspap-webgui/blob/master/installers/raspbian.sh) has several options for configuring a RaspAP installation. You can get usage notes from your command shell by requesting the installer like so:

```
curl -sL https://install.raspap.com | bash -s -- --help
```

Appending `-s -- [option]` to the Quick Install directive will activate one or more options. Several options may be chained together to customize an installation. Examples are given below.

## Examples
The installer may be invoked locally or remotely via `curl`. Examples with both cases and various options are given below.

Invoke installer remotely, run non-interactively with option flags:
```
curl -sL https://install.raspap.com | bash -s -- --yes --wireguard 1 --adblock 0
```

Invoke remotely, uprgrade an existing install to the [:octicons-heart-fill-24:{: .heart }  Insiders Edition](insiders.md). The `--name` and `--token` arguments are optional; if they are not specified the user will be prompted to authenticate with GitHub:
```
curl -sL https://install.raspap.com | bash -s -- --upgrade --insiders --name <name> --token <token>
```

Invoke remotely, perform an unattended update to the latest release version:
```
curl -sL https://install.raspap.com | bash -s -- --yes --update --path /var/www/html
```

Run locally specifying a GitHub repo and branch:
```
raspbian.sh --repo foo/bar --branch my/branch
```

Run locally requesting release info:
```
raspbian.sh --version
```

## Switches

#### -y, --yes, --assume-yes
This option enables unattended installations, such that the installer assumes "yes" as an answer to all user prompts. This behavior is identical to how the same option with the `apt-get` package handler works. 

#### -c, --cert, --certificate
This option installs an SSL certificate with `mkcert` and configures lighttpd for HTTPS support. It does _not_ (re)install RaspAP. Details are [provided here](ssl.md).

#### -o, --openvpn `<flag>`
Used with the `-y`, `--yes` option above, this sets the OpenVPN install option (`0` = don't install OpenVPN). Given that OpenVPN support is an optional extra, this enables an unattended setup without installing it.

#### -s, --rest, --restapi `<flag>`
Used with the `-y`, `--yes` option above, this sets RestAPI install option (`0` = don't install the RestAPI). Given that the RestAPI is an optional extra, this enables an unattended setup without installing it.

#### -a, --adblock `<flag>`
Used with the `-y`, `--yes` option above, this sets the Ad Blocking install option (`0` = don't install Adblock). Given that Adblock support is an optional extra, this enables an unattended setup without installing it.

#### -w, --wireguard `<flag>`
Used with the `-y`, `--yes` option above, this sets the WireGuard install option (`0` = don't install WireGuard). Given that WireGuard support is an optional extra, this enables an unattended setup without installing it.

#### -g, --tcp-bbr `<flag>`
Used with the `-y`, `--yes` option above, this enables kernel support for [TCP BBR congestion control](https://cloud.google.com/blog/products/networking/tcp-bbr-congestion-control-comes-to-gcp-your-internet-just-got-faster) (`0` = don't configure TCP BBR). Given that TCB BBR support is optional, this enables an unattended setup without enabling it.

#### -e, --provider `<value>`
Used with the `-y`, `--yes` option above, this sets the VPN provider install option. Valid numeric option values are:
```
  1 = ExpressVPN
  2 = Mullvad VPN
  3 = NordVPN
  0 = None
```

#### -r, --repo, --repository `<name>`
If you have forked this project to your own GitHub repo, this option lets you override the default GitHub repo (`RaspAP/raspap-webgui`) used to install RaspAP. An alternate repository name is a required parameter.

#### -b, --branch `<name>`
Similarly, this option overrides the default git branch. This is useful if you have created a feature branch (`my-feature`) and wish to perform an installation using the Quick Installer. An alternate branch name is a required parameter.

An example combining the `-r`, `--repo` and `-b`, `--branch` options is given below:
```
curl -sL https://install.raspap.com | bash -s -- --repo foo/bar --branch my-feature
```

#### -t, --token `<accesstoken>`
Specify a GitHub [personal access token](https://docs.github.com/en/authentication/) to authenticate with a private repository. Used together with the `-n`, `--name` option (below).

#### -n, --name `<username>`
Specify a GitHub username to access a private repository. An example combining the `--token` and `--name` options is given below:

```
curl -sL https://install.raspap.com | bash -s -- --name billz --token [my-token]
```

#### -u, --upgrade
Upgrades an existing RaspAP installation to the latest release version.

#### -d, --update
Performs a minimal update of an existing installation to the [latest release version](https://github.com/RaspAP/raspap-webgui/releases). This differs from the `-u`, `--upgrade` option in several ways. The user is not prompted to install optional RaspAP components, and several steps used for an initial installation are not performed. Existing configuration files remain intact.

#### -p, --path `<path>`
Sets the application path for an existing RaspAP installation. 

It may be combined with the `-d`, `--update` and `-y`, `--yes` options to perform an unattended update. An example is given below:

```
curl -sL https://install.raspap.com | bash -s -- --update --path /var/www/html --yes
```

#### -i, --insiders
Installs from the [:octicons-heart-fill-24:{: .heart }  Insiders Edition](insiders.md) (`RaspAP/raspap-insiders`).

#### -m, --minwrite
Configures a microSD card for [minimum write operation](minwrite.md).

#### -v, --version
Queries the Github API, outputs the latest RaspAP release version and exits.

#### -n, --uninstall
Loads and executes the uninstaller.

#### -h, --help
Outputs these usage notes and exits.

## Discussions
Questions or comments about using RaspAP's Quick installer? Join the [discussions here](https://github.com/RaspAP/raspap-webgui/discussions/).


