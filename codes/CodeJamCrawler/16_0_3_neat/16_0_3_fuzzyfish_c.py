
print("Case #1:")
T = int(input())
N, J = map(int, input().split())

b = 1 + 2**(N-1)
maxadd = 2**(N-2)

ints = [0]*9


# Sieve
#cn = 1000000
#cache = [0]*cn

#for i in range(b-1, b+cn, 2):
#    cache[i] = 1


def getdiv(n):
    if n==2 or n==3: return 1
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return i
    return 1

for i in range(0, maxadd):
    num = b + 2*i
    s = "{0:b}".format(num)
    
    flag = False
    for base in range(0, 9):
        d = getdiv(int(s, base+2))
        if d == 1:
            flag = True
            break
        else:
            ints[base] = d
            
    if not flag:
        ints = [str(n) for n in ints]
        print(s + " " + " ".join(ints))
        J -= 1
        if J == 0:
            break
