import sys

fd = open(sys.argv[1], 'r')

NUMS = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

def sub(num, mix):
    if num in ['THREE','SEVEN']:
        if mix.count('E') < 2:
            return False

    for i in num:
        if i not in mix:
            return False
    return True

ncases = int(fd.readline()[:-1])

for case in range(1, ncases+1):

    mixpnum = list(fd.readline()[:-1])

    pnum = []
    while 'Z' in mixpnum:
        pnum.append('0')
        for i in 'ZERO':
            mixpnum.remove(i)

    while 'W' in mixpnum:
        pnum.append('2')
        for i in 'TWO':
            mixpnum.remove(i)

    while 'X' in mixpnum:
        pnum.append('6')
        for i in 'SIX':
            mixpnum.remove(i)

    while 'G' in mixpnum:
        pnum.append('8')
        for i in 'EIGHT':
            mixpnum.remove(i)

    for num in ['SEVEN','THREE', 'FIVE', 'FOUR', 'NINE', 'ONE']:
        if not mixpnum:
            break
            
        while sub(num, mixpnum):
            pnum.append(str(NUMS.index(num)))

            for i in num:
                mixpnum.remove(i)

    pnum.sort()    
    print("Case #" + str(case) + ":", ''.join(pnum))
            
