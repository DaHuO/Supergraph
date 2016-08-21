input = '''50
3
1 2 3
2 3 5
'''


def rank(rows):
    list = []
    for i in rows:
        for j in i:
            if j in list:
                list.remove(j)
            else:
                list.append(j)
    return ' '.join(map(str,sorted(list)))
split = input.splitlines()
t = int(split[0])
curr = 1
for i in range(t):
    rows = []
    n = int(split[curr])
    curr += 1
    for j in range(2*n-1):
        rows += [[int(k) for k in split[curr].split()]]
        curr += 1
    print 'Case #%i: ' % (i+1) + rank(rows)
        
# for i in range(1, int(split[0])+1):
    # print 'Case #%i: ' % i + rank(split[i])