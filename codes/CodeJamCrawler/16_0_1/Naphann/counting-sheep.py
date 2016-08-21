T = int(input())
s = set()
output = open('a-large-output.txt','w')

def insert_to_set(n):
    list(map(lambda x: s.add(x), n))

for t in range(1,T+1):
    s.clear()
    n = int(input())
    insert_to_set(str(n))
    old_n = n
    if n == 0:
        print('Case #%d: INSOMNIA' % t)
        output.write('Case #%d: INSOMNIA\n' % t)
        continue
    while len(s) != 10:
        n += old_n
        insert_to_set(str(n))
    print('Case #{0}: {1}'.format(t,n))
    output.write('Case #{0}: {1}\n'.format(t,n))
output.close()