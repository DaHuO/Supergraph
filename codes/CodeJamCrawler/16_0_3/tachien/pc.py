T = input()
line = input()
line = line.split()
n = int(line[0])
j = int(line[1])

def isPrime(num):
    i = 2
    while (i < num / i):
        if (num % i == 0):
            return num // i
        i += 1
    return -1

def success(s):
    sol = []
    for i in range(2, 11):
        re = isPrime(int(s, i))
        if (re == -1):
            return False
        sol.append(re)

    print(s, end=' ')
    for i in sol:
        print(i, end=' ')
    print()
    return True

for c in range(1, int(T)+1):
    print("Case #" + str(c) + ":")
    for i in range(0, (1 << (n - 2))):
        s = str(bin(i))[2:].zfill(n-2)
        s = '1' + s + '1'
        if (success(s)):
            j -= 1
        if (j == 0):
            break
