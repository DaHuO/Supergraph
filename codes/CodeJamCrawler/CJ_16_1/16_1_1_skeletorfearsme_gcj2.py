with open("A-.in") as f:
    content = f.readlines()
fo = open("out.txt", "wb")

T=int(content[0])
words=content[1:]
for case in range(T):
    w = list(words[case])
    S=w[0]
    for i in range(1,len(w)):
        if w[i]>=S[0]:
            S=str(w[i])+S
        else:
            S+=str(w[i])
    fo.write("Case #" + str(case+1) + ": " + S)
fo.close()
