import random
def new_word( s ):
    word = ""
    for x in s:
        if "" == word or word[0] <= x:
            word = x + word
        else:
            word = word + x
    return word

answers=[]
N = int(input())
for i in range(0, N):
    s = input()

    word = new_word(s)

    answers.append(word)
# print(answers)

f = open('submission.txt','w')
for i in range(0, len(answers)):
    f.write("Case #"+str(i+1)+": "+str(answers[i])+'\n')
f.close()
