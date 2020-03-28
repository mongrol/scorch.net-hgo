Title: Exiting The Cloud #3
Date: 2011-02-16 12:18
Author: mongrol
Category: The Skreegs
Tags: Open Source
Slug: exiting-the-cloud-3

So actually ignoring the cloud for the moment and returning to Kitten
Ranch. The primary offender onsite is our MacBook Pro. This, being the
main computer, was purchased and put in operation because "it just
works". After years of faffing around with Linux I wanted something
stable and good. Good it has been. It's fast, stable, Hazel mostly likes
it and it does it's job well. How far can we extract ourselves from it
though?

Locally I have the following critical functions being serviced by it;

-   Local email storage.
-   1.2GB of photo's - currently held in iPhoto
-   9GB of movies. Mostly home video in probably in .mov format
-   TE and Moolah development done in XCode - TE is cross platform but
    Moolah is pure Cocoa
-   Various artifacts from projects over the years.
-   Finance managment in jGnash.
-   Skype
-   Hazel uses it to plunder eBay, use email, Skype etc

So I'm tackling this lot very slowly. Firstly I've installed reFit and
dual booting Debian 6.0 (squeeze). After a bit of slapping I've got
Gnome looking pretty good and I'm quite impressed with the whole
package. It's very fast, stable so far and a lot easier to install than
I remember. It takes ages to boot though as I had to use LILO to get
past some 64bit reFIT/mbr issue. What about the above list?

-   Email was moved up to Fastmail and a copy imported into Thunderbird.
    Evolution just doesn't cut it. It's a UI disaster and Thunderbird is
    cross platform.
-   XCode is replaced with Geany. This is a lovely lightweight IDE with
    basic but good features. Since TE is part developed in VIM on a
    ArchLinux netbook then this was easy. Moolah however is now an
    abandoned project. How can I develop for a proprietary platform?
    This also means TE is now a Linux only game project. SFML 1.6
    (latest stable), which TE uses for graphics and input is also in
    Squeeze. Bonus!
-   jGnash is java but I had to dip into contrib and non-free to get the
    sun-java6-jre. I'm really trying to stay out of those repositories
    as much as possible. Finance Management sorted.
-   Movies - I'd sort of moved away from iMovie anyway as it just wasn't
    efficient and importing and converting to a youtube format (more on
    that later) so I expect I can find a suitable commandline way to do
    this.
-   Photos - These will need to stay on OSX until Hazel moves across.
    She's the last thing to migrate and this is a no rollback situation.
-   Skype - Killer. This is essential to talking to folks back home and
    I'm not aware of any usable alternative. There's no 64bit binary for
    Linux available so I expect a debacle trying to get this to work.
-   Flash - Debian comes with gnash which in my mind shouldn't exist
    (like mono) and it's not very good. readingeggs.com does not work
    with it. I'll try resisting install Flash but it may have to happen
    not just for reading eggs but also to help meet the WAF.

The hard part is the Hazel migration as she does get fed up with me
changing things every few years. I do have the fact that she appears to
think anything Apple is a bit pretentious. Which of course it is.
