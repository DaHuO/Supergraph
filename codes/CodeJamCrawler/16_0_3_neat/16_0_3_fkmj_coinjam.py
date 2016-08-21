from random import randint, choice

n = 32
mx = 10000

def random_num():
    return ''.join(['1'] + [choice('01') for i in range(n-2)] + ['1'])


def check(num, base):
    for i in range(2,mx):
        if num % i == 0:
            return (True,i)
    return (False,0)


def gen():
    n = random_num()
    ds = []
    for i in range(2,11):
        val = int(n,i)
        res,d = check(val,i)
        if not res:
            return None
        ds.append(d)
    return (n,ds)

def main():
    global n
    raw_input()
    nn,j = [int(s) for s in raw_input().strip().split()]

    n = nn

    print "Case #1:"
    
    used = set()
    for i in range(j):
        o = gen()
        while (o == None) or (o[0] in used):
            o = gen()

        print o[0],' '.join([str(x) for x in o[1]])

        used.add(o[0])

main()
