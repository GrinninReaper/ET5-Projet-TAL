import sys
import os
import re

os.chdir("..");

if(len(sys.argv) < 3):
  print("Not enough arguments. GetTextFromTagged.py take two arguments");
  print("Try with: python3 GetTextFromTagged.py <inputFile> <outputFile>");

inputPath = sys.argv[1];
outputPath = sys.argv[2];

taggedFile = open(inputPath, "r+");
taggedContent = taggedFile.read();
taggedFile.close();

taggedLines = taggedContent.split("\n");
taggedWords = []
for line in taggedLines:
  taggedWords += line.split(" ");
outputFile = open(outputPath, "w+");
i = 0
for word_tag in taggedWords:
  i += 1
  print(word_tag)
  word_tagSplit = word_tag.split("_");
  if(len(word_tagSplit) == 2):
    outputFile.write(word_tagSplit[0] + "\t" + word_tagSplit[1] + "\n");
outputFile.close();