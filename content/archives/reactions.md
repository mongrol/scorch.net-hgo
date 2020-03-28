---
Title: "Reactions"
Date: 2011-03-25
Author: "mongrol"
Categories: ["Traction Edge"]
Tags: ["Traction Edge"]
---

An important feature of any XCom-a-like is opportunity fire, or reaction
fire. This means when you click to move your wee man and he starts
moving towards his destination, if an enemy see's him there's a chance
of the opposition getting a free shot at him, during your turn, if they
have action points and win some kind of initiative. This also means that
you can "save" points during your turn for possible reaction fire during
the enemies turn. Handy for setting up guard posts, ambushes, covering
fire etc.

Traction Edge though, doesn't use the point and click interface. It's a
roguelike so every turn step or action is a single keypress. While
implementing reaction fire I noticed how different this style of control
is to the usual point and click. In the traditional XCom's you click a
destination and the man moves towards it. If spotted on the way you're
man freezes and the enemy has a few pot shots. Basically he's stuck
there until the enemy decides he's done shooting at you.

In TE with the current RF(reaction fire) code you move onto a new tile,
enemy spots you and has a shot if it has AP (I'll implement initiative
later). You then get a chance to move again, if you're still alive and
again, the enemy gets his chance at RF. This means that instead of being
stuck to the spot until the enemy is finished you actually get to duck
and run, change direction, fire back, whatever during the RF.

It does need more fine tuning though. At present if enemies are already
visible then they still take reaction fire which doesn't seem quite
right. It quickly turns into a visible firefight from both sides when
really it should be your turn. I think RF should only be granted when an
previously unseen enemy comes into view. Not when they are already in
view.
