import sys
import os

os.chdir("..");

#Récupération des arguments
if(len(sys.argv) < 3):
  print("Not enough arguments. GetTextFromTagged.py take two arguments");
  print("Try with: python3 GetTextFromTagged.py <inputFile> <outputFile>");
#Stockage des chemins d'entrée et de sortie
inputPath = sys.argv[1];
outputPath = sys.argv[2];

#récupération du contenu du fichier d'entrée
taggedFile = open(inputPath, "r+");
taggedContent = taggedFile.read();
taggedFile.close();

#traitement
rsltStr = "";
inputLines = taggedContent.split("\n"); #extraction ligne par ligne
for line in inputLines:
  #boucle sur chacune des lignes
  if(line != ""):
    #si ligne non vide
    if(line[0] != '#'):
      #si pas ligne de commentaire
      #extraction du mot et de son tag
      lineColumn = line.split("\t");
      rsltStr += lineColumn[1] + "\t" + lineColumn[3] + "\n";

#écriture dans fichier de sortie
outputFile = open(outputPath, "w+");
outputFile.write(rsltStr);
outputFile.close();