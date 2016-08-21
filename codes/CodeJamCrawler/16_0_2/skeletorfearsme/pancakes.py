with open("b.in") as f:
    content = f.readlines()

T=int(content[0])
stacks=content[1:]
fo = open("out.txt", "wb")
for case in range(0,T):
    i=0
    c=0
    L=list(stacks[case][::-1])
    while i<len(L):
        if L[i] == "-":
            c+=1
            for j in range(i,len(L)):
                if L[j]=="-":
                    L[j]="+"
                else:
                    L[j]="-"
        i+=1
    fo.write("Case #" + str(case+1) + ": " + str(c) + "\n")
fo.close()
