import sys
import os

def convEnToEtiq(entity):
  #print(entity)
  if(entity == "ORGANIZATION"):
    return "ORG"
  if(entity == "LOCATION"):
    return "LOC"
  if(entity == "PERSON"):
    return "PERS"
  if(entity == "NUMEX"):
    return "NUMEX"
  if(entity == "DATE"):
    return "DATE"
  if(entity == "GEO"):
    return "GEO"
  if(entity == "NUMBER"):
    return "NUMBER"
  if(entity == "UNIT"):
    return "UNIT"
  if(entity == "TIME"):
    return "TIME"
  else:
    return entity


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
previous = ""
try:
  for line in inputLines:
    #boucle sur chacune des lignes
    if(line != ""):
      #si ligne non vide
      if(line[0] != ""):
        #si pas ligne de commentaire
        #extraction du mot et de son entity nomme
        lineColumn = line.split("\t");

          #print(lineColumn[9].split("."))
        if(lineColumn[1] != "O"):
          en = lineColumn[1]
          en = convEnToEtiq(en)
          #verfier que l'entity est une sous entity
          if(previous == "B"):
            en = "I-" + en
            previous = "B"
          #La premiere entity
          else:
            en = "B-" + en
            previous = "B"
          print(en);
        else:
          en = lineColumn[1]
          previous =""
          
        rsltStr += lineColumn[0] + "\t" + en + "\n";
        #print(rsltStr)
except Exception as e:
    print(str(e))

#ecriture dans fichier de sortie
outputFile = open(outputPath, "w+");
outputFile.write(rsltStr);
outputFile.close();


  