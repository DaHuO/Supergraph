import pyprimes

def factors(n):
    for f in range(2,100000):
        if n % f == 0:
            return f
    return n

fp = open("q3l.txt")
fw = open("q3a.txt", 'w')
fp.readline()
fw.write("Case #1:\n")
n, j = fp.readline().strip().split()
n = int(n)
j = int(j)
s = 2 ** (n-1) + 1
while 1:
    nonprime = {base:False for base in range(2,11)}
    s += 2
    string = "{0:b}".format(s)
    for base in range(2, 11):
        number = int(string, base)
        f = factors(number)
        if f == number:
            break
        else:
            nonprime[base] = f
    if all(nonprime.values()):
        fw.write(string)
        fw.write(" ")
        for base in range(2, 11):
            fw.write(str(nonprime[base]))
            fw.write(" ")
        fw.write("\n")
        j -= 1
        if j == 0:
            break
