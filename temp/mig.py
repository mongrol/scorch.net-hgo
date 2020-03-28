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
        nf.write("---\n")
        # put lines in a list
        content = f.readlines()
        block = 0
        for line in content:
            if line.startswith("Title:"):
                print (line)
                title = line[7:].rstrip('\n')
                output = 'Title: "{}'.format(title) + '"\n'
                print (output)
                nf.write(output)
            if line.startswith("Date:"):
                print (line)
                date = line[6:-7]
                output = 'Date: {}'.format(date) + '\n'
                print (output)
                nf.write(output)
            if line.startswith("Author:"):
                print (line)
                author = line[8:].rstrip('\n')
                output = 'Author: "{}'.format(author) + '"\n'
                print (output)
                nf.write(output)
            if line.startswith("Category:"):
                print (line)
                cat = line[10:].rstrip('\n')
                output = 'Categories: ["{}'.format(cat) + '"]\n'
                print (output)
                nf.write(output)
            if line.startswith("Tags:"):
                print (line)
                tagstr = line[6:].rstrip('\n')
                taglist = tagstr.split(", ")
                print (taglist)
                tagstr = ', '.join(str(e) for e in taglist)
                print (tagstr)
                output = 'Tags: ["{}'.format(tagstr) + '"]\n'
                print (output)
                nf.write(output)
            if line.startswith("\n") and block == 0:
                nf.write("---\n")     
                #everything from here is body text
                block = 1
            if block == 1:
                print(line)
                nf.write(line)


             



            
        
