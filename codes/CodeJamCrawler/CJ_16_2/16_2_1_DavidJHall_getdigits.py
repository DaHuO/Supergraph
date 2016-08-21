import time
# EONNESENRFENIVOU

infilename ='A-large.txt'

numbers = [("6","SIX"),("7","SEVEN"),("5","FIVE"),("8","EIGHT"),("0","ZERO"),("4","FOUR"),("9","NINE"),  ("3","THREE"),  ("2","TWO"),("1","ONE")]
# for i in numbers:
#     print i[0]
# exit(0)


def removeWord(wordToRemove,word):
    #print "Remove "+wordToRemove,word
    for i in wordToRemove:
        word = word.replace(i, "", 1)
    #print word
    return word

print numbers
def solve(word):
    answer = ""
    for key  in numbers:

        loopy = True
        # print numbers[key]+"*'"
        while loopy:
            temptry = word
            for letter in key[1]:

                #print numbers[key]
                if letter in temptry:
                    #print letter, word, True
                    temptry = removeWord(letter,temptry)
                    found = True
                else:
                    #print letter, word, False
                    found = False
                    loopy = False
                    break
            if found:
                #print key
                answer += str(key[0])
                #print "calling remove word"
                word = removeWord(key[1], word)
                #print word
    if len(word)>0:
        print word
    answer=''.join(sorted(answer))

    return answer

timestart = time.time()
iterations = 0
problem = []

f = open(infilename, 'r')
iterations = int(f.readline())
for i in range(0,iterations):
    problem.append( (f.readline().strip()) )



fw = open('large.txt', 'w')
print problem
num = 1
answer = ''
for i in problem:
    answer=str(solve(i))
    # print "Case #"+str(num)+": "+answer
    fw.writelines("Case #"+str(num)+": "+answer+"\n")
    num +=1


print time.time()-timestart

# EFIEOIFRSNVVEUXS   - 155
# FORU
# 4567

