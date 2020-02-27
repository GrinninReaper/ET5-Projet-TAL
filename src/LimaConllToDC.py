import sys
import os

os.chdir("..");

#Recuperation des arguments
if(len(sys.argv) < 3):
  print("Not enough arguments. GetTextFromTagged.py take two arguments");
  print("Try with: python3 GetTextFromTagged.py <inputFile> <outputFile>");
#Stockage des chemins d'entree et de sortie
inputPath = sys.argv[1];
outputPath = sys.argv[2];

#recueperation du contenu du fichier d'entree
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
  else:
    rsltStr += "\n";

#ecriture dans fichier de sortie
outputFile = open(outputPath, "w+");
outputFile.write(rsltStr);
outputFile.close();