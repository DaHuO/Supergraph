
import sys

def checkN(n):
    a = [False] * 10
    for i in range(1, 100000):
        num = n * i
        s_num = str(num)
        for x in range(10):
            if (not a[x]) and (str(x) in s_num):
                a[x] = True
        if all(a):
            return n * i
    return None
    
def main():
    s = ''
    with open(sys.argv[1], 'r') as f:
        first_line = f.readline()
        count = 0
        for l in f:
            count += 1
            print l
            n = int(l.strip())
            c = checkN(n)
            print(count, n, c)
            if c:
                s += 'Case #' + str(count) + ': ' + str(c)
            else:
                s += 'Case #' + str(count) + ': INSOMNIA'
            s += '\n'
    
    with open(sys.argv[2], 'w') as f:
        f.write(s)
        
if __name__ == '__main__':
    main()