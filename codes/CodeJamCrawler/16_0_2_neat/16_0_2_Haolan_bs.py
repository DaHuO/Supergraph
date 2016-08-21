times = int(input())
for t in range(times):
    pans = raw_input()
    size = len(pans)
    if size == 0:
        print 'Case #'+str(t+1)+': 0'
        continue
    i = 0
    cur = pans[i]
    rev = 1
    while i < size:
        if pans[i] != cur:
            cur = pans[i]
            rev += 1
        i += 1
    if pans[-1] == '+':
        rev -= 1 
    print 'Case #'+str(t+1)+': '+str(rev)
