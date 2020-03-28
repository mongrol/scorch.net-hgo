---
Title: "Level Level"
Date: 2012-03-16
Author: "mongrol"
Categories: ["Traction Edge"]
---

I've been meaning to do a post on my programming mistakes with Traction
Edge since I started. I'll do it soon but one item that will be in the
list bit me on the bum yesterday. Because I'm such a genius, my Creature
class has all it's attributes as int's instead of in a std::map. I've
always had the thought this was a bad idea every time I added another
attribute and it finally bit me when I tried to do the UI for level up.

When you level up you get an point to spend on strength, dexterity or
intelligence. The UI needs to be able to iterate over these to select
one to upgrade. Ever tried iterating over something that's not in a list
or a map? It doesn't work very well. So basically I need to move all
these into an attribute map and then refactor every little bit of code
that's accessing these directly. There's another mistake. They're all
public and not accessed through proper accessors.

So the next release will be without levelling up, which isn't a big
issue yet since there's so much content still missing. I've also got
some more sensible level population code in and have a couple of sticky
AI bugs to fix and we're out! Yay!
