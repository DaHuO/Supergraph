T = int( input().strip() )
O = list()
for t in range(T) :
    I = list( input().strip() )
    I.append('+')
    I = list( reversed(I) )
    to = 0
    for i in range( len(I) - 1 ) :
        if I[i] != I[i+1] :
            to += 1
    O.append(to)

for i,o in enumerate(O):
    print('Case #', i+1, ': ', o, sep='')
