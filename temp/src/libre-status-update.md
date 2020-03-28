Title: Libre Status Update
Date: 2012-12-28 20:05
Author: mongrol
Category: The Skreegs
Tags: Free Software, Open Source, Parabola GNULinux
Slug: libre-status-update

While I'm a Free Software Activist and want to get more involved I
certainly don't practise 100% what I preach. I have the following
devices in my home.

-   1 Windows Netbook - It's Hazel's and will be replaced when it dies
-   1 Debian Wheezy Desktop - It has and AMD gfx card and runs binary
    firmware. It also contains various binary games. I think the only
    binary applicaiton on it is flash.
-   1 Lenovo x121 with Arch Linux. Also contains games and runs binary
    firmware for the Intel wifi card.
-   1 Mythbuntu server - Not sure what binaries are on this. Likely not
    many.
-   1 Mythbuntu Zbox id11 - Serves as a myth front end. Will be running
    nVidia binary blobs for VDPAU acceleration.
-   Nokia N900 and Sony Xperia Mini - Typical smartphone firmwares.

So we're not doing very well there. I've started raising the bar by
converting the laptop, which I do most gamedev on and play games, to
[Parabola GNU/Linux][]. This is a free distro based on Arch and is very
easy to migrate to on any machines already running Arch. My first step
was to find and install a Mini-PCIE Wifi card that doesn't need binary
firmware. Ebay was very helpful here and I obtained an Atheros card for
buttons. Once installed it's simply a case of following the Parabola
migration guide, installing Parabola repos, doing a pacman -Syyu to
update and then remove any binary packages that there doesn't exist a
free equivalent for. I only lost a couple of packages I wasn't even
using.

I then needed to do some grub tweaking to enable my LUKS encrypted
rootfs and I'm up and running. No games to play but no closed software
other than my UEFI bios.

  [Parabola GNU/Linux]: http://www.parabolagnulinux.org
