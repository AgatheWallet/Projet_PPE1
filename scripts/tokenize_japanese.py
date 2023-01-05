#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A exécuter ainsi 
python3 ./scripts/tokenize_japanese.py
"""
import spacy


nlp = spacy.load("ja_core_news_sm")
with open ("./iTrameur/contextes-jp.txt", 'r') as rf:
	with open ("./iTrameur/contextes-jp-tok.txt", 'w') as wt:
		for line in rf:
			doc=nlp(line)
			for token in doc:
				wt.write(token.text)
				wt.write(" ")

