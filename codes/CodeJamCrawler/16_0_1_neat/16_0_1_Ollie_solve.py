#!/usr/bin/python3

def seen_all(x, seen):
    for digit in str(x):
        seen[int(digit)] = True
    for digit in seen:
        if digit == False:
            return False
    return True

def solve(n):
    seen = [False]*10

    if n == 0:
        return "INSOMNIA"

#    print(n)
    i = 1
    while True:
        temp=i*n
        if seen_all(temp, seen):
            return str(temp)
        i += 1
#        print("\t"+str(temp))
#        print("\t"+str(seen))

t = int(input())
for i in range(1,t+1):
#    print(i)
    n = int(input())
    print("Case #%d: %s" % (i, solve(n)))
