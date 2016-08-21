def flip(pancake):
    lp=[pancake[0]]
    for x in range(len(pancake)-1):
        if (pancake[x]!=pancake[x+1]):
            lp.append(pancake[x+1])

    if (lp[-1] == '+'):
        lp.pop()
        
    ps=''.join(lp)

    return len(ps)

def pancake(file):
    f=open(file)
    g=open('output.ou',mode='w')
    b=int(f.readline()[:-1])
    for x in range(b):
        m = f.readline()[:-1]
        c=flip(m)
        g.write("Case #"+str(x+1)+": "+str(c)+"\n")
    f.close()
    g.close()

