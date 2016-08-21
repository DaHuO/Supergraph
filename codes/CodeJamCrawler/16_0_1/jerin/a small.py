def remove_num(n,num):
    for i in str(n):
        if int(i) in num:
            num.remove(int(i))
    return num
for _ in range(input()):
    n = input()
    num = [i for i in range(10)]
    if n == 0:
        print 'Case #%d: INSOMNIA'%(_+1)
    else:
        num = remove_num(n,num)
        nn = n
        while len(num)>0:
            nn+=n
            num = remove_num(nn,num)
        print 'Case #%d:'%(_+1),nn
            
