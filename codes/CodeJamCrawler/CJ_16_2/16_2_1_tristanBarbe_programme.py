f = open('data.in', 'r')
f2 = open('output.in', 'w')
nb = int(f.readline())
list_value = []
for i in range(nb):
    list_value.append(f.readline())

print list_value

for idx,v in enumerate(list_value):
    machaine = v
    nb = 0
    nb0 = machaine.count('Z')
    machaine=machaine.replace('Z','',nb0)
    machaine=machaine.replace('E','',nb0)
    machaine=machaine.replace('R','',nb0)
    machaine=machaine.replace('O','',nb0)

    nb2 = machaine.count('W')
    machaine=machaine.replace('T','',nb2)
    machaine=machaine.replace('W','',nb2)
    machaine=machaine.replace('O','',nb2)

    nb4 = machaine.count('U')
    machaine=machaine.replace('F','',nb4)
    machaine=machaine.replace('U','',nb4)
    machaine=machaine.replace('R','',nb4)
    machaine=machaine.replace('O','',nb4)

    nb6 = machaine.count('X')
    machaine=machaine.replace('S','',nb6)
    machaine=machaine.replace('I','',nb6)
    machaine=machaine.replace('X','',nb6)

    nb8 = machaine.count('G')
    machaine=machaine.replace('I','',nb8)
    machaine=machaine.replace('E','',nb8)
    machaine=machaine.replace('G','',nb8)
    machaine=machaine.replace('H','',nb8)
    machaine=machaine.replace('T','',nb8)

    nb5 = machaine.count('F')
    machaine=machaine.replace('F','',nb5)
    machaine=machaine.replace('I','',nb5)
    machaine=machaine.replace('V','',nb5)
    machaine=machaine.replace('E','',nb5)

    nb7 = machaine.count('V')
    machaine=machaine.replace('S','',nb7)
    machaine=machaine.replace('E','',2*nb7)
    machaine=machaine.replace('V','',nb7)
    machaine=machaine.replace('N','',nb7)

    nb1 = machaine.count('O')
    machaine=machaine.replace('E','',nb1)
    machaine=machaine.replace('N','',nb1)
    machaine=machaine.replace('O','',nb1)

    nb9 = machaine.count('I')
    machaine=machaine.replace('I','',nb9)
    machaine=machaine.replace('N','',nb9*2)
    machaine=machaine.replace('E','',nb9)

    nb3 = machaine.count('T')
    machaine=machaine.replace('H','',nb3)
    machaine=machaine.replace('E','',nb3*2)
    machaine=machaine.replace('T','',nb3)
    machaine=machaine.replace('R','',nb3)


    res = '0'*nb0 + '1'*nb1+'2'*nb2+'3'*nb3+'4'*nb4+'5'*nb5+'6'*nb6+'7'*nb7+'8'*nb8+'9'*nb9
    f2.write('Case #{0}: {1} \n'.format(idx+1,res) )

f.close()
f2.close()
