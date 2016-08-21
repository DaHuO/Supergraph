f = open('data.in', 'r')
f2 = open('output.txt', 'w')
nb = int(f.readline())
list_value = []
for i in range(nb):
    list_value.append(f.readline())
    list_value[i] =  list_value[i][0:( len(list_value[i]) - 1)]

print list_value

for idx,v in enumerate(list_value):
    taille = len(v)
    print v
    v += '+'
    print v
    compteur = 0
    for i in range(taille):
        compteur += (1 if v[i] != v[i+1] else 0)
    print compteur
    f2.write('Case #{0}: {1} \n'.format(idx+1,compteur) )

f.close()
f2.close()
    
