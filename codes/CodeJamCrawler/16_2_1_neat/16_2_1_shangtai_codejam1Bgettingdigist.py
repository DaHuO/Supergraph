T = int(raw_input())
for t in xrange(T):
    phonestring=raw_input()
    stringlen=len(phonestring)
    stringdict=dict()
    numberlist=[0 for i in xrange(10)]
    for i in phonestring:
        stringdict[i]=stringdict.get(i,0)+1
    def fillinnumberlist(checkletter,stringtoreduce,numbertoincrease):
        if checkletter in stringdict and stringdict[checkletter]>0:
            n=stringdict[checkletter]
            for j in stringtoreduce:
                stringdict[j]-=n
            numberlist[numbertoincrease]+=n
    fillinnumberlist('Z', 'ZERO', 0)
    fillinnumberlist('W', 'TWO', 2)
    fillinnumberlist('U', 'FOUR', 4)
    fillinnumberlist('X', 'SIX', 6)
    fillinnumberlist('G', 'EIGHT',8)
    fillinnumberlist('F', 'FIVE', 5)
    fillinnumberlist('T', 'THREE', 3)
    fillinnumberlist('O', 'ONE', 1)
    fillinnumberlist('S', 'SEVEN', 7)
    fillinnumberlist('I', 'NINE', 9)
    phonenumber=""
    for i in xrange(10):
        phonenumber+=numberlist[i]*str(i)
    print("Case #{}: {}".format(t+1, phonenumber))