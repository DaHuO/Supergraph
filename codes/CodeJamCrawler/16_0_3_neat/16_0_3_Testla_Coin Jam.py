t = int(input())
n, j = (int(x) for x in input().split())

print("Case #1:")

def next_permutation(s):
    index = s.rfind('0', 0, s.rfind('1'))
    if index == -1:
        return None
    return s[0:index] + '10' + ''.join(sorted(s[index + 2:]))

# return 0 if x is a prime, x's smallest prime divisor if x is not a prime
def test_prime(x):
    if x % 2 == 0:
        return 2
    for i in range(3, 1000, 2):
        if x % i == 0 and x != i:
            return i
    return 0

for num_one in range(n - 1 - 1, 0, -1):
    s = '0' * (n - num_one - 2) + '1' * num_one
    while s is not None:
        number = s.join(('1', '1'))
        l = [test_prime(int(number, base)) for base in range(2, 10 + 1)]
        if 0 not in l:
            print(number, ' '.join(map(str, l)))
            j -= 1
            if j == 0:
                exit()
        s = next_permutation(s)