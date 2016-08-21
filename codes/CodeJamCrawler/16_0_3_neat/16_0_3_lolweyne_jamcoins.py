def check_prime(n):
    if n%2 == 0:
        return 2
    for i in range(3, int((n**0.5)+1), 2):
        if n%i==0:
            return i
    return None


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True


def check_bases(n):
    divisors = []
    for i in range(2, 11):
        based = int(str(n), i)
        divisor = check_prime(based)
        if divisor:
            divisors.append(check_prime(based))
        else:
            return None
    return divisors


def solve(n, j):
    solutions = []
    g = (10**(n-1)+1)
    while len(solutions) != j:
        divisors = check_bases(g)
        if divisors:
            solutions.append([g]+divisors)
        g = int(bin(int(str(g), 2)+2)[2:])
    return solutions

cases = int(input())
a = input()
n, j = (int(i) for i in a.split())
print('Case #1:')
ans = solve(n, j)
for i in ans:
    for index, d in enumerate(i):
        if index==len(i)-1:
            print(d)
        else:
            print(d, end=' ')
