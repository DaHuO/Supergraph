import argparse
import random
parser = argparse.ArgumentParser()
parser.add_argument("path", help="path of the input file")
args = parser.parse_args()
inputPath = args.path

f = open(inputPath, 'r')

possible_words = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}

def canConstructWord(word, available_letters):
    present_letter = {}
    for letr in word:
        if letr in present_letter:
            present_letter[letr] += 1
        else:
            present_letter[letr] = 1
        if letr not in available_letters or (available_letters[letr] - present_letter[letr] + 1) == 0:
            return False
    return True

def isEmpty(dictionary):
    for key in dictionary.keys():
        if dictionary[key] != 0:
            return False
    return True

f.readline()
i = 1
for line in f:
    line = line.rstrip()
    canStop = False
    while(not canStop):
        nbr = []
        available_letters = {}
        for letter in line:
            if letter in available_letters:
                available_letters[letter] += 1
            else:
                available_letters[letter] = 1
        keys = list(possible_words.keys())
        random.shuffle(keys)
        for word in keys:
            while canConstructWord(word, available_letters):
                for let in word:
                    available_letters[let] -= 1
                nbr.append(possible_words[word])
        nbr.sort()
        canStop = isEmpty(available_letters)
        if(canStop):
            print("Case #" + str(i) + ": " + ''.join(str(x) for x in nbr))
            i += 1


f.close()