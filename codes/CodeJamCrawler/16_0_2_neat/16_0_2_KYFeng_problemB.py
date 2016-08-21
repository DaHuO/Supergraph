f = open('B-large.in', 'r')
fo = open('B-large.out', 'w')
T = int(f.readline())
for caseID in range(1, T+1):
    print(caseID)
    cakes = f.readline()
    flag = cakes[0]
    cnt = 0
    for j in range(0, len(cakes)-2):
        if cakes[j] != cakes[j+1]:
            flag = cakes[j+1]
            cnt += 1
    if flag == '-':
        cnt += 1
    fo.write('Case #{}: {}\n'.format(caseID, cnt))
   
            
