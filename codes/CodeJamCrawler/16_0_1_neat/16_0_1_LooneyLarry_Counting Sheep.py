# Google Code Jam 2016 Qualifying A
def digits(num):
    result = []
    while num != 0:
        result += [num % 10]
        num = num / 10
    return result

def doCase(n):
    if n == 0: return 'INSOMNIA'
    needed = range(10)          # Digits not yet seen
    value = 0
    while needed:
        value += n
        for dig in digits(value):
            if dig in needed:
                needed.remove(dig)
    return value

cases = int(raw_input())
for i in range(cases):
    print 'Case #{}: {}'.format(i+1, doCase(int(raw_input())))
