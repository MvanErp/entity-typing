# -*- coding: utf-8 -*-

import sys
from lxml import etree

infile = open(sys.argv[1], "r")
raw = infile.read()
doc1 = etree.XML(raw)
texts = doc1.findall(".//text")
for text in texts:
	paragraphs = text.findall(".//p")
	for paragraph in paragraphs:
		print paragraph.text 
