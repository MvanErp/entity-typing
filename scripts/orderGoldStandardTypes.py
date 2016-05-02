#!/usr/bin/python

# This script sorts the gold standard types in the results file according to the DBpedia
# hierarchy. The evaluation script can be modified to output the top level results or the
# more finegrained results  
# Author: Marieke van Erp 
# Date: 27 April 2016 

import sys
import collections
from ordered_set import OrderedSet

# First load the DBpedia ontology
dbpedia = {} 
with open("DBpediaHierarchy.tsv", "r") as f:
	for line in f:
		line = line.rstrip()
		elements = line.split("\t")
		elements.pop(0)
		dbpedia[elements[-1]] = []
		dbpedia[elements[-1]] = elements
		#print dbpedia[elements[-1]]
		elements.pop(-1)
		for element in elements: 
			try:
				dbpedia[elements[-1]] = elements
			except:
				pass
			#print dbpedia[elements[-1]]
			
f.close()

for item in dbpedia:
	if len(dbpedia[item]) == 0:
		dbpedia[item].append(item)
	if dbpedia[item][-1] != item:
	#		print "Let's fix this", dbpedia[item], item
		dbpedia[item].append(item)
		continue
	#		print "Fixed ", dbpedia[item], item
		#else:
		#	print "OK We're good", dbpedia[item], item
	#	print "I did something else here", dbpedia[item], item
	#print "Bla ", item, dbpedia[item] 
	#list = dbpedia[item]
	#print len(list)
	#print list[0]
	#for elem in list:
	#	print "bla", elem 


for item in dbpedia:
	if len(dbpedia[item]) > 1:
		if dbpedia[item][-2] == item:
			dbpedia[item].pop(-1)
	#print item, dbpedia[item]


with open(sys.argv[1], "r") as f:
	for line in f:
		line = line.rstrip()
		split1 = line.split("GOLD_STANDARD:")
		split1[1] = split1[1].replace("Location\t", "") # Hack to also remove the Location equivalent class from results 
		split1[1] = split1[1].lstrip("\t")
		types = split1[1].split("\t")
		longest = 0
		best_match = []
	#	print types 
		for item in dbpedia:
			if collections.Counter(dbpedia[item]) == collections.Counter(types):
				#print "Yay", types
				best_match = dbpedia[item]
				break
		#	else:
		#		print "no Match", item, dbpedia[item]
		#if len(best_match) == 0:
		#	for type in types:
		#		if type in dbpedia:
		#			try:
		#				if len(best_match) < len(dbpedia[type]):
		#					best_match = dbpedia[type]
		#					best_match.append(type)
		#			except: 
		#				pass
		#try:
		final_match = OrderedSet(best_match)
		#	print types, best_match, OrderedSet(best_match), len(best_match), len(types) 
		#except:
		#	print "bla ", types, best_match
		sys.stdout.write(split1[0] + "\tGOLD_STANDARD:\t" + "\t".join(final_match) + "\n")					
f.close()
		