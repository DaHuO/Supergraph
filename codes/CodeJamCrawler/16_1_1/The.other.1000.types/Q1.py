in_file = 'A-large.in'
Type = 'large'
out_file = 'A-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

Tt = int(data[0])
del data[0]

OUT = []
for k in range(Tt):
    S = list(data[k])[:-1]
    Last = [S[0]]
    del S[0]
    for i in S:
        if i >= Last[0]:
            Last.insert(0, i)
        else:
            Last.append(i)
    OUT.append(''.join(Last))
    pass

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i]))