def func(s,c):
    counter = 1
    for i in range(1,len(s)):
        if s[i] == c:
            counter=counter+1
        else:
            break
    return counter

    
t = int(raw_input())
for i in range(1,t+1):
    s = raw_input()
    length = len(s)
    j = 0
    if '-' in s:
        if len(s) == 1:
            j =1
        else:
            for j in range(1,length+1):
                firstchar = s[0]
                toflip = func(s,firstchar)
                s= s.replace(toflip*firstchar,toflip* '-' if firstchar == '+' else '+',1)
                #print s
                if '-' not in s:
                    break    
    print "Case #"+str(i)+": "+str(j)