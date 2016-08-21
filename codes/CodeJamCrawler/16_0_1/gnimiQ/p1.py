import sys
from collections import deque
debug = False

def getDigits(n):
    s = deque()
    while n:
        s.appendleft(n%10)
        n //= 10
    if debug:
        print(list(s))
    return s

def answer(n):
    if n == 0:
        return "INSOMNIA"
    # how many digits are met
    counter = 0
    # which digits are met
    record = [False]*10
    N = 0
    while True:
        N += n
        if debug:
            print("read " + str(N))
        for digit in getDigits(N):
            if not record[digit]:
                record[digit] = True
                counter += 1
                if counter == 10:
                    return N
        
        



if __name__ == '__main__':
    filenm = list(sys.argv)[1]
    f = open(filenm, 'r')
    csnmbr = f.readline()
    if debug:
        print("case number: " + csnmbr )
    counter = 0
    for line in f:
        counter += 1
        r = answer(int(line))
        print("Case #" + str(counter) + ": " + str(r))
        

    
