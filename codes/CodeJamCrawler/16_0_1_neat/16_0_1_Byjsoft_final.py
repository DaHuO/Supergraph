def exist(x):
    global now
    for i in list(str(x)):
        now[int(i)] += 1
    if 0 in now:
        return True
    else: return False

num = int(input())
count = 0

for cases in range(1,num+1):
    n = int(input())
    count += 1
    if n == 0:
        print('Case #'+str(count)+': INSOMNIA\n')
        continue
    now = [0,0,0,0,0,0,0,0,0,0]

    for i in list(str(n)):
        now[int(i)] += 1

    multi = 2

    while exist(multi*n):
        multi += 1

    print('Case #'+str(count)+': '+str(multi*n)+'\n')