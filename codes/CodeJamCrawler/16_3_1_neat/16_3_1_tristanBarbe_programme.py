import string


with open('data.in','r') as f:
    cases=int(f.readline())
    lines=f.readlines()

f2 = open('output.in', 'w')
for i in range(cases):
    liste_parti = string.ascii_uppercase
    dict_parti = list((key,int(value)) for key,value in zip(liste_parti,lines[2*i+1].strip().split(' ')))
    out = []
    print dict_parti
    while True:
        dict_parti = sorted(dict_parti,key = lambda x :-x[1])
        x = dict_parti[0][1]
        y = dict_parti[1][1]
        z = sum([w[1] for w in dict_parti])-x-y
        if len(dict_parti) >2:
            v = dict_parti[2][1]
        else:
            v = 0

        if x == 0:
            break
        
        if y <= x+z-2:
            out.append((dict_parti[0][0],dict_parti[0][0]))
            dict_parti[0] = (dict_parti[0][0],dict_parti[0][1]-2)

                
        elif v <= x+y-2:
            out.append((dict_parti[0][0],dict_parti[1][0]))
            dict_parti[0] = (dict_parti[0][0],dict_parti[0][1]-1)
            dict_parti[1] = (dict_parti[1][0],dict_parti[1][1]-1)

        else :
            out.append((dict_parti[0][0]))
            dict_parti[0] = (dict_parti[0][0],dict_parti[0][1]-1)

    res = ''
    for g in out:
        for j in g:
            res += str(j)
        res += ' '
    print res
    f2.write('Case #{0}: {1} \n'.format(i+1,res ))
    

    
f.close()
f2.close()
