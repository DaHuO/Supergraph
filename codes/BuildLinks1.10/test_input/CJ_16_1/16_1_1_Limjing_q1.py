def last_word(word):
    #print list(word)
    wordlist = list(word)
    ans = ""
    start = wordlist[0]
    for i in range(len(wordlist)):
        if wordlist[i]>=start:
            ans = wordlist[i]+ans
            start = wordlist[i]
        else:
            ans += wordlist[i]
    return ans



nCases = int(raw_input())
for i in range(nCases):
    word = raw_input()
    #last_word(word)
    print "Case #"+str(i+1)+": "+last_word(word)

