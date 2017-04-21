"""
:Author: Pravallika
:Description: Python code to convert a given string/document into a dictionary

:Instructions to run:
    1. python3 dictionary.py filename1.txt filename2.txt
    2. python3 dictionary.py
        >> Please enter fileName: filename.txt
    3. python3 dictionary.py
        >> Please enter fileName:
        >> Will run some dictionary creation for default string embedded in the code as an sample
"""

import re
import sys
from sortedcontainers import SortedDict


class Word(object):
  def __init__(self):
    self.frequency = 1
    self.sentenceNumbers = []

  def addSentenceNumber(self, sentenceNumber):
    self.sentenceNumbers.append(sentenceNumber)

  def __str__(self):
    if self:
      return "%s:%s" % (self.frequency, self.sentenceNumbers)

class Dictionary(object):

  def __init__(self):
    self.concordance = SortedDict()

  def createDictionaryFromFile(self, documentPath):
    file = open(documentPath, "r")
    self.createDictionary(file.read())

  def createDictionary(self, inputDocument):
    """
    :type inputDocument: str
    :rtype: collection
    """

    if inputDocument == "":
      return self.concordance

    words = inputDocument.split(" ")

    sentenceNumber = 1

    self.createWord(words[0], sentenceNumber)

    for i in range(1, len(words)):

      if words[i-1].count('.') == 1 and words[i-1][-1] == "." and words[i][0].isupper():
          sentenceNumber += 1

      currentWord = words[i].lower()

      if currentWord != "i.e.":
        currentWord = re.sub(r'(^\W+)|(\W+$)', '', currentWord)

      if currentWord in self.concordance:
        self.updateWord(currentWord, sentenceNumber)
      else:
        self.createWord(currentWord, sentenceNumber)

    return self.concordance

  def getWord(self, word):
    return self.concordance[word]

  def createWord(self, word, sentenceNumber):
    self.concordance[word] = Word()
    self.concordance[word].addSentenceNumber(sentenceNumber)

  def updateWord(self, word, sentenceNumber):
    self.getWord(word).frequency += 1
    self.getWord(word).addSentenceNumber(sentenceNumber)

  def printDictionary(self):
    index = 0
    counter = 1
    for word,details in self.concordance.items():
      currentLabel = chr(ord('a') + index) * counter
      print(currentLabel+". "+word+"\t{"+str(details)+"}")
      index += 1
      if index == 26:
        index = 0
        counter += 1

  def removeWord(self, word):
    word = word.lower()
    self.concordance.pop(word, None)




inputString = "This sentence works too. I am just inline sentence. I love to be invoked directly. Isn't this cool code?"
#Create with string directly
#obj.createDictionary(inputString)

#Create with fileName as command line argument
documentPath = ""
if(len(sys.argv) > 1):
    for i in range(1,len(sys.argv)):
        print("=============Dictionary for Doc:"+sys.argv[i]+" starts ==================")
        obj = Dictionary()
        obj.createDictionaryFromFile(sys.argv[i])
        obj.printDictionary()
        print("=============Dictionary for Doc:"+sys.argv[i]+" ends ==================")
else:
    documentPath = input("Please enter fileName:")
    obj = Dictionary()

    if(documentPath):
        print("=============Dictionary for Doc:"+documentPath+" starts ==================")
        obj.createDictionaryFromFile(documentPath)
        obj.printDictionary()
        print("=============Dictionary for Doc:"+documentPath+" ends ==================")
    else:
        print("=============Dictionary for String:"+inputString+" ==================")
        obj.createDictionary(inputString)
        obj.printDictionary()
