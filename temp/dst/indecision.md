---
Title: "Language Indecision"
Date: 2014-01-14
Tags: ["tractionedge"]
---

I feel like moving back to Love2d and Lua. Nothing wrong with Python as such
and I still prefer that over Lua but the pysdl2 has some issues. Let's do a procon.

**Python/PySDL**

Cons;

* It's relatively low level. Even to do something as simple as scaling or rotating
 forces you to dive down into SDL itself. 
* No community. The pygame community doesn't count.
* SDL docs are terrible. Really.
* Nowhere near as feature rich as Love2d.
* Harder to package and distribute games
 
Pros;

* Python is preferred as it benefits my career
* SDL is big, popular and not going away any time soon
* More cross platform targets (not that I care much about this)
* Easier to switch to 3d engine e.g. Panda3d
  
**Love2d/Lua**
  
Cons;

* Lua is lower level than Python. Most structure as missing and need to be
 implemented yourself or via a library e.g. Classes etc.
* It's not python and doesn't benefit my career
* There's something less verbose about it compared to Python.
* Difficult to swap engine out for a 3d one.
 
Pros;

* Love2d is feature rich and fast.
* Loads of libraries for every kind of feature you'd want in a game.
* Vibrant community
* Active development.
 
 From that list it looks like a no brainer but for 2 things. As an Infrastructure
 Enterprise Architect for a firm entering the devops era bigtime, python 
 contributed directly to my career. Lua only contributes as programming
 practise, however, they are very similar and if needed to, I could switch
 back to Python with ease.

There's something else about Lua that I don't like. The syntax of control
structures, the need to drill into libraries when reading others code to 
make sure I understand how this guy's written his class implementation
this time, the available documentation is a bit thin on the ground and I don't
like the way the current manuals are written.

Oh bugger it. Lua/Love2d it is. :)
