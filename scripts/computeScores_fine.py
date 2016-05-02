#!/usr/bin/python

import sys

counter = 0
score_at_1_low = 0 
score_at_5_low = 0
score_at_10_low = 0
with open(sys.argv[1], 'r') as f:
	for line in f:
		line = line.rstrip()
		if "**_NIL" in line:
			continue 
		counter = counter + 1
		elements = line.split("GOLD_STANDARD:")
		gs = elements[1].split("\t")
		if len(gs[0]) < 2:
			gs.pop(0)
		system = elements[0].split("\t")
		# Compute the scores for the low level types (more fine grained) 
		for idx, val in enumerate(system):
			if val == "_**_":
				pass
			else:
				try:
					if gs[-1] == val and idx == 1:
						#print "Yay! precision at 1"
						#print system, idx, val, item
						score_at_1_low = score_at_1_low + 1 
						continue
					elif gs[-1] == val and idx < 5: 
						#print "Yay! precision at 5"
						#print idx, val, item 
						score_at_5_low = score_at_5_low + 1
						continue
					elif gs[-1] == val and idx < 10: 
						#print "Yay! precision at 10"
						#print system, idx, val, item 
						score_at_10_low = score_at_10_low + 1
				except:
					pass	
f.close()

if counter == 0 :
	p1_low = 0
	p5_low = 0
	p10_low = 0
else:
#	print "Low level types", sys.argv[1], counter, score_at_1_low, score_at_5_low, score_at_10_low
	p1_low = (float(score_at_1_low)*100/float(counter))
	p5_low = (float(score_at_5_low)*100/float(counter))  
	p10_low = (float(score_at_10_low)*100/float(counter))

sys.stdout.write(str(p1_low) + "\t" + str(p5_low) + "\t" + str(p10_low) + "\n")





