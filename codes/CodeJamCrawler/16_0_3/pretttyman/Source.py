LOCAL = 'input.txt'
NOT_LOCAL = 'tests.in'


def convert(num, base):
    res = 0
    power = 1
    while num:
        if num % 2:
            res += power
        power *= base
        num //= 2
    return res


def getDivisor(num):
    for div in range(2, 100):
        if num % div == 0:
            return div
    return -1


inp = open(LOCAL, 'r')
outp = open('output.txt', 'w')

print("Case #1:", file=outp)

len, need = map(int, inp.readline().split())
made = 0
for num in range(2 ** (len - 1) + 1, 2 ** len, 2):
    if (made == need):
        break
    divs = []
    good = True
    for base in range(2, 11):
        cur_num = convert(num, base)
        div = getDivisor(cur_num)
        if div == -1:
            good = False
            break
        divs.append(div)

    if good == True:
        made += 1
        print(bin(num)[2:], file=outp, end=' ')
        print(*divs, file=outp)


inp.close()
outp.close()

























