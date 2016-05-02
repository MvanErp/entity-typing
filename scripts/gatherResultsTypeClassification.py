#!/usr/bin/python

import sys
import collections 
import numpy
from itertools import islice

# First read in the file with the entity types as a dict of dicts
# entities_types[entity][type] 
entities_types = collections.defaultdict(dict)
with open(sys.argv[1], 'r') as f:
	for line in f:
		line = line.rstrip()
		elements = line.split("\t")
		entities_types[elements[1]][elements[2]] = 1     
f.close()	 

# Then read in the results file as a dict of dicts
# results[entity_to_classify][class] = [] (scores will be put in a list 
# at the end, the list will be read in and the average over the class will be computed)  
results = collections.defaultdict(list)
with open(sys.argv[2], 'r') as f:
	for line in f:
		line = line.rstrip()
		elements = line.split("\t")
		if "NIL" in elements[3]:
			continue
		for entity_type in entities_types[elements[3]]:
			if "http://dbpedia.org/ontology/" in entity_type:
				if "http://dbpedia.org/ontology/Location" in entity_type:
					continue
					#print elements[1], elements[3], type
				else:	
					key = elements[0] + "_**_" + elements[1] + "_*_" + entity_type 
					results[key].append(float(elements[4]))
f.close()   

# Read out the results dict and compute the average score per class for each entity 
rehash = collections.defaultdict(dict)
for entity in results:
	#for type in entity:
	#	print results[entity][type]
	entity_parts = entity.split("_*_")
	rehash[entity_parts[0]][entity_parts[1]] = numpy.mean(results[entity])	
	

# Now this is the bit where you print the top 10 classes
for entity in rehash:
	rehash_sorted = sorted(rehash[entity], key=rehash[entity].get, reverse=True)
	iterator = islice(rehash_sorted, 10)
	sys.stdout.write(entity + "\t")
	entity_parts = entity.split("_**_")
	gs_string = ""
	for entity_type in entities_types[entity_parts[1]]:
		if "http://dbpedia.org/ontology/" in entity_type:
			entity_type = entity_type.lstrip("http://dbpedia.org/ontology/")
			gs_string = gs_string + entity_type + "\t"
	for item in iterator:
		item_stripped = item.lstrip("http://dbpedia.org/ontology/")
  		sys.stdout.write(item_stripped + "\t" + str(rehash[entity][item]) + "\t") 
  		#	print entity, value, rehash[entity][value]
  	sys.stdout.write("GOLD_STANDARD:\t" + gs_string + "\n")
  		

