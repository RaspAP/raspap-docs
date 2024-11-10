# Custom user plugins

## Overview
RaspAP's `PluginManager` provides a framework for developers to create custom plugins to extend its functionality. To facilitate this, the `SamplePlugin` [repository](https://github.com/RaspAP/SamplePlugin) exists to give developers an entry point into creating their own plugins. Getting started with the `SamplePlugin` is described in the following sections.

## The SamplePlugin
The `SamplePlugin` implements a `PluginInterface` and is automatically loaded by RaspAP's `PluginManager`. 

![sample-plugin](https://github.com/user-attachments/assets/5a6ecf40-2b14-4502-8b63-5e85f9ade6f6){: style="width:420px"}


Several common plugin functions are demonstrated in `SamplePlugin`, as well as a method for persisting session data in plugin instances. Each plugin has its own namespace, meaning that classes and functions are organized to avoid naming conflicts. Plugins are self-contained and render templates from inside their own `/templates` directory.

## Getting started
The `SamplePlugin` requires an installation of RaspAP, either via the [Quick install](quick.md) method or with a [Docker container](docker.md). The default application path `/var/www/html` is used here. If you've chosen a different install location, substitute this in the steps below.

1. Begin by creating a fork of the [SamplePlugin repository](https://github.com/RaspAP/SamplePlugin).
2. Change to your RaspAP install location and create a `/plugins` directory.
   ```
   cd /var/www/html
   sudo mkdir plugins
   ```
3. Change to the `/plugins` directory and clone your `SamplePlugin` fork:
   ```
   cd plugins
   sudo git clone https://github.com/[your-username]/SamplePlugin
   ```
4. The `PluginManager` will detect and autoload the plugin. A **:fontawesome-solid-plug: Sample Plugin** item will appear in the sidebar.
5. Proceed with customizing your plugin by using the tips in the next sections.

## Scope of functionality
The `SamplePlugin` implements the server-side methods needed to support basic plugin functionality. It initalizes a `Sidebar` object and adds a custom navigation item. User input is processed with `handlePageAction()` and several common operations are performed, including:

1. Saving plugin settings.
2. Starting a sample service.
3. Stopping a sample service.

Template data is then collected in `$__template_data` and rendered by the `main.php` template file located in `/templates`. Property get/set methods are demonstrated with `apiKey` and `serviceStatus` values. A method is then used in `persistData()` to save the `SamplePlugin` object data.

!!! warning "Caution"
    Importantly, `SamplePlugin` does _not_ use the PHP `$_SESSION` object. Known as a "superglobal", or automatic global variable, this is available in all scopes throughout a script. Using the `$_SESSION` object in a plugin context can lead to conflicts with other plugin instances.

On the front-end, Bootstrap's [form validation](https://getbootstrap.com/docs/5.3/forms/validation/) is used to validate user input. A custom JavaScript function is used to generate a random `apiKey` value. The `sample.service` LED indicator is functional, as are the service stop/start form buttons.

## Customizing
The `SamplePlugin` demonstrates basic plugin functions without being overly complex. It's designed with best practices in mind and made to be easily modified by developers.

### Unique plugin names
Most plugin authors will probably begin by renaming `SamplePlugin` to something unique. The `PluginManager` expects the plugin folder, file, namespace and class to follow the same naming convention. When renaming the `SamplePlugin` ensure that each of the following entities uses the same plugin name:


|  Entity                                          |   Type     |
|--------------------------------------------------|------------|
| `plugins/SamplePlugin`                           | folder     |
| `plugins/SamplePlugin/SamplePlugin.php`          | file       |
| `namespace RaspAP\Plugins\SamplePlugin`          | namespace  |
| `class SamplePlugin implements PluginInterface`  | class      |

That is, replace each occurrence of `SamplePlugin` with your plugin name in these entities.

### Plugin logic and templates
Plugin classes and functions are contained in `SamplePlugin.php`. The parent template `main.php` and child tab templates are used to render template data. 

```
├── SamplePlugin/
│   ├── SamplePlugin.php
│   └── templates/
│       ├── main.php
│       └── tabs/
│           ├── about.php
│           ├── basic.php
│           └── status.php
```

You may wish to omit, modify or create new tabs. This is done by editing `main.php` and modifying the contents of the `/tabs` directory.

### Sidebar item
The `PluginInterface` exposes an `initalize()` method that is used to create a unique sidebar item. The properties below can be customized for your plugin:

```
$label = _('Sample Plugin');
$icon = 'fas fa-plug';
$action = 'plugin__'.$this->getName();
$priority = 65;
```

You may specify any icon in the [Font Awesome 6.6 free library](https://fontawesome.com/icons) for the sidebar item. The priority value sets the position of the item in the sidebar (lower values = a higher priority).

### Permissions
For security reasons, the `www-data` user which the `lighttpd` web service runs under is not allowed to start or stop daemons or execute commands. RaspAP's installer adds the `www-data` user to [sudoers](https://www.sudo.ws/about/intro/), but with restrictions on what commands the user can run. If your plugin requires execute permissions on a Linux binary not present in RaspAP's [sudoers file](https://github.com/RaspAP/raspap-webgui/blob/master/installers/raspap.sudoers), you will need to add this yourself. To edit this file, the `visudo` command should be used. This tool safely edits `sudoers` and performs basic validity checks before installing the edited file.

Execute `visudo` and edit RaspAP's sudoers file like so:

```
sudo visudo /etc/sudoers.d/090_raspap
```

An example of adding entries to support a plugin's service is shown below:

```
www-data ALL=(ALL) NOPASSWD:/bin/systemctl start sample.service
www-data ALL=(ALL) NOPASSWD:/bin/systemctl stop sample.service
www-data ALL=(ALL) NOPASSWD:/bin/systemctl status sample.service
```

Wildcards ('`*`') and regular expressions are supported by `sudoers` but [care should be taken when using them](https://www.sudo.ws/posts/2022/03/sudo-1.9.10-using-regular-expressions-in-the-sudoers-file/).

## Multiple instances
The `PluginManager` is a managerial class responsible for locating, instantiating and coordinating plugins. Through the use of namespaces and object data persistence in `SamplePlugin`, any number of user plugins may be installed to `/plugins` and run concurrently.

![multiple-plugins](https://github.com/user-attachments/assets/2d156efe-8cfc-49e7-b682-219d2db4eeee){: style="width:640px"}

As previously noted, developers should avoid using PHP's `$_SESSION` object in their plugins to prevent conflicts with other plugin instances. An alternative method for session data storage is provided in the `SamplePlugin` `persistData()` function. 

!!! note "Note"
    The `persistData()` function writes serialized data to the volatile `/tmp` directory which is cleared on each system boot. For this reason, it should not be used as a permanent method of data persistence. However, this functionality roughly approximates PHP's `$_SESSION` object; the difference being that each plugin's data is isolated from other plugin instances.


## Publishing your plugin
The `SamplePlugin` contains an "About" tab where you may provide author information, a description and link to your project. If you've authored a plugin you feel would be useful to the RaspAP community, you're encouraged to share it in the `SamplePlugin` repository's [discussions](https://github.com/RaspAP/SamplePlugin/discussions). 

## Discussions
Questions or comments about creating user plugins? Join the [discussion here](https://github.com/RaspAP/raspap-webgui/discussions/).
