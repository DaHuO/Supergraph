from sets import Set

def last_number(N):
    if N == 0:
        return "INSOMNIA"
    i = 1
    s = Set(['0','1','2','3','4','5','6','7','8','9'])
    while True:
        num = N*i
        for digit in str(num):
            if digit in s:
                s.remove(digit)
        if len(s) == 0:
            return str(num)
        i += 1


if __name__ == '__main__':
    f = open("A-large.in", 'r')
    r = open("result.txt", 'w')
    test = int(f.readline())
    for i in range(test):
        N = int(f.readline())
        result = last_number(N)
        r.write('Case #%s: %s' %(i+1,result))
        if i != test-1:
            r.write('\n')
    r.close()
    f.close()