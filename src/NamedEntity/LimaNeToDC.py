import sys
import os


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
try:
  for line in inputLines:
    #boucle sur chacune des lignes
    if(line != ""):
      #si ligne non vide
      if(line[0] != "#"):
        #si pas ligne de commentaire
        #extraction du mot et de son entity nomme
        lineColumn = line.split("\t");

        #print(lineColumn[9].split("."))
        #verifier que l'entity nomme exist
        if(len(lineColumn[9].split(".")) > 1):
          en = lineColumn[9].split(".")[1].split("|")[0];
        else:
          en = "O";
          #previous =""
          
        rsltStr += lineColumn[1] + "\t" + en + "\n";
        #print(rsltStr)
    '''else:
      rsltStr += "\n";'''
except Exception as e:
    print(str(e))

#ecriture dans fichier de sortie
outputFile = open(outputPath, "w+");
outputFile.write(rsltStr);
outputFile.close();


  