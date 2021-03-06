import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import RegexpParser
import sys

if(len(sys.argv) < 3):
  print("Not enough arguments. GetTextFromTagged.py take two arguments");
  print("Try with: python3 GetTextFromTagged.py <inputFile> <outputFile>");

#Downloading packages
nltk.download('punkt');
nltk.download('averaged_perceptron_tagger');
nltk.download('maxent_ne_chunker');
nltk.download('words');

#Settings
inputPath = sys.argv[1];
outputPath = sys.argv[2];

#Extracting data
file = open(inputPath, "r+");
content = file.read();
file.close();

#Tokenization
tokenizer = PunktSentenceTokenizer();
tokens = tokenizer.tokenize(content);

words = []
tagged = []
namedEnt = []

for sentence in tokens:
  # print(sentence)
  words += nltk.word_tokenize(sentence)
  tagged = nltk.pos_tag(words)
  #Named Entity Recognition
  namedEnt = nltk.ne_chunk(tagged);

#Creating output files
outFile = open(outputPath, "w");
res = ""
for token in namedEnt:
  
  if(type(token) is nltk.tree.Tree):
    #recuperation du type de l'entite nommee
    en = token.label()
    for parts in token:
      outFile.write(parts[0] + "\t" + en + "\n")
  else:
    outFile.write(token[0] + "\t" + "O" + "\n")

outFile.close();