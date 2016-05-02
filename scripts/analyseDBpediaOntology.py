import rdflib
import sys

g=rdflib.Graph()
g.parse("dbpedia_2015-10.owl")

qres = g.query(
	""" 
	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
	PREFIX owl: <http://www.w3.org/2002/07/owl#>
	select distinct * where { 
  		values ?c1 { owl:Thing } 
  		?c1 ^rdfs:subClassOf ?c2 .
  	OPTIONAL { 
    	?c2 ^rdfs:subClassOf ?c3 .
    	OPTIONAL { 
      	?c3 ^rdfs:subClassOf ?c4 .
      		OPTIONAL { 
      		?c4 ^rdfs:subClassOf ?c5 .
      	OPTIONAL { 
      		?c5 ^rdfs:subClassOf ?c6 .
      	OPTIONAL { 
      		?c6 ^rdfs:subClassOf ?c7 .
     		 }
      	}
      }
    }
  }
} order by ?c7 ?c6 ?c5 ?c4 ?c3 ?c2 
	"""
	)
	
for row in qres:
	for i in row: 
		if i != None:
			i = i.lstrip("http://dbpedia.org/ontology/")
			sys.stdout.write(str(i) + "\t")
	sys.stdout.write("\n")
