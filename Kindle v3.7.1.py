import string
from typing import Final
import numpy
import itertools


# Opens File
Final_Texts = []
with open(r"C:\Users\mindo\Desktop\My Clippings.txt", encoding = 'cp850') as OpenFile:
    for lines in OpenFile:
        while True:
            try:
                SingleLine = lines.splitlines(True)
                Final_Texts.append(SingleLine)
                break
            except UnicodeDecodeError:
                print('ERROR')


# Indexes Titles
count = int(len(Final_Texts)/5 - 2)
Title_Indexes = [0]
for x in range(0, count):
    NewIndex = Title_Indexes[-1] + 5
    Title_Indexes.append(NewIndex)


# Divides list into sections of 5 for indexing
count = int(len(Final_Texts)/5 - 2)
Text_Indexes = [3]
for x in range(0, count):
    NewIndex = Text_Indexes[-1] + 5
    Text_Indexes.append(NewIndex)


# Take Final_Texts and pull all indexes from it
count = -1
SexyFormat = []
for x in Text_Indexes:
    count = count + 1
    indexer = Text_Indexes[count]
    SexyFormat.append(Final_Texts[indexer])


# Sort quotes by size
def Sorting(SexyFormat):

    lenList = []
    for x in SexyFormat:
        stringy = str(x)
        lenList.append(len(stringy))
    sortedindex = numpy.argsort(lenList)  

    SexyFormat_2 = ['dummy']*len(SexyFormat)

    for i in range(len(SexyFormat)):
              SexyFormat_2[i] = SexyFormat[sortedindex[i]]     
                                          
    return SexyFormat_2

placeholder = Sorting(SexyFormat)
SexyFormat = placeholder


# Writes file with each quote on new line
with open('Org_Notes.txt', 'w', encoding = 'cp850') as wf:
    for lines in SexyFormat:
        lines = str(lines)

        lineLength = len(lines)
        if lineLength <= 25: # Prints words
            wf.write(lines[2:-4] + '\n'*2)
        else: # Prints quotes
            # if len(lines) >= 100:
               # lines = lines + "\n"
            wf.write(lines[2:-4] + '\n'*2 + "*****\n\n") # The indexing removes brackets and shitty old formatting.

# TODO 
    # Remove duplicates
    # Add \n after certain character length on quotes?
        # Not necessary, but pissed I can't find a way to do it. Should just be a .split loop...
    # Sorting by the book they came from.
        # Or pulling the book names up top just as a list
    # How to write a file to a location of my choice?
    # How to auto create quizlet flashcards? Quizlet API? 
        # Hook up vocab words to spellchecker and pair the dictonary def
    # Sexy UI to go with it? Oh man let's overengineer the fuck outta this...