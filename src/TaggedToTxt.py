import sys

if(len(sys.argv) < 3):
  print("Not enough arguments. GetTextFromTagged.py take two arguments");
  print("Try with: python3 GetTextFromTagged.py <inputFile> <outputFile>");


inputPath = sys.argv[1];
outputPath = sys.argv[2];

taggedFile = open(inputPath, "r+");
taggedContent = taggedFile.read();
taggedFile.close();

taggedWords = taggedContent.split("\n");
wordsWithLB = [];
for word in taggedWords:
  wordsWithLB.append(word.split("\t")[0]);


rsltStr = "";

for word in wordsWithLB:
  if(word == ""):
    rsltStr = rsltStr + "\n";
  else:
    rsltStr = rsltStr + word + " ";

print(rsltStr);


outputFile = open(outputPath, "w+");
outputFile.write(rsltStr);
outputFile.close();
