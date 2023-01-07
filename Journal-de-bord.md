# JOURNAL DE BORD 
## Mot = Féminisme 
## Langues : Florian (Japonais) / Agathe (Coréen et français) / Fanny (Portugais et français) 

## 1er novembre 
Fanny : 
- Ajout d'URL pour alimenter le corpus en Portugais. 
- Création d'un fichier féminisme, quelques recherches sur la définition et l'histoire du mot féminisme en France. 
- Création d'un fichier question, à alimenter avec nos questions et nos remarques. 

## 21 novembre 
Fanny : 
- Création d'un fichier "index.html" afin de créer une page web pour le projet. 
- To do : continuer de trouver des liens, affiner les explications sur le pourquoi du choix du mot. 
- C'est une défaite, je n'arrive pas à créer un site web, il semblerait que seul le propriétaire du dépôt puisse le faire (je ne trouve pas l'onglet settings)
- ajout de liens pour le corpus en portugais. 
Questionnement : nécessité de faire un corpus en français ? 

## 22 novembre
Agathe : 
- Création d'un répertoire pour le site
- Activation des pages git
- Création du fichier tableau.html

Fanny : 
- Ajout de liens pour le corpus en portugais. 

## 26 novembre
Agathe:
- Ajout d'URL pour corpus coréen
- Ajout d'URL pour corpus français
- Fusion des fichiers README.md et questions.txt

## 30 novembre 
Fanny : 
- Modification de la page web => ajout définition + titre. 
- Modifications sur l'index. 


## 7 décembre 
Fanny :
- Création d'un dossier et fichiers pour le site web
- Remplissage des pages html
- Ajout des derniers URL pour le portugais
- Mise sur le git de la première version du script qu'il est nécessaire de modifier. 

Agathe : 
- Travail sur le script pour générer les tableaux
- Mise en page du site : ajout de la fiche CSS Bulma et d'une feuille CSS supplémentaire pour pouvoir modifier certaines choses

## 20 décembre
Agathe :
- Modification du script bash pour la génération des tableaux → ajout d'une balise fermante manquante
- Ajout des derniers URLs pour le coréen
- Génération du tableau pour le coréen
- CSS pour la page tableaux.html avec ajout du tableau coréen complet 

Florian :  
- Ajout script pour faire les concordanciers

## 21 décembre
Agathe :
- Première tentative de mise en page de notre page Présentations mais pas convaincue
- Faudrait-il garder cette page pour nous présenter nous et ajouter une page sur le féminisme ?


## 27 décembre et 28 décembre
Agathe : 
- Fusion du script `base-tableau-html.sh` et du script `concordancier.sh` fait par Florian
- Lancement du script sur le fichier URL : je me suis rendue compte que le nombre d'occurences trouvées par le script de Florian était bien en deçà du nombre d'occurences réel. Nous nous sommes rendus compte qu'en voulant prendre la phrase entière dans laquelle notre mot apparaît, c'est à dire en cherchant une chaîne de caractères contenant notre mot, précédée et suivie d'un point, nous mettions de côté toutes les phrases démarrant un nouveau paragraphe. J'ai donc remplacé les doubles passages à la ligne par un caractère § pour indiquer qu'il s'agit de la fin d'un paragraphe. Les simples sauts à la ligne ont aussi été retirés pour éviter que les phrases de soient coupées d'une ligne à une autre. Malgré tout, nous ne réussissons pas à obtenir 100% de nos occurrences mais nous en obtenons la plupart. De même, nous n'arrivons pas à récupérer une phrase plusieurs fois lorsqu'il y a plusieurs occurrences de notre mot dans la phrase (la phrase n'apparaît qu'une fois dans le concordancier).
- Ajout de la page concordancier et de son accès au menu sur toutes les pages + mise en page CSS

Florian :  
- Fin de recherche et ajout des 51 urls pour le japonais

## 29 décembre :  
Florian :  
- Recherche et ajout des 50 urls pour le français

## 30 décembre : 
Agathe : 
- Ajout d'un début de présentation de nous 3
- Création d'un fichier supplémentaire pour les détails autour du mot féminisme (page à travailler, avec ajout balises début, fin, etc)
- Création des tableaux pour le français
- Modification du tableau kr sur le site
- Ajout tableaux français sur le site
- Ajout du remplacement des caractères < > et & par leurs entités html dans le script `base_tableaux_fichiers.sh`

Florian : 
- Exécution du scripts `base_tableaux_fichiers.sh` pour le mot 'フェミニズム'　qui produit les pages html pour le tableau d'urls et le concordancier 
- Création des tableaux pour le japonais  
- Création du concordancier pour le japonais après ajout des caractères de ponctuation japonais '？' et　'！' (différents des caractères ASCII leur ressemblant) pour délimiter les phrases contenant le mot フェミニズム  
- Ajout tableau d'urls japonais sur le site  
- Ajout concordancier japonais sur le site  

## 1er janvier
Agathe :
- Ajout de sous-répertoire par langue pour les dumps, les aspirations et les contextes 
- Ré exécution du script `base_tableaux_fichiers.sh` sur le français, le coréen et le japonais
- Ajout du script pour la mise en page des dumps pour le traitement iTrameur
- Exécution du script `make_itrameur_corpus.sh` → il semble y avoir un petit problème avec l'encodage du fichier de sortie `dumps.txt` (est détecté comme du Latin 1 par Geany et quand ouverture avec `Text Editor`, l'erreur suivante s'affiche : `The file you opened has some invalid characters.`. Cependant, en fermant l'erreur, le texte s'affiche parfaitement bien.


## 2 janvier 
Fanny : 
- Exécution du script `base_tableaux_fichier.sh` pour le mot "feminismo", permettant ainsi de générer les pages html, le tableau d'urls et le concordancier. 
- Exécution du script iTrameur. 
- Ajout d'informations sur la page "féminisme", approfondissement sur l'histoire du mot. 

## 3 janvier
Agathe : 
- Insertion des tableaux portugais sur le site
- Changement des expressions régulières pour le changement des caractères "<", ">" et "&" en entités html dans le programme 
- Exécution du programme `make_itrameur_corpus.sh` et test des fichiers `dumps.txt` et `contextes.txt` sur iTrameur → les fichiers sont correctement lus
- Insertion de la page féminisme sur le site et ajout de la définition du féminisme selon le dictionnaire en ligne coréen Naver

## 4 janvier
Agathe :
- Génération des nuages de mots pour le français et le portugais à partir des dumps-text

Fanny : 
- Première analyses pour le français et le portugais. 
- Vérification des mots pour le nuage de mot en portugais. 
- Recherche de données sur iTrameur. => concordancier avec le mot "feminismo" ... 

## 5 janvier
Agathe : 
- Tokenization des contextes japonais avec script utilisant tokenizer spacy pour génération des nuages de mots
- Génération des nuages de mots pour le français, le portugais, le coréen et le japonais (stopwords encore à supprimer pour portugais et japonais) à partir des contextes → plus pertinent et retire les menus, etc
- Ajout des scripts bash sur le site
- Ajout de l'image bas-de-page sur toutes les pages du site

Florian :  
- Modification du script de tokenisation python pour accepter un argument (le nom du fichier à tokeniser) lors de son exécution
- Écriture script bash pour tokeniser tous les dumps et tous les contextes japonais car iTrameur a besoin que les textes soient tokenisés pour pouvoir faire une analyse textométrique 
- Mise à jour de toutes les aspirations, dumps et contextes japonais car ceux-ci n'étaient plus en accord avec les liens japonais
- Tokenisation des dumps et des contextes japonais
- Création du corpus `dump-jp` et `contexte-jp` pour itrameur avec les dumps et les contextes tokenisés 

## 6 janvier  
Florian :  
- Création du nuage de mot japonais avec le site suivant : [https://www.nuagesdemots.fr/][https://www.nuagesdemots.fr/]. Les _stopwords_ japonais ont été retirés ainsi que tout autres mots ne nous intéressant pas pour l'analyse textométrique.

## 7 janvier 
Fanny : 
- Mise en ligne des premières analyses sur le français et le portugais. 
- Modification de la page présentation. 
- Modifications URL en portugais, certains n'avaient pas le code 200
- Éxecution de nouveau du script `base_tableaux_fichiers.sh` pour le mot "feminismo". 

Florian : 
- Ajout présentation Florian sur la page présentation du site 
- Ajout de la définition du terme "フェミニズム" en japonais 
