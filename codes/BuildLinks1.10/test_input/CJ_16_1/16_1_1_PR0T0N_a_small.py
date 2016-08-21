import random
n = input()
for case in range(1,n+1):
    S = list(raw_input())
    len_s = len(S)
    word = list(S[0])
    for i in range(1,len_s):
        if(S[i] >= word[0]):
            word.insert(0,S[i])
        else:
            word.append(S[i])

    print ("Case #{}: {}".format(case,"".join(word)))



