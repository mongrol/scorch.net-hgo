---
Title: "Exiting The Cloud #4"
Date: 2011-02-17
Author: "mongrol"
Categories: ["The Skreegs"]
Tags: ["Open Source, Traction Edge"]
---

I've been angling towards self hosting over the last couple of days.
Firstly I just shrugged off the idea as being too much hassle, possibly
costly, difficult to maintain etc. The more I thought about it the more
I warmed to it though. I mean, all I need to do is poke some holes for
what I need (www only really) and make sure I have a proper backup. I'd
start off with SVN, move this blog there, integrated some video
streaming plugin for the clan to what kidlet videos and then think about
tackling mail. Job done. A Total Cloud Exit Event[tm].

**Exiting Google Code**

So this evening I've been wrestling with svnsync as I want my full
repository and history for TE and google code won't let me do a svnadmin
dump. 2 hours in I've actually got it working but now realised it's a
bit trickier than first thought. I need a hosted, local, on the wire SVN
so I can sync from the Mac and my Netbook. That means putting SVN hosted
on the server. Now this server is no ordinary server. It's the
BeanBox[tm] so called because Cooper uses it to watch Mr Bean. As in,
it's a MythTV media server. It's also running ancient technology, AGP
vid card, LGA775 P4. It also sits under the house next to the water
boiler and is frequently exposed to 30C+ for long periods. This box
breaks often and is the bane of my life.

So, in order to do any self hosting at all I need to do the MythTV
refresh I've been putting off in order to get some robustness to the
platform. This means splitting the Frontend off into a SFF unit of some
kind. Sticking that to the back of the telly allowing me to move the
backend server into the house downstairs where it belongs. I can then
hang some backup disk off it and give it cuddles or glaring looks when
it needs it.

This is where I start to spend money. A FrontEnd unit will probably skin
me \$300+ as I insist on silence in the living room. No Asrock or Zotac
nonsense here.

In the meantime I think I'll sync my repository to Sourceforge if I can.
