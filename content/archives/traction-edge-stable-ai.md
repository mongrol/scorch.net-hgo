---
Title: "Traction Edge: Stable AI"
Date: 2011-03-01
Author: "mongrol"
Categories: ["Traction Edge"]
Tags: ["Open Source, Traction Edge"]
---

My second iteration of TE's AI has finally reached some kind of
stability. It's the first draft of a fairly basic state machine with a
few bits of bandaid over my rushed code.

The FSM consists of Patrol state, Attack State and Run State. Each
state, during update will run an awareness update (process fov) then
make some decisions based on what it can see and also what the creatures
present condition is. Just now that consists of assessing whether it can
attack and reach safety in the same round. If not, just run for safety.
Once it reaches safety it returns to Patrol which consists of picking a
random point that's reachable and moving towards it until it's awareness
detects an enemy.

The switch from Safety to Patrol does cause some flickering in and out
of hiding places that's a bit unnatural but it's good enough just now.
It also present a decent challenge. The next iteration will have a more
complex behavior system and will soften the transitions.

Since the AI just now presents a usable enough enemy I'm going to jump
back into the guts of the RPG system and get some progress to make this
an actual game, rather than a tech demo.
