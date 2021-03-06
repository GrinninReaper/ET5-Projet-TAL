#Projet de TAL
Author: Anandou C.
		Abdoulaye D. 
		Justine Thanh N.H.T

Object 
Guide des fichiers pour le projet de TAL

En règle générale pour les deux exercices, les scripts sont dans le dossier /src. 
Les résultats sont situés dans le dossier /data. 

Exercice 1
Les fichiers de données de l'exercice 1 sont ceux commençant par "pos_". 
Pour toute exécution des scripts il faut donner deux arguments.
Le premier argument renseigne le fichier contenant les données de base. Le deuxième argument renseigne le nom sous lequel on souhaite stocker le fichier de résultat.
Le déroulé permet d'obtenir les résultats pour effectuer l'analyse, ces étapes sont aussi détaillées dans le rappor du projet.
Pour obtenir les résultats: 
 * se placer dans le dossier /src
 * lancer le script LimaTransform.py
 * lancer LimaToUniv.py sur le fichier résultant
 * lancer TaggedToTxt.py
 * utiliser le fichier .txt résultant pour les analyes (le script Nltk.py) permet l'analyse nltk
 * utiliser les scripts StanfordToDC.py et LimaConllToDC.py sur les fichiers correspondant
 * utiliser le script LimaTransform.py sur chacun des fichiers résultats des analyses
 * utiliser les LimaToUniv.py, StfdToUniv.py et NltkToUniv.py
 * lancer evaluate.py sur les fichiers obtenus en résultat
 
Exercice 2
Les fichiers de données de l'exercice 2 sont ceux commençant par "ne_".
Les scripts relatifs à cet exercice sont dans le dossier /src/NamedEntity. 
Le principe d'exécution des scripts reste le même que pour l'exercice 1 et est aussi détaillé dans le rapport.
 Pour obtenir les résultats: 
 * se placer dans le dossier /src/NamedEntity
 * lancer la commande java -mx600m -cp stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile ne_test.txt > ne_test.txt.ne.stanford.unrendered
 pour stanford
 * lancer la commande analyzeText -l eng -p main ne_test.txt > ne_test.txt.ne.lima.unrendered
 pout lima
 * lancer le script Nltk_ne.py ../../data/ne_test.txt ../../data/ne_test.txt.ne.nltk

  *** Transformer les résultats en deux colonnes***
  * Toujours se placer dans le dossier NamedEntity
  * lancer le script StanfordNeToDC.py ../../data/ne_test.txt.ne.stanford.unrendered ../../data/ne_test.txt.ne.stanford
  * lancer le script LimadNeToDC.py ../../data/ne_test.txt.ne.lima.unrendered ../../data/ne_test.txt.ne.lima

  *** Conversion des étiquettes en étiquettes Conll2003 ***

  * Toujours se placer dans le dossier NamedEntity
  * * lancer le script StanfordNeToConll.py ../../data/ne_test.txt.ne.stanford ../../data/ne_test.txt.ne.stanford.conll
  * lancer le script LimadNeToConll.py ../../data/ne_test.txt.ne.lima ../../data/ne_test.txt.ne.lima.conll
  * lancer le script LimadNeToConll.py ../../data/ne_test.txt.ne.nltk ../../data/ne_test.txt.ne.nltk.conll
 * lancer evaluate.py sur les fichiers obtenus en résultat
