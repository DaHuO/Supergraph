T = int(raw_input())
for t in xrange(T):
    pancake=raw_input()
    signswitch=0
    for i in xrange(len(pancake)-1):
        if pancake[i]!=pancake[i+1]:
            signswitch+=1
    if pancake[-1]=='-':
        signswitch+=1
    print("Case #{}: {}".format(t+1, signswitch))