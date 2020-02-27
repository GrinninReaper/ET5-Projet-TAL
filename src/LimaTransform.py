import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import RegexpParser
 

inputPath1 = "data/pos_reference.txt.lima"
outputPath1 = "data/pos_reference.txt.lima2";

inputFile1 = open(inputPath1, "r+");
content1 = inputFile1.read();
inputFile1.close();

nltk.download('averaged_perceptron_tagger');

arrayTagsKeys=["SCONJ","SENT","COMMA", "COLON", "PROPN","AUX", "ADJ", "VERB", "DET", "ADP", "NOUN", "PART", "CONJ", "OQU", "QUOT"];
arrayTagsValues=["CC",".",",",":", "NNP", "MD","JJ", "VB", "DT", "IN", "NN", "POS", "CC", ".", "."];

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
      wordsInContent = contentSplitTab[0].split(" ")
      tagToAdd = contentSplitTab[-1]
      for k in range (len(wordsInContent)):
        arrayContentKeys1.append(wordsInContent[k])
        arrayContentValues1.append(tagToAdd)

# for word in contentSplitSpace1:  
#   if(word == ""):
    # print("---",word);
#print("\narrayContentKeys1[0] = :",arrayContentKeys1[0]);
#print("\arrayContentKeys1 = :",arrayContentKeys1);
#print("\arrayContentValues1 = :",arrayContentValues1);

print("\n");
writeTag = False;
tagToWrite = "";

#print("taille arrContentKeys = " + str(len(arrayContentKeys1)));
#print("taille arrayContentValues = " + str(len(arrayContentValues1)));
#print("taille arrayTagsKeys = " + str(len(arrayTagsKeys)));
#print("taille arrayTagsValues = " + str(len(arrayTagsValues)));

chaine = ""


# print("\n");
# writeTag = False;
# tagToWrite = "";
# #Creating output files:
outFile1 = open(outputPath1, "w");
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

# contentOutputFile = content1;


# for i in range(len(arrayTagsKeys)):
#   contentOutputFile.replace("DET", "DT");
# print(contentOutputFile.replace("DET", "DT"));  

# outFile1.write(contentOutputFile);
# outFile1.close();

# string = "geeks for geeks geeks geeks geeks" 
   
# # Prints the string by replacing geeks by Geeks  
# print(string.replace("geeks", "Geeks"))  
