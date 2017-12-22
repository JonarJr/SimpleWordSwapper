# Swappy Joe's:
# 1. Pick a mode to swap all verbs, all adjectives, all nouns or all
# 2. Enter a sentence or file to read
# 3. The magic of the swap happens and the output is posted to the screen

import Translator

def main():
    print "Welcome to Swappy!"
    wordSwapper = Translator.WordSwapper()
    # do indefinitely
    while True:
        modeSwap = modeRead = inputString = ""
        
        # swap mode
        while modeSwap != "V" and modeSwap != "A" and modeSwap != "N" and modeSwap != "WTF" and modeSwap != "Q":
            modeSwap = raw_input("\nMode: Verb [V], Adjective/Adverbs [A], Noun [N], All [WTF], Quit [Q] \n> ")
            if modeSwap == "Q":
                print "Bye!"
                return
        
        # read mode
        while modeRead != "S" and modeRead != "F":
            modeRead = raw_input("Read from: Sentence [S], File [F] \n> ")
        if modeRead == "S":
            inputString = raw_input("Sentence: ")
        else:
            print "Not supported yet."
            inputString = ""
        wordSwapper.setInputString(inputString)

        if modeSwap == "V":
            wordSwapper.changeAllVerbs()
        elif modeSwap == "A":
            wordSwapper.changeAllAdjectives()
        elif modeSwap == "N":
            wordSwapper.changeAllNouns()
        elif modeSwap == "WTF":
            wordSwapper.changeWTF()

        wordSwapper.display()
        wordSwapper.clearLast()

if __name__ == '__main__':
	main()