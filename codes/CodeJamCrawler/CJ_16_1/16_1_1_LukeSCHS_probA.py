#By Luke Baird for Google CodeJam Round 1a 2016
#problem A - The Last Word

#we are given a string. CAB
#we start with the first letter. Then we build in either direction off of it
#C -> AC or CA
#then we continue doing this until the last letter
#C -> AC or CA -> ACB, BAC, BCA, CAB
#CBA never happens because A & C must be adjacent
#The contestant wins the game if their last word is the last of an alphabetically sorted list of all of the possible last words that could have been produced.
#so CAB would be the solution
#in JAM, MJA would be the solution (J -> JA -> MJA)

#options: generate all possible scenarios. return a list. get the last alphabetically in this list.
#option b: every time, if the letter is greater than the first in the prior, put it before, otherwise put it at the end.
for x in range(int(input())):
    word = input() #say JAM
    wordChar = list(word) # ['J', 'A', 'M']
    builder = ''
    for character in wordChar:
        if len(builder) == 0:
            builder = character
            continue
        mB = list(builder)
        if mB[0] <= character:
            builder = character + builder
        else:
            builder += character

    print(str.format('Case #{}: {}', x+1, builder))