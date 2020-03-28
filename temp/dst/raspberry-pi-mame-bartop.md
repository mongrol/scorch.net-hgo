---
Title: "Raspberry Pi Mame Bartop"
Date: 2012-08-07
Author: "mongrol"
Categories: ["The Skreegs"]
Tags: ["raspberrypi"]
---

I always wanted to build a MAME cabinet but the plan was to wait till
the kids were bigger and I had more time on my hands. Mame Cabs are
generally big, full sized things and have a full PC in them. Big, clunky
and expensive to build and run.

Enter the [RaspberryPi][]!

I'm now intending to build a bartop mame cabinet. Just big enough to fit
two people playing side by side so probably no bigger than a 17" screen.
It'll be easy to move it around, put it in a cupboard etc when not in
use and hide it from children when I don't want to damaged. :)

Here's the shopping list in AUD.

1x raspberrypi \$40  
1x powered USB Hub \$15  
1x 8GB Class 10 SDCard \$9  
1x EDUP Wifi Dongle \$10

That's the compute bit. Now the arcade bit.

1x Ultimarc mini-pac keyboard encoder \$50  
2x sticks \$30  
7x buttons (2 fire buttons per player, 1 + 2 player buttons and a coin
insert.

Then a screen from somewhere and some speakers as well. Haven't quite
planned that bit yet.

We then need a version of MAME to run on the Pi. There's a couple of
efforts underway, Advancedmame and RetroArch which uses iMame4All. Since
the Pi is a bit juice starved I'll aim for one that can run without X
and outputs directly to the framebuffer. OpenglES accel would be nice
too if possible.

I've currently got the pi hooked up with Galaxians running on Retroarch.
I can't see to get the keyboard working properly though. Early days.

  [RaspberryPi]: http://www.raspberrypi.org
