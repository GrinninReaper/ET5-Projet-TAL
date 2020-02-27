import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import RegexpParser
import os

os.chdir("..");

inputPathTags = "data/POSTags_PTB_Universal_Linux.txt"
inputPath1 = "data/pos_reference.txt.lima2"
outputPath1 = "data/pos_reference.txt.univ";

inputFileTags = open(inputPathTags, "r+");
contentTags = inputFileTags.read();
inputFileTags.close();

inputFile1 = open(inputPath1, "r+");
content1 = inputFile1.read();
inputFile1.close();

nltk.download('averaged_perceptron_tagger');

contentSplitTags = contentTags.split();
#print("After Split:",contentSplitTags);
arrayTagsKeys=[];
arrayTagsValues=[];
for i in range(len(contentSplitTags)):
  if(i%2==0):
    arrayTagsKeys.append(contentSplitTags[i])
  else:
    arrayTagsValues.append(contentSplitTags[i])

#print("arrayTagsKeys:",arrayTagsKeys);
#print("\narrayTagsValues:",arrayTagsValues);

contentSplitSpace1 = content1.split('\n');
arrayContentKeys1=[];
arrayContentValues1=[];
for i in range(len(contentSplitSpace1)):
  if(contentSplitSpace1[i] == ""):
    arrayContentKeys1.append("\n")
    arrayContentValues1.append("")
  else:
    contentSplitTab= contentSplitSpace1[i].split('\t');
    for j in range(len(contentSplitTab)-1):
      arrayContentKeys1.append(contentSplitTab[j])
      arrayContentValues1.append(contentSplitTab[-1])
#print("\nAfter Split:",contentSplit1);

print("\n");
writeTag = False;
tagToWrite = "";
#Creating output files:
outFile1 = open(outputPath1, "w+");
for j in range(len(arrayContentKeys1)):
  for i in range(len(arrayTagsKeys)):
    if(arrayContentValues1[j] == arrayTagsKeys[i]):
      tagToWrite = arrayTagsValues[i]
      #print("arrayContentValues1[i]="+arrayContentValues1[j]+" arrayTagsKeys[i]=" + arrayTagsKeys[i] + " tagToWrite=" + tagToWrite)
      writeTag = True
  if(writeTag):
    outFile1.write(arrayContentKeys1[j] + "\t");
    outFile1.write(tagToWrite + "\n");
    writeTag = False;
  else:
    if(arrayContentKeys1[j] == "\n"):
      outFile1.write("\n");
outFile1.close();

print("\nFIN");
print("\n");
