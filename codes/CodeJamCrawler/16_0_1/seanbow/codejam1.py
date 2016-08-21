from math import log10
import random

def digits(n):
    exp = int(log10(n) + 1)
    for i in range(exp):
        yield n % 10
        n /= 10

def last_number_counted(n):
    if n == 0:
        return "INSOMNIA"
    seen = [0]*10
    num = n
    while not all(seen):
        for dig in digits(num):
            seen[dig] = 1
        num += n        
    return num - n

def testcode():
    last_number_counted(random.randint(1,1000000))

def run_on_input():
    fname = 'A-large.in'
    f = open(fname, 'r')
    inputs = f.read().split()[1:]
    fout = open('out.txt', 'w')
    for (i,inp) in enumerate(inputs):
        fout.write('Case #' + str(i + 1) + ': ' + str(last_number_counted(int(inp))))
        fout.write('\n')
        print('Case #' + str(i + 1) + ': ' + str(last_number_counted(int(inp))))

    fout.close()    
