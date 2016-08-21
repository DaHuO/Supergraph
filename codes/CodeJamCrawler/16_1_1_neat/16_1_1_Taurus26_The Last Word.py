File=open("A-large.txt",'w')

T=int(raw_input())
for t in range(T):
    S=raw_input()
    lastword=[S[0]]
    for n in range(1,len(S)):
        if S[n]>=lastword[0]:
            lastword.reverse()
            lastword.append(S[n])
            lastword.reverse()
        else:
            lastword.append(S[n])
    Lastword=''.join(lastword)
    print >> File, "Case #%d: %s" %(t+1,Lastword)
File.close()
