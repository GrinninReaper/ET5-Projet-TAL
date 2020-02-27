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

rsltStr = "";
inputLines = taggedContent.split("\n");
for line in inputLines:
  if(line != ""):
    if(line[0] == '#'):
      print("Ignored line");
    else:
      lineColumn = line.split("\t");
      rsltStr += lineColumn[1] + "\t" + lineColumn[3] + "\n";

outputFile = open(outputPath, "w+");
outputFile.write(rsltStr);
outputFile.close();