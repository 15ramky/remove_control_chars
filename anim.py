from __future__ import print_function
import sys
import time

def screen_anim(line):
	for c in line:
		print (c, end='')
		sys.stdout.flush()
		time.sleep(0.03)
