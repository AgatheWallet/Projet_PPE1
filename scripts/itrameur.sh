#!/usr/bin/env bash

#=======================================================================
# script pour rendre les fichiers textes traitables par iTrameur
# Pour lancer le script: 
# ./scripts/itrameur.sh
#=======================================================================

path="./dumps-text/*"

output="./iTrameur/iTrameur.txt"

echo "" > $output

for subpath in $path
do
	lang=$(echo "$subpath" | sed "s/\.\/dumps-text\///g") 
	echo "<lang=\"$lang\">" >> $output
	#echo "$lang"
	for file in $subpath/*
	do
		filename=$(echo "$file" | sed "s/\.\/dumps-text\/[a-z]*\/URL_//g; s/.txt//g")
		echo "<page=\"$filename\">" >> $output
		contenu=$(cat "$file" | sed 's/\&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g')
		echo "<text>$contenu</text>" >> $output
		echo "</page> §" >> $output
	done
	echo "</lang>" >> $output
done
