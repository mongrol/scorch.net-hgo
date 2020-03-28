---
Title: "UI Mistake Redux"
Date: 2012-04-16
Author: "mongrol"
Categories: ["Traction Edge"]
---

My last post berated my event loop and UI structure. I had a good old
look at it today and some reading and I'm not so sure I've got it wrong
after all. MVC means the view reacts to events and sends commands to the
controller. The controller then translates that into an order to change
the model.

In TE both my UI classes and my EngineState reacts to events so these
are essentially performing the View role. My monster GameWorld class is
doing the Controller role. All model data is modified through this
class. It's supposed to represent the Model but I've kinda squished the
controller into both UI and Gameworld class. Oh well. No dramas.
