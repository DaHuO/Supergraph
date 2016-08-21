import sys


def process(num):
    if num == 0:
        return 'INSOMNIA'
    chsum = 45
    tmp = [False] * 10
    for c in str(num):
        if not tmp[int(c)]:
                chsum = chsum - int(c)
                tmp[int(c)] = True

    if chsum == 0 and tmp[0]:
        return num

    for i in range(2, 1000):
        c_num = num * i
        for c in str(c_num):
            if not tmp[int(c)]:
                chsum = chsum - int(c)
                tmp[int(c)] = True
        if chsum == 0 and tmp[0]:
            return c_num

if __name__ == '__main__':
    res = ''
    i = 0
    with open('A-large.in', 'r') as file:
        first = True
        for line in file:
            if first:
                first = False
                continue;
            i = i + 1
            res = res + ("Case #%s: %s\n" % (i, process(int(line))))

    with open('output', 'w+') as file:
        print res
        file.write(res)