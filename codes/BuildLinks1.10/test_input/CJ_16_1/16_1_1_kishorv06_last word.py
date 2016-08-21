v = raw_input()
L = v.split()[0]
i = 1
while(i <= int(L) ):
    text = raw_input()
    val = []
    val.append(text[0])
    first = text[0]
    for c in text[1:]:
        if (c < first) :
            val.append(c)
        else:
            val.insert(0,c)
            first = c
    print "Case #{0}: {1}".format(i,''.join(val))
    i +=1
