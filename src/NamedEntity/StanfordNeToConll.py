import sys
import os
import re
import LimaNeToConll as ldc


if(len(sys.argv) < 3):
  print("Not enough arguments. GetTextFromTagged.py take two arguments");
  print("Try with: python3 GetTextFromTagged.py <inputFile> <outputFile>");

inputPath = sys.argv[1];
outputPath = sys.argv[2];

taggedFile = open(inputPath, "r+");
taggedContent = taggedFile.read();
taggedFile.close()

taggedLines = taggedContent.split("\n")
taggedWords = []
for line in taggedLines:
  taggedWords += line.split(" ")
outputFile = open(outputPath, "w+")
previous = ""
for word_tag in taggedWords:
  print(word_tag)
  word_tagSplit = word_tag.split("\t")

  if(len(word_tagSplit) == 2):
    if(word_tagSplit[1] != "O"):
      en = ldc.convEnToEtiq(word_tagSplit[1])
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
      en = word_tagSplit[1]
      previous =""
    outputFile.write(word_tagSplit[0] + "\t" + en + "\n");
outputFile.close();