import sys


def counting_sheep(N):
    res = set()
    if N == 0:
        return 'INSOMNIA'
    num = N
    while True:
        [res.add(c) for c in str(num)]
        if len(res) == 10:
            return num
        num += N

def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        count = int(f.readline())
        for i in range(count):
            N = int(f.readline())
            num = counting_sheep(N)
            print 'Case #%d: %s' % (i+1, num)
    

if __name__ == '__main__':
    main()
