# Quick installer

## Overview
The installer has been designed to assist users with creating an instance of RaspAP both quickly and with a great deal of flexibility.
The install loader will respond to several command line arguments, or switches, enabling various features, upgrades or even installing from a forked version of RaspAP in another GitHub repository. 

## Usage
The [Quick installer](https://github.com/billz/raspap-webgui/blob/master/installers/raspbian.sh) has several options for configuring a RaspAP installation. You can get usage notes from your command shell by requesting the installer like so:

```
curl -sL https://install.raspap.com | bash -s -- --help
```

Appending `-s -- [OPTION]` to the Quick Install directive will activate one or more options. These are described below.

## Switches

#### -y, --yes, --assume-yes
This option enables unattended installations, such that the installer assumes "yes" as an answer to all user prompts. This behavior is identical to how the same option with the `apt-get` package handler works. 

#### -o, --openvpn `<flag>`
Used with the `-y`, `--yes` option above, this sets the OpenVPN install option (`0` = don't install OpenVPN). Given that OpenVPN support is an optional extra, this enables an unattended setup without installing it.

#### -a, --adblock `<flag>`
Used with the `-y`, `--yes` option above, this sets the Ad Blocking install option (`0` = don't install Adblock). Given that Adblock support is an optional extra, this enables an unattended setup without installing it.

#### -c, --cert, --certificate
This option installs an SSL certificate with `mkcert` and configures lighttpd for HTTPS support. It does _not_ (re)install RaspAP. Details are [provided here](https://github.com/billz/raspap-webgui/wiki/SSL-certificates-(Quick-Installer)). 

#### -r, --repo, --repository `<name>`
If you have forked this project to your own GitHub repo, this option lets you override the default GitHub repo (`billz/raspap-webgui`) used to install RaspAP. An alternate repository name is a required parameter. 

#### -b, --branch `<name>`
Similarly, this option overrides the default git branch (`master`). This is useful if you have created a feature branch (`my-feature`) and wish to perform an installation using the Quick Installer. An alternate branch name is a required parameter.

An example combining the `repo` and `branch` options is given below:
```
curl -sL https://install.raspap.com | bash -s -- --repo foo/bar --branch my-feature
```

#### -h, --help
Outputs these usage notes and exits.

#### -u, --upgrade
Upgrades an existing installation to the latest release version.

#### -v, --version
Queries the Github API, outputs the latest RaspAP release version and exits.
