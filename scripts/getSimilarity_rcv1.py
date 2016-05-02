#!/usr/bin/python

import sys
#from gensim.models import Word2Vec
from gensim.models import word2vec

model = word2vec.Word2Vec.load_word2vec_format('rcv1vectors.bin', binary=True)

#model = word2vec.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
#model = Word2Vec.load("en_1000_no_stem/en.model")

entities = {}
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.rstrip()
        elements = line.split("\t")
        if len(elements) == 1:
		elements.append("NIL")
	entities[elements[0]] = elements[1]
        
for entity in entities:
	for secondlayer in entities: 
		if entity != secondlayer:
			entity_parts = entity.split(" ")
			secondlayer_parts = secondlayer.split(" ")
			try:
				result = model.n_similarity(entity_parts, secondlayer_parts)
				print entity + "\t" + entities[entity] + "\t" +  secondlayer + "\t" + entities[secondlayer]+"\t" + str(result)
			except:
				pass  
        
#   try:
#      results = model.most_similar([ elements[0], elements[1]], [elements[2]], topn=3)
#     sys.stdout.write(elements[2] + "\t")
#    for result in results:
#       sys.stdout.write(str(result[0]) + ' ' + str(result[1]) + "\t")
     #   sys.stdout.write("\n")
    #except KeyError, e:
     #   print line, 'Reason: %s' % str(e)



