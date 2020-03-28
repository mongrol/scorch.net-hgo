---
Title: "MongCade Update"
Date: 2013-02-12
Author: "mongrol"
Categories: ["The Skreegs"]
Tags: ["raspberrypi"]
---

Roughly on schedule the final physical build is complete. It's turned
out very well with only the usual audio issues from advmame on the Pi.
Here's the parts list.

\* Raspberry Pi \$40  
\* Ultimarc miniPac keyboard encoder (\$60 delivered from USA)  
\* Powered USB hub from BigW (\$15)  
\* 2x Sticks \$34  
\* 8x buttons \$20  
\* 2x 1w Champ amplifier kits from Jaycar \$15  
\* 2x 8w speakers from Jaycar \$24  
\* Various cables/plugs/box etc from Jaycar \$20  
\* MDF from Bunnings \$60  
\* Vinyl from ebay \$8  
\* LG 1710B 17" monitor from somewhere over a decade ago.  
\* Edimax tiny wifi dongle \$11

In terms of software we have the following;  
\* Raspian (current)  
\* AdvanceMame 1.18? (whatever was before 1.20)  
\* AdvanceMenu for a frontend  
\* SDL DISPMANX backend (awesome!)

Config overview  
\* Pulseaudio removed (Poettering is a menace)  
\* 950Mhz overclock  
\* All software scaling disabled (DISPMANX does it for free)  
\* Advmenu and Advmame shortcuts tuned for UI goodness without a
keyboard.

Instead of the usual "get every rom from pleasesuredome" approach I've
decided to hand pick my games. Less games mean they get played more so
I'll start with those I loved playing as a teenager and also only run
ones that work well. Here's some pics

{% img /static/images/20130211_004.jpg 640 %}

{% img /static/images/20130211_0021.jpg 640 %}

While it's a bit busy under the panel with the minipac loom its actually
quite roomy at the back. The cabinet was designed in Blender to scale
and I'll post the .blend file shortly.
