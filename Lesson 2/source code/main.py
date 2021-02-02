# Elizabeth Nastoff
# ICP 2

import string
import collections

# Part 1
# take a list of heights in feet and convert them to cm
def feetToCm():
    print("Enter a list of heights (feet) then type 'D' when finished")
    heights = []
    inputValue = "Y"
    while inputValue != 'D':
        inputValue = input()
        if (inputValue.isalpha() == False):
            heights.append(float(inputValue))
    heightsCM = []
    for x in heights:
        heightsCM.append(round((x * 30.48),2))
    print("Heights as feet: ", heights)
    print("Heights as CM ", heightsCM)

    return 0

# Part 2
# Given a non-negative integer num, return the number of steps to reduce it to zero
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

def reduceToZero():
     value = int(input("Enter a number to reduce to zero"))
     stepCount = 0
     while value != 0:
         stepCount +=1
         if value % 2 == 0:
             value = value/2
             print (stepCount, ")", value*2, " is Even, divide by 2 to obtain ", value)
         else:
             value = value - 1
             print (stepCount, ")", value+1, "is odd, subtract 1 to obtain", value)
     return 0

# Part 3
# take an input file and out put the word count
def wordCount():
    file = open("sampletext.txt", "r")
    wordsDict = dict()
    for line in file:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split(" ")

        for word in words:
            if not word.isalpha():
                words.remove(word)
                pass
            elif word in wordsDict:
                wordsDict[word] = wordsDict[word] + 1
            else:
                wordsDict[word] = 1

    # Sorted the dictionary so the highest counts are first
    sort = sorted(wordsDict.items(), key=lambda kv: kv[1], reverse=True)
    count = collections.OrderedDict(sort)
    for key in count:
        print(key, ":", count[key])

if __name__ == '__main__':
    feetToCm()
    reduceToZero()
    wordCount()
