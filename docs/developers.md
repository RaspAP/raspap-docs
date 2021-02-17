# Developer tips

## Overview
There are as many different ways of developing software for single board computers, like the Raspberry Pi, as there are developers who do it. Likewise, opinions vary as to which approach is best.
Ultimately it's the process that works for best for you that prevails. This briefly describes two approaches used by contributors to RaspAP. 

## Remote host update
Project contributor [@glaszig](https://github.com/glaszig) maintains a working copy of RaspAP on his workstation and automatically copies changes over to the Pi.
He's written [this handy script](https://gist.github.com/glaszig/673691a6ba7bdc8e3d054d826a179976) to automate the process by way of `fswatch`. The script watches a local (dev) directory and pushes
changes to the remote target (the Pi, in this case) via `scp`, or secure copy. This way, you can use your preferred integrated development environment (IDE) and simply push updates in the background
to a remote system. More on fswatch [here](http://emcrisostomo.github.io/fswatch/).

An ancillary benefit with this method is that uncommitted changes to your local working copy are less vulnerable to being lost, in the event the remote system becomes inaccessible.
It is also less susceptible to potential 'over-the-wire' network latency issues.

## Direct access via terminal
If you're comfortable using a Linux-based text editor, developing directly on the Pi via the terminal is an alternate approach. This trades the IDE for Vim, Emacs or some other editor.
While these tend to have steeper learning curves, the upside is their extreme portability and universality. That is, human readable, plain-text configuration files for terminal programs (often called 'dotfiles') are generally much more portable than those for IDEs. 

![tmux + vim](https://pbs.twimg.com/media/EPX1B2AXkAA1oqy?format=jpg&name=small)
> [@billz's](https://github.com/billz) dev environment, via [Twitter](https://twitter.com/rasp_ap/status/1222152318503833601)

This means that you could, for example, save your dotfiles to GitHub and in effect "bring them with you" to whichever system you happen to be working on. The availability of Vim or Emacs is generally much greater than OS-specific IDEs, so in seconds (or at most a few minutes) you can setup your familiar dev environment. With the addition of [tmux](https://github.com/tmux/tmux/wiki), you can have multiple panes in a single terminal window. Here is an [excellent guide](https://www.lucasfcosta.com/2019/02/10/terminal-guide-2019.html) to getting started with the terminal.

