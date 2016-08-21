INPUT_FILE = "f.in"
OUTPUT_FILE = "f.out"
res = []
    
def write_output():
    l = [0] * 9 
    l[1] = l[3] = l[5] = l[7] = 2
    out_file = open(OUTPUT_FILE, "w")
    out_file.write("Case #1:\n")
    for j in res:
        b = j[0]
        for i in [2,4,6,8,10]:
            l[i-2] = j[i/2]
        tmp = [str(i) for i in l]
        out_file.write(b + ' ' + " ".join(tmp)+'\n')
    out_file.close()

def prime(n):
    to = int(n ** 0.5 // 1) 
    for i in range(2, to):
        if n % i == 0:
            return i
    return True

def build_set(n, j):
    start = 2 ** (n-1) + 1 
    end = 2 ** n
    
    res = set()
    print 'start is %d' % start
    print 'end is %d' % end
    
    for i in range(start, end, 2):
        print 'iteration %d' % i
        b = bin(i)[2:]
        if (b.count('1') % 2) != 0:
            continue
        t2 = int(b,2)
        t4 = int(b,4)
        t6 = int(b,6)
        t8 = int(b,8)
        t10 = int(b,10)
        p2 = prime(i)
        p4 = prime(t4)
        p6 = prime(t6)
        p8 = prime(t8)
        p10 = prime(t10)
        if p2 == True:
            print 'continue - %d is prime' % t2
            continue
        if p4 == True: 
            print 'continue - %d is prime' % t4
            continue
        if p6 == True: 
            print 'continue - %d is prime' % t6
            continue
        if p8 == True: 
            print 'continue - %d is prime' % t8
            continue
        if p10 == True: 
            print 'continue - %d is prime' % t10
            continue
        print 'adding %d, found already %d' % (i,len(res))
        res.add((b,p2,p4,p6,p8,p10))
        if len(res) == j:
            return res
        
    return res

def solve(case):
    inputs = case.split(' ')
    n , j = int(inputs[0]), int(inputs[1]) 
    s = build_set(n, j)
    print 'returned s of size %d' % len(s) 
    result = []
    for _ in range(j):
        result.append(s.pop())
    return result

def get_next(data):
    for line in data:
        case = line.strip()
        yield case

if __name__ == '__main__':
    print 'Starting...'
    f = file(INPUT_FILE)
    for line in get_next(f.read().strip().split('\n')[1:]):
        res = solve(line)
    write_output()
    f.close()
    print 'done.'