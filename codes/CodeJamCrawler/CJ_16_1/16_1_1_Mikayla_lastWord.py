def lastWord(word):
    if len(word) < 2:
        return word
    newWord = word[0]
    word = word[1:]
    for letter in word:
        if letter > newWord[0]:
            newWord = letter + newWord
        elif letter < newWord[0]:
            newWord = newWord + letter
        else:
            try:
                if letter >= newWord[1]:
                    newWord = letter + newWord
                else:
                    newWord = newWord + letter
            except:
                newWord = newWord + letter
    return newWord


with open("A-large.in", "r") as f:
    nCases = int(f.readline())
    with open("A-large.out", "w") as fout:
        for iCase in range(nCases):
            word = f.readline().strip()
            print("Case #%d: %s" % (iCase+1, lastWord(word)), file=fout)

# print(flippingPancakes('-')) # 1
# print(flippingPancakes('-+')) # 1
# print(flippingPancakes('+-')) # 2
# print(flippingPancakes('+++')) # 0
# print(flippingPancakes('--+-')) # 3
