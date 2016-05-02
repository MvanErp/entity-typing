#!/usr/bin/python

import sys

counter = 0
with open(sys.argv[1], 'r') as f:
	for line in f:
		line = line.rstrip()
		counter = counter +1 
		if "**_NIL" in line:
			continue 
 		elements = line.split("GOLD_STANDARD:")
 		gs = elements[1].split("\t")
 		if len(gs) < 2:
 			sys.stdout.write(str(sys.argv[1]) + "\t" + str(counter) + "\t" + line + "\n") 