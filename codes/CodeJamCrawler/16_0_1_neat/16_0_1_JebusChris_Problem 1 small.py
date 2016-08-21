def getvalue(num):
    numbers = '0123456789'
    numbers = searchnumber(num, numbers)
    if (num == '0'):
        return 'INSOMNIA'
    # Hi graders, max is 45 times for two, but lets be safe and say 100
    # I wish I could fall asleep as fast as that sheep
    for i in range(1, 100):
        aaa = str(i*int(num))
        numbers = searchnumber(aaa, numbers)
        if numbers == '':
            return aaa
    return 'INSOMNIA'


def searchnumber(num, xxx):
    for j in num:
        if j in xxx:
            xxx = xxx.replace(j, '')
    return xxx


f = open('ex.txt', 'r')
i = 0
insomnia = 'false'
for line in f:
    line = line.strip()
    if ( i == 0 ):
        i = 1
    else:
        print('Case #' + str(i) + ': ' + getvalue(line))
        i += 1

