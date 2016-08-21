f = open('data.in', 'r')
f2 = open('output.in', 'w')
nb = int(f.readline())
list_value = []
for i in range(nb):
    list_value.append(f.readline())
    list_value[i] =  list_value[i][0:( len(list_value[i]) - 1)]
    list_value[i] = [int(s) for s in list_value[i].split() if s.isdigit()]

print list_value

for idx,v in enumerate(list_value):
    K = v[0]
    C = v[1]
    S = v[2]
    if S < K:
        f2.write('Case #{0}: {1} \n'.format(idx+1,'IMPOSSIBLE') )
    else:
        maliste = range(1,1+K)
        f2.write('Case #{}:'.format(idx+1))
        for el in maliste:
            f2.write(' {}'.format(el))
        f2.write('\n')


f.close()
f2.close()
