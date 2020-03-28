Title: VPS gone
Date: 2013-10-30 21:53
Tags: raspberrypi
Slug: vps gone
Author: mongrol
Category: The Skreegs

I've now knocked up my other Raspberrypi Model B as a web server to replace
my slowing VPS. It's performing way better than I expected. I've set it up with
Lighttpd, Postgresql and enabled php-apc to cache php. Php-apc is giving a 
reasonable speedup of around 30%. The Pi is serving tt-rss external over https,
using a server cert from [cacert.org](www.cacert.org). It's also running dokuwiki
which basically gets no action.

Really must back it up at some point. Pi's eat sdcards for breakfast. I've also just
received my [Cubietruck](www.cubieboard.org). For some chinese tat I'm very
impressed. More on this once I find a power supply that can run it. 

