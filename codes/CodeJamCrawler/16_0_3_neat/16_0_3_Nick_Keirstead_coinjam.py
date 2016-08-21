from __future__ import print_function

def readinput():
    fp = open('coinjam.in', 'r')
    t = int(fp.readline().strip())
    ln = fp.readline().strip().split()
    n = int(ln[0])
    j = int(ln[1])
    return (n, j)

def find_factor(n):
    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return i
    return -1

def main():
    (n_tot, j_tot) = readinput()
    j = 0
    print('Case #1:')
    for i in range(2**(n_tot - 2)):
        str2 = '1' + '0'*(n_tot-2-len(bin(i)[2:])) + bin(i)[2:] + '1'
        factors = []
        good = True
        for k in range(2, 11):
            num2 = int(str2, k)
            fac = find_factor(num2)
            if fac < 0:
                good = False
                break
            factors.append(fac)
        if good:
            print(str2, end=" ")
            for k in range(8):
                print(factors[k], end=" ")
            print(factors[8])
            j += 1
        if j >= j_tot:
            break
                

main()
