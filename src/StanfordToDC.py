import sys
import os

os.chdir("..");

if(len(sys.argv) < 3):
  print("Not enough arguments. GetTextFromTagged.py take two arguments");
  print("Try with: python3 GetTextFromTagged.py <inputFile> <outputFile>");

inputPath = sys.argv[1];
outputPath = sys.argv[2];

taggedFile = open(inputPath, "r+");
taggedContent = taggedFile.read();
taggedFile.close();

taggedWords = taggedContent.split(" ");
outputFile = open(outputPath, "w+");
for word_tag in taggedWords:
  word_tagSplit = word_tag.split("_");
  outputFile.write(word_tagSplit[0] + "\t" + word_tagSplit[1] + "\n");
outputFile.close();