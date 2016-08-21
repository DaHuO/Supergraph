FILENAME = "A-large"
f = open(FILENAME + ".in", "r")
output = open(FILENAME + ".out", "w")
T = int(f.readline())

D = {}
names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
lettersInNumber = {}
letters = {}
numbersWithLetter = {}
letterWhichAppearOnlyInNNames = {}
cnt = 0
for name in names:
    lettersInName = {}
    for letter in name:
        hasLetter = lettersInName.get(letter)
        if hasLetter != None:
            lettersInName[letter] = hasLetter+1
        else:
            lettersInName[letter] = 1

        letterExistsInNumber = numbersWithLetter.get(letter)
        if letterExistsInNumber == None:
            numbersWithLetter[letter] = [cnt]
        else:
            if cnt not in numbersWithLetter[letter]:
                numbersWithLetter[letter].append(cnt)
    lettersInNumber[cnt] = lettersInName
    cnt += 1

print("Letters in Number")
print(lettersInNumber)
print("Numbers with Letter")
print(numbersWithLetter)

for letter in numbersWithLetter:
    l = len(numbersWithLetter[letter])
    item = letterWhichAppearOnlyInNNames.get(l, [])
    item.append(letter)
    letterWhichAppearOnlyInNNames[l] = item
print("letterWhichAppearOnlyInNNames")
print(letterWhichAppearOnlyInNNames)
print("Loop")
for t in range(T):
    word = f.readline().strip()
#    if t < 97:
#        continue
    print(t, "-", word)
    numbersInPhone = []
    numsExplored = []
    lettersInWord = {}
    for letter in word:
        lettersInWord[letter] = lettersInWord.get(letter, 0) + 1
#    print("Letters in word:", lettersInWord)
    for idx in [1, 2, 3, 4, 7]:
        for letter in letterWhichAppearOnlyInNNames[idx]:
            for guess in range(len(numbersWithLetter[letter])):
                num = numbersWithLetter[letter][guess]
                
                if num not in numsExplored:
                    numsExplored.append(num)
                    if letter in lettersInWord:
                        mult = lettersInWord[letter]
#                        print("word has letter", letter, mult, "times. Num: ", num)
                        hasNum = True
                        for letterInNum in lettersInNumber[num]:
                            if lettersInWord.get(letterInNum) == None:
                                hasNum = False
#                                print("Not this num")
                            elif lettersInWord.get(letterInNum) < lettersInNumber[num][letterInNum]:
                                hasNum = False
#                                print("Not this num")
                        repeats = 0
                        while hasNum:
                            repeats += 1
#                            print("Repeats:", repeats)
                            for letterInNum in lettersInNumber[num]:
                                if lettersInWord[letterInNum] >= lettersInNumber[num][letterInNum]:
                                    lettersInWord[letterInNum] -= lettersInNumber[num][letterInNum]
                                    
                                else:
                                    hasNum = False
                                if lettersInWord[letterInNum] == 0:
                                    lettersInWord.pop(letterInNum)
                                    hasNum = False
                        for tmp in range(repeats):
                            numbersInPhone.append(num)
#                        print("New letters in word:", lettersInWord)
    phone = "".join([str(tmp) for tmp in sorted(numbersInPhone)])
    print("Phone:" , phone)
    output.write("Case #%d: %s\n"%(t+1, phone))

f.close()
output.close()
