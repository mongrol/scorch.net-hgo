---
Title: "Traction Edge Design Mistakes #1"
Date: 2012-04-11
Author: "mongrol"
Categories: ["Traction Edge"]
---

Traction Edge is the one and only C++ program I've ever written. I
didn't start with Hello World. I just got in and started moving an @
around using SFML (then called EnemyX) and it just kept going from
there. Since my dev time is quite limited and games take a lot of
devtime, in order to get content in I follow this methodology.

1.  Implement idea using quick and dirty code with about 1 bus trips
    worth of thought into doing it properly and cleanly. That's about 30
    mins.
2.  Refactor that code the next time I encounter it. This can sometimes
    be either the following week or 12 months away.

This methodology, and my early lack of experience in C++ has led to some
rather glaring design mistakes in Traction Edge. Particularly when I
didn't encounter said code again for a number of months. Here's the
first of my big boobs.

**The Singleton Pattern**

By far my biggest mistake has been the singleton pattern. Initially I
fell into the trap of creating "Manager" classes. These are dubious at
best and frequently the newbie thinks they need only one of these, and
from that they produce a singleton instance of said beasts. Singleton's
are also easier to access from any class which also leads to class bloat
in these monsters as it's a handy place to just shove any old function
in. This in turn leads to bad design choices and a big lack of
separation of duty.

In Traction Edge my monster singleton is the GameWorld class. It's
purpose is to hold data of the world, levels and the players progression
through the game. Almost everything has their hooks into this class from
the GfxSFML.h class which draws the graphics to all the UI classes which
control input into states. It's just ridiculous and will be quite
difficult to unpick but as the codebase matures it's going to have to be
fixed at some stage.

What should be happening is the GameWorld is created by the Engine at
game start and a reference passed to whatever classes needs access to it
as the loop roles along. This ensures thought is given to what classes
need access to it when I'm writing code and better design is produced
more naturally.

I do have other singleton's as well but code has been cut down
significantly. DisplayManager is the interface to SFML and manages the
UI screens as they change from state to state. It's a tiny class and I
haven't touched it in 2 years and have no intention to. Sometimes I do
wonder why it exists at all.

Logger.h is also a singleton. This is a very common pattern though. Who
needs more than one logger? Since blah.h, which is implemented into my
Logger.h, can parse out to separate logs then I'm perfectly happy have a
singleton Logger.

SFML2.0 is due any time and at some point this year I'll be doing a
graphics engine refresh. I want layers and proper animation and I expect
this GameWorld monster will need to go before then.
