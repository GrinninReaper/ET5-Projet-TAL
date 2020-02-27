#LimaTransform: transformation des tags LIMA en tags PTB
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import RegexpParser

#noms des fichiers d'entrées et de sorties
inputPath1 = "data/pos_reference.txt.lima"
outputPath1 = "data/pos_reference.txt.lima2";

#lecture du fichier d'entrée et récupération du contenu
inputFile1 = open(inputPath1, "r+");
content1 = inputFile1.read();
inputFile1.close();

nltk.download('averaged_perceptron_tagger');

#initialisation des tags LIMA à transformer en PTB
arrayTagsKeys=["SCONJ","SENT","COMMA", "COLON", "PROPN","AUX", "ADJ", "VERB", "DET", "ADP", "NOUN", "PART", "CONJ", "OQU", "QUOT"];
arrayTagsValues=["CC",".",",",":", "NNP", "MD","JJ", "VB", "DT", "IN", "NN", "POS", "CC", ".", "."];

#séparation du contenu du fichier d'entrée par saut de ligne
#puis séparation de chaque ligne en tabulation
#ainsi que correction des noms propres en une ligne vers plusieurs lignes
# ex: Pierre Vinken NNP devient
# Pierre  NNP
# Vinken  NNP
contentSplitSpace1 = content1.split('\n');
arrayContentKeys1=[];
arrayContentValues1=[];
for i in range(len(contentSplitSpace1)):
  if(contentSplitSpace1[i] == ""):
    arrayContentKeys1.append("\n")
    arrayContentValues1.append("")
  else:
    contentSplitTab= contentSplitSpace1[i].split('\t');
    for j in range(len(contentSplitTab)-1):
      wordsInContent = contentSplitTab[0].split(" ")
      tagToAdd = contentSplitTab[-1]
      for k in range (len(wordsInContent)):
        arrayContentKeys1.append(wordsInContent[k])
        arrayContentValues1.append(tagToAdd)

print("\n");
writeTag = False;
tagToWrite = "";

#Création du fichier de sortie
#transformation des tags Lima en PTB
outFile1 = open(outputPath1, "w");
for j in range(len(arrayContentKeys1)):
  for i in range(len(arrayTagsKeys)):
    if(arrayContentValues1[j] == arrayTagsKeys[i]):
      tagToWrite = arrayTagsValues[i]
      writeTag = True
  if(writeTag):
    outFile1.write(arrayContentKeys1[j] + "\t");
    outFile1.write(tagToWrite + "\n");
    writeTag = False;
  else:
    if(arrayContentKeys1[j] == "\n"):
      outFile1.write("\n");
outFile1.close();

