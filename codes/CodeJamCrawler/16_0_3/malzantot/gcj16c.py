import sys


n = 32
j = 500

def print_binary(num):
    if num != 0:
        print_binary(num>>1)
        if (num&1 ==0):
            sys.stdout.write("0")
        else:
            sys.stdout.write("1")

def getbasek(num, k):
    if num==0:
        return 0
    return (num&1) + k*getbasek(num>>1, k)

cur = 0

for i in range(1<<(n-2)):
    tmp = (1<<(n-1)) | (i<<1) | 1
    factors = []

    for k in range(2, 11):
        basek = getbasek(tmp, k)
        ff = 2
        while(ff * ff <= basek and ff <= 100000):
            if (basek % ff ==0):
                factors += [ff]
                break
            ff += 1


    if (len(factors) == 9):
        print_binary(tmp)
        for k in factors:
            sys.stdout.write(format(" %d" %k))
        print("")
        cur += 1
    if (cur == j):
        break


