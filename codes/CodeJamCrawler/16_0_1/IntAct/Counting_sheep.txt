n = int(raw_input())
numbers = ['0','1','2','3','4','5','6','7','8','9']
for i in xrange(1, n+1):
    check = []
    looper = False
    nu = raw_input()
    for j in xrange(1,10000):
        s_count = str(j*(int(nu)))
        for el in s_count:
            if el in numbers and el not in check:
                check.append(el)
            if len(check) == 10:
                print('Case #'+str(i)+': '+s_count)
                looper = True
                break
            if looper:
                break
        if looper:
                break
    if looper == False:
        print('Case #'+str(i)+': INSOMNIA')