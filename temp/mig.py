# migrate from pelican to hugo

# Here's a source header of swim-swim-swim.md

#Title: >Swim swim swim!
#Date: 2008-10-28 12:00
#Author: mongrol
#Category: The Skreegs
#Tags: Miniskreeg, Weekends
#Slug: swim-swim-swim

# Dest should be swim-swim-swim.md

#---
#Title: "Swim swim swim!"
#Date: 2007-08-17
#Author: "mongrol"
#Categories: ["The Skreegs"]
#Tags: ["Miniskreeg", "Weekends"]
#Slug: swim-swim-swim
#---

# Open all files in dir

import glob, os

path = './src/'
dst = './dst/'
for filename in glob.glob(os.path.join(path, '*.md')):
    newfile = os.path.join(dst, os.path.basename(filename))
    with open(filename) as f:
        nf = open(newfile, 'w')
        # put lines in a list
        content = f.readlines()
        for line in content:
            if line.startswith("Title:"):
                print (line)
                title = line[7:].rstrip('\n')
                output = 'Title: "{}'.format(title) + '"'
                print (output)
                nf.write(output)
        
