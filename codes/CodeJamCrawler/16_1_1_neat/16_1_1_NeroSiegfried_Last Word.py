f = open('Last Word.txt', 'w')
T = int(raw_input())
for i in range(T):
    S=raw_input()
    first=' '
    last=''
    for j in S:
        if ord(j)>=ord(first):
            first=j
            last=j+last
        else:
            last=last+j
    print last
    f.write("Case #"+str(i+1)+": "+last+"\n")
    
