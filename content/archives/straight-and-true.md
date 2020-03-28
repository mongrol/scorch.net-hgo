---
Title: "Straight And True"
Date: 2012-07-19
Author: "mongrol"
Categories: ["Traction Edge"]
---

I was fairly quick getting Dijkstra maps in for path finding but still
found my monsters taking round about paths to get to targets. Exactly
the same as my old code. It took an infuriatingly long time to fix as
well. The problem was I was calculating every tile around the centre
tile including the diagonals instead of just the orthagonal neighbours.
The result was a steeper slope on the diagonals and gentler on orthos.

I can't see why it makes a difference even after doing it in a
spreadsheet and staring at it for most of a flight back from Melbourne.
A tweak to code later and now my AI is straight and true. They run right
up and hit you in the face without all the silly dancing around they've
been doing for over a year. :)

Next, some aggression traits and fleeing and I'll be happy to move onto
Item progression.
