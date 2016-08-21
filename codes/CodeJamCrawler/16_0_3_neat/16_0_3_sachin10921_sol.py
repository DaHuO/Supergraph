import sys

def is_prime(n):
    if n <= 1:
        return False, 0
    elif n <= 3:
        return True, -1
    elif n % 2 == 0:
        return False, 2
    elif n % 3 == 0:
        return False, 3
    i = 5
    while i*i <= n:
        if n % i == 0:
            return False, i
        if n % (i + 2) == 0:
            return False, i + 2
        i += 6
    return True, -1

def collect_prime(num):
    sol = []
    flag = False
    for x in xrange(2, 11):
        prime, val = is_prime(int(num, x))
        flag = flag or prime
        if flag:
            return None
        else:
            sol.append(str(val))
    return sol

def solve(n, j):
    number_to = int((n - 2) * '1', 2)
    num = 0
    result = []
    while num <= number_to and len(result) != j:
        mid = str(bin(num))[2:]
        bin_num = "1" + ("0" * (n - 2 - len(mid))) + str(bin(num))[2:] + "1"
        flag = True
        sol = collect_prime(bin_num)
        if sol:
            result.append((bin_num, sol))
        num += 1
    return result


def output(result):
    with open("output1.txt", 'w') as f:
        for i, j in result:
            f.write("Case #" + str(i + 1) + ":\n")
            for item in j:
                f.write(str(item[0]) + " " + " ".join(item[1]) + "\n")

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        t = int(f.readline())
        result = []
        for case in xrange(t):
            n, j = map(int, f.readline().strip().split())
            result.append((case, solve(n, j)))
        output(result)