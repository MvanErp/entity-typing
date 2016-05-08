#!/usr/bin/python

# This script first gathers the topic descriptions, then adds those to each document ID
# Note that the topic descriptions file was reformatted to tab separated instead of space separated
# tr -s " " < rcv1.topics.hier.orig.txt | tr " " "\t" > rcv1.topics.hier.orig.tsv 
# Author: Marieke van Erp 
# Date: 26 April 2016 

import sys
import re

topics = {}
with open('rcv1.topics.hier.orig.tsv', 'r') as f:
	for line in f:
		line = line.rstrip()
		parts = line.split("\t")
		description = '_'.join(parts[5:])
		description = description.replace(",", "")
		topics[parts[3]] = description
f.close()

docs_topics = {}
with open('rcv1-v2.topics.qrels.txt', 'r') as f:
	for line in f:
		line = line.rstrip()
		parts = line.split(" ")
		pattern = re.compile("CCAT|\\bC15\\b|\\bC151\\b|\\bC17\\b|\\bC18\\b|\\bC31\\b|\\bC33\\b|\\bC41\\b|ECAT|\\bE12\\b|\\bE13\\b|\\bE14\\b|\\bE21\\b|\\bE31\\b|\\bE41\\b|\\bE51\\b|GCAT|\\bG15\\b|MCAT|\\bM13\\b|\\bM14\\b")
		match = re.match(pattern, parts[0])
		if match:   # change in to if not match: for top level topics only 
			continue
		if not parts[1] in docs_topics:
			docs_topics[parts[1]] = []
			docs_topics[parts[1]].append(topics[parts[0]])
		else:
			docs_topics[parts[1]].append(topics[parts[0]])
f.close()

with open('index_docnames.txt', 'r') as f:
	for line in f:
		line = line.rstrip() 
		line = line.rstrip('newsML.txt')
		parts = line.split("*")
		try:
			sys.stdout.write(parts[1] + "\t" + ' '.join(docs_topics[parts[1]]) + "\n")
		except:
			sys.stdout.write(parts[1] + "\tNONE\n")



		