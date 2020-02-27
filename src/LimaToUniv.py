import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import RegexpParser
import os
import sys

os.chdir("..");
#Recuperation des arguments
if(len(sys.argv) < 3):
  print("Not enough arguments. GetTextFromTagged.py take two arguments");
  print("Try with: python3 GetTextFromTagged.py <inputFile> <outputFile>");

inputPathTags = "data/POSTags_PTB_Universal_Linux.txt"
inputPath1 = sys.argv[1];
outputPath1 = sys.argv[2];
print(inputPath1)
print(outputPath1)

inputFileTags = open(inputPathTags, "r+");
contentTags = inputFileTags.read();
inputFileTags.close();

firstTag = []
replacedTag = []
contentsTagLine = contentTags.split("\n");
for line in contentsTagLine:
  lineSplit = line.split(" ");
  firstTag.append(lineSplit[0])
  replacedTag.append(lineSplit[-1]);

inputFile1 = open(inputPath1, "r+");
content1 = inputFile1.read();
inputFile1.close();

wordsLines = content1.split("\n");


outputFile = open(outputPath1, "w+");
for wordTagged in wordsLines:
  if(wordTagged != ""):
    wordsTaggedSplit = wordTagged.split("\t");
    if wordsTaggedSplit[1] in firstTag:
      tag = replacedTag[firstTag.index(wordsTaggedSplit[1])];
    else:
      tag = wordsTaggedSplit[1];
    outputFile.write(wordsTaggedSplit[0] + "\t" + tag + "\n")
  else:
    outputFile.write("\n")
outputFile.close();
