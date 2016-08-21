ninput = int(raw_input())
for z in range(ninput):
    vec = raw_input()
    l = len(vec)

    optv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    search_order = [['Z', 'W', 'U', 'X', 'G', 'F', 'V', 'H', 'O', 'N' ], [0,2,4,6,8,5,7,3,1,9]]

    nb = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']


    for i in range(10):
        for j in range(l):
            if vec[j] == search_order[0][i]:
                optv[ search_order[1][i] ] +=1

                for k in range(len(nb[ search_order[1][i] ])):
                    for x in range(l):
                        if vec[x] == nb[ search_order[1][i] ][k]:
                            vec = vec[:x] + 'K' + vec[(x+1):]
                            break

    print "Case #"+str(z+1)+":",
    st = ""
    for i in range(10):
        if optv[i] != 0:
            st += str(i)*optv[i]
    print st

