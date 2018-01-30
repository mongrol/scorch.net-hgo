Title: PCG Progress
Date: 2012-01-05 23:32
Author: mongrol
Category: Traction Edge
Tags: Traction Edge
Slug: pcg-progress

I've successfully switched my PCG code from the convoluted BSP code to
the much simpler map squares alah UFO(Xcom). The square size of 5x5
seems a nice fit too. I've also got masking in so buildings that don't
entirely fill the square simply overlay on top of the ground already
there.

I've decided buildings, instead of being procedurally generated will be
drawn statically and stored in a tilemap (Tiled to the rescue again).
This is much quicker and I can get more detailed buildings in easily. I
can always rotate them around to get some variety.

So next up. Draw some buildings. Get code in to handle buildings that
take up more than one square. Get weighted placement in so farms are in
the middle of the map.

 
