#!/usr/bin/python

# This script will query DBpedia for the dbpedia classes of entities 
# Date: 17 April 2016
# Author: Marieke van Erp // marieke.van.erp@vu.nl

from SPARQLWrapper import SPARQLWrapper, JSON
import sys
import codecs
from time import sleep


with open(sys.argv[1], 'r') as f:
    for line in f:
        if "NIL" in line:
            continue
        line = line.rstrip()
        parts = line.split('\t')
        link = parts[1]
        link = "<" + link + ">"
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        query = u"""SELECT DISTINCT ?p WHERE{ %s rdf:type ?p . }""" % (link)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results["results"]["bindings"]:
        	#print result
        	output= result["p"]["value"]
        	#if "http://dbpedia.org/ontology/" in output:
        	outputstring = parts[0] + "\t" +  parts[1] + "\t" + output 
        	print outputstring
        sleep(2) 
        	 
# lineno = 0 
# with open(sys.argv[1], 'r') as f:
#     for line in f:
#         if "?entity" in line:
#             continue
#         line = line.rstrip()
#         parts = line.split('\t')
#         variable = parts[0]
#         sparql = SPARQLWrapper("http://dbpedia.org/sparql")
#         query = u"""SELECT DISTINCT ?p ?o WHERE {
# %s ?p ?o .
# }""" % (variable)
#         sparql.setQuery(query)
#         sparql.setReturnFormat(JSON)
#         results = sparql.query().convert()
#         
#         filename = "Persons/" + variable[29:-1] + ".txt"
#         print variable, filename
#         f = open(filename, 'w+') 
#  
#         for result in results["results"]["bindings"]:
#             output = parts[0] + "\t" + result["p"]["value"] + "\t" + result["o"]["value"] + "\n"
#             output = output.encode('utf8')
#             f.write(output)
#         f.close()
#         lineno = lineno + 1
#         if lineno > 100:
#             break
#         sleep(2)