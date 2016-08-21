__author__ = 'zfeng'

def nToArr(line):
    l = line.strip()
    arr = [] * len(l)
    for i in l:
        arr.append(int(i))

    return arr


def solver(line):
    n = int(line)
    count = 0
    result = 1
    mark = [0] * 10
    cur = [0] * 256
    num = nToArr(line)

    if n == 0:
        return 'INSOMNIA'
    else:
        idx = 0
        for j in xrange(len(num) - 1, -1, -1):
            i = num[j]
            if mark[i] == 0:
                mark[i] = 1
                count += 1
            cur[idx] = i
            idx += 1

        while True:
            idx = 0
            o = 0
            result += 1
            for j in xrange(len(num) - 1, -1, -1):
                i = num[j]
                cur[idx] += i + o
                o = 0
                if cur[idx] >= 10:
                    cur[idx] -= 10
                    o = 1

                if mark[cur[idx]] == 0:
                    mark[cur[idx]] = 1
                    count += 1
                idx += 1

                if count == 10:
                    return result * n
            while o == 1:
                cur[idx] += 1

                if cur[idx] >= 10:
                    cur[idx] -= 10
                    o = 1
                else:
                    o = 0

                if mark[cur[idx]] == 0:
                    mark[cur[idx]] = 1
                    count += 1
                if count == 10:
                    return result * n
                idx += 1

        return result * n

if __name__ == '__main__':
    f = open('/Users/zfeng/Downloads/A-large.in')
    lines = f.readlines()
    f.close()

    for i in xrange(int(lines[0])):
        print str.format('Case #{0}: {1}', i + 1, solver(lines[i + 1]))

