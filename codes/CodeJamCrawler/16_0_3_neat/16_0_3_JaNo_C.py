def is_nprime(x):
    for i in range(2,1000):
        if x % i == 0:
            return i
    return None

def check(x):
    res = []
    for i in range(2, 11):
        a = is_nprime(int('{:b}'.format(x), i))
        if not a: return None
        res.append(a)
    return res

input()
n, k = map(int, input().split())
print("Case #1:")

a = 2**(n-1)+1
p = 0
while p < k:
    x = check(a)
    if x:
        print('{:b}'.format(a), ' '.join(map(str,x)))
        p+=1
    a+=2
