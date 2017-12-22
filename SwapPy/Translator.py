from PyDictionary import PyDictionary
from nltk.corpus import brown
from nltk.tag import pos_tag
from nltk import word_tokenize
from random import *
#TODO USE EN for verbs
from pattern import en

class WordSwapper():
    def __init__(self):
        self.dictionary = PyDictionary()
        self.outputString = "New Phrase:"

        # Categorize all the options for the three parts of speech.
        self.verbOptions = ["VB", "VBP", "VBD", "VBG", "VBN", "VBZ"]
        self.nounOptions = ["NN", "NNS", "NNP", "NNPS"]
        self.adOptions = ["JJ", "JJR", "JJS", "RB", "RBR", "RBS"]

        self.inputString = ""
        self.tokens = []
        self.tags = []

    # Requires that the user sets the input string before changing any words.
    def setInputString(self, inputString):
        self.inputString = inputString
        self.tokens = word_tokenize(inputString)
        self.tags = pos_tag(self.tokens)
        
    # Call any of these on a set input string to do a swappy.
    def changeAllVerbs(self): 
        self.__randomTranslator__(self.verbOptions, self.tags)
        
    def changeAllAdjectives(self):
        self.__randomTranslator__(self.adOptions, self.tags)

    def changeAllNouns(self):
        self.__randomTranslator__(self.nounOptions, self.tags)

    def changeWTF(self):
        self.__randomTranslator__(self.verbOptions + self.adOptions + self.nounOptions, self.tags)

    # Handle logic to get random synonyms to swap to based on the options; concatenates results to the outputString.
    def __randomTranslator__(self, options, tags):
        for word,tag in tags:
            if tag in options:
                synList = self.dictionary.synonym(word)
                if len(synList) != 0:
                    random_index = randrange(0, len(synList))
                    replaceWord = synList[random_index]
                    self.outputString = self.outputString + " " + replaceWord
            # handle punctuation
            elif tag == "." or tag == ":" or tag == ",":
                self.outputString += word
            else:
                self.outputString = self.outputString + " " + word

    # Display the most recent output for the user.
    def display(self):
        print self.outputString
        
    # Clear the last entry
    def clearLast(self):
        self.outputString = "New Phrase:"
        