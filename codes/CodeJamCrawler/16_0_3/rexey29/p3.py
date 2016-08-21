import itertools
l = []
count = 0
print('Case #1:')
def basecal(num, base):
    s = 0
    for x in range(1, len(num)+1):
        s += int(num[-x])*(base**(x-1))
    return s
for combination in itertools.product([0,1], repeat=14):
    l.append('1'+''.join(map(str, combination))+'1')
while count < 50:
    for x in l[:]:
        num = x
        dic = {}
        st = num
        for x in range(2, 11):
            basex = basecal(num, x)
            flag = False
            for y in range(2,1000):
                if int(basex)%y == 0:
                    dic[x] = y
                    flag = True
                    break
                else:
                    flag = False
            if not flag:
                break
        if flag:
            for x in range(2,11):
                st += ' {}'.format(dic[x])
            print(st)
            count += 1
        if count == 50:
            break



