#! /usr/bin/python

import os
import anim

def parse_each(each_file):
	out_file = each_file+str(".result")
	out_f = open(out_file, "w")

	with open(each_file,"rb") as f:
            anim.screen_anim("Processing ..."+str(each_file))
            for line_p in f.readlines():
                line, i, imax = '', 0, len(line_p)
                while i < imax:
                    ac = ord(line_p[i])
                    if (32<=ac<127) or ac in (9,10): # printable, \t, \n
                        line += line_p[i]
                    elif ac == 27:                   # remove coded sequences
                        i += 1
                        while i<imax and line_p[i].lower() not in 'abcdhsujkm':
                            i += 1
                    elif ac == 8 or (ac==13 and line and line[-1] == ' '): # backspace or EOL spacing
                        if line:
                            line = line[:-1]
                    i += 1

                out_f.write(line)
            anim.screen_anim(" -- DONE\n")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for each_file in files:
	if each_file.split('.')[-1] == "data":
		parse_each(each_file)

