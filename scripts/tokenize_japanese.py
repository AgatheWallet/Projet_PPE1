#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# """
# A exécuter ainsi 
# python3 ./scripts/tokenize_japanese.py
# """

#import spacy

entree=input("Entrez le chemin du fichier à tokenizer : ")
coupe_path=entree.split('/')
coupe_ext=coupe_path[-1].split('.')
coupe_path=coupe_path[:len(coupe_path)-1]
path='/'.join(coupe_path)
coupe_path='/'.join(coupe_path[-1])
sortie=path+'/'+coupe_ext[0]+"-tok."+coupe_ext[1]



nlp = spacy.load("ja_core_news_sm")
with open (entree, 'r') as rf:
 	with open (sortie, 'w') as wt:
		for line in rf:
 			doc=nlp(line)
 			for token in doc:
				wt.write(token.text)
				wt.write(" ")


