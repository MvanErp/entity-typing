#!/usr/bin/python

import sys

counter = 0
score_at_1_low = 0 
score_at_5_low = 0
score_at_10_low = 0
score_at_1_top = 0 
score_at_5_top = 0
score_at_10_top = 0 
with open(sys.argv[1], 'r') as f:
	for line in f:
		line = line.rstrip()
		if "**_NIL" in line:
			continue 
		elements = line.split("GOLD_STANDARD:")
		gs = elements[1].split("\t")
		counter = counter + 1
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
		# compute the scores for the top level types (more coarse grained)
		for idx, val in enumerate(system):
 			if val == "_**_":
 				pass
 			else:
 				try:
 					if gs[0] == val and idx == 1:
 						#	print "Yay! precision at 1"
 						#	print idx, val, item
 						score_at_1_low = score_at_1_top + 1
 						continue 
 					elif gs[0] == val and idx < 5: 
 						#	print "Yay! precision at 5"
 						#	print idx, val, item 
 						score_at_5_top = score_at_5_top + 1
 						continue
 					elif gs[0] == val and idx < 10: 
 						#print "Yay! precision at 10"
 						#print idx, val, item 
 						score_at_10_top = score_at_10_top + 1
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
	p5_low = (float(score_at_5_low)*100/float(counter))  + p1_low
	p10_low = (float(score_at_10_low)*100/float(counter)) + p5_low

#sys.stdout.write(str(p1_low) + "&" + str(p5_low) + "&" + str(p10_low) + "\n")


#print "Top level types", counter, score_at_1_top, score_at_5_top, score_at_10_top
if counter == 0 :
	p1_top = 0 
	p5_top = 0
	p10_top = 0
else:
	p1_top = (float(score_at_1_top)*100/float(counter))
	p5_top = (float(score_at_5_top)*100/float(counter)) + p1_top
	p10_top = (float(score_at_10_top)*100/float(counter)) + p5_top

print sys.argv[1]
sys.stdout.write(str(format(p1_top, '.2f')) + " & " + str(format(p5_top, '.2f')) + " & " + str(format(p10_top, '.2f')) + " & "+ str(format(p1_low, '.2f')) + " & " + str(format(p5_low, '.2f')) + " & " + str(format(p10_low, '.2f')) + "\n")

#print p1_top
#print p5_top
#print p10_top


