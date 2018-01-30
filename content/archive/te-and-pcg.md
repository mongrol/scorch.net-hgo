Title: TE and PCG
Date: 2011-12-30 03:42
Author: mongrol
Category: Traction Edge
Tags: Traction Edge
Slug: te-and-pcg

I'm now plugging away at procedural maps. Maps are created for
"scenarios", e.g. Farm, Village, City, Dungeon etc. With custom code for
each without obvious reuse where possible. Buildings are then generated
and placed into the map where there is space. Finding space is the
tricky part. At first I attempted using a BSP to divide the space up.
This proved too hard as to cater for different sized buildings I had to
traverse an overlapping map of "nodes' that may or may not have
buildings in there children. When I started thinking about all the nice
bits like, paths, road, rivers etc I just knew this would be a nightmare
going forward.

I've now went for a more UFO style approach by dividing the map up into
squares and placing a building in each. UFO had 10x10 squares. I've gone
for 5x5 in the hope it can give a bit more granular feel to it. I've got
the basics down and need to work on handling buildings that take up more
than 1 square. Then its back into the building code to work on randomly
generating interesting builds for each scenario.

Then I get to do the fun stuff of fitting it all together, placing
rivers and roads and making sure it all looks decent.
