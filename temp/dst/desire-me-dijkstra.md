---
Title: "Desire me Dijkstra"
Date: 2012-07-10
Author: "mongrol"
Categories: ["Traction Edge"]
---

The AI refresh is going great. I have some fantasy is my head about
ditching the state machine, which technically I have. The idea is to
update awareness of every loop, then update desires, and goals for those
desires,  based on that awareness. The final result is a djmap that the
monster just roles downhill on which is towards the strongest desire. On
the next step, we update our awareness and take an action if required.
This is where state machines creep back in.

My first thought was to update awareness, update desires then enter a
behaviour tree to perform an action. After I started coding this I
realised that updating desires, goals and choosing an action is
basically the same thing. Also surely only one desire can be the
strongest at any one time? If not, then two equally strong desires would
pull teh creature towards the closest one and now I've just written
then, seems like not such a bad thing. Still, having a dominant desire
still means we have a state machine. The current state is the dominant
awareness.

The big chunky bit is the processing of desires based on awareness. I
want to componentise this enough to allow me to develop different traits
for different creatures. I'd also like to avoid hardcoding values and
farm out AI traits to either xml or possibly even lua (eek, exciting!).
To reach this point I'll need to draft up some kind of abstraction layer
of what I want to feed values into. Wine threshold reached. I'll stop
typing now.
