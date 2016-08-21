import sys

def get_number(n):
    if n == 0: return "INSOMNIA"
    digits = set()
    i = 1
    while True:
        for d in str(i*n):
            digits.add(d)
            if len(digits)==10:
                return i*n
        i+=1


g = open("out.txt" or sys.argv[2] , 'w')

with open(sys.argv[1]) as f:
    tests = map(lambda x: long(x.strip()),f.readlines())[1:]
    i = 0
    for test in tests:
        i+=1
        s  = "Case #{0}: {1}".format(i, get_number(test))
        print(s)
        g.write(s+"\n")
g.close()
