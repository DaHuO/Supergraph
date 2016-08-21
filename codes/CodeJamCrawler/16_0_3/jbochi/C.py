import sys

table_size = 1000000
divisors = [False] * (table_size)
for i in range(2, table_size):
    if divisors[i] == False:
        for multiple in range(2 * i, table_size, i):
            if divisors[multiple] == False:
                divisors[multiple] = i

# #print(list(enumerate(divisors[:100])))

def divisor(n):
    if n < table_size:
        return divisors[n]
    for i, divisor in enumerate(divisors[:10]):
        if (i >= 2) and (divisor == False) and ((n % i) == 0) and (i < n):
            return i
    return False

def interpret(n, b):
    x = 0
    base = 1
    for v in n[::-1]:
        x += int(v) * base
        base *= b
    return x

def jamcoin(n):
    n_bin = binary(n)
    bases = range(2, 11)
    numbers = map(lambda b: interpret(n_bin, b), bases)
    divs = map(lambda x: divisor(x), numbers)
    # if all(divs):
    #     print numbers, divs
    return divs


def binary(n):
    return bin(n)[2:]


def output(N, J):
    answer = ""
    #print(N)
    n = 2 ** (N - 1) + 1
    j = 0
    #print (N, n, binary(n))
    while j < J:
        # if not divisor(n):
        #     continue
        divs = jamcoin(n)
        if all(divs):
            answer += "\n%s %s" % (binary(n), " ".join(map(str, divs)))
            j = j + 1
        # answer += "\n%s %s" % (binary(n), "2 3 4 5 6 7 8 9 10")
        n = n + 2
    return answer

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        N, J = map(int, sys.stdin.readline().strip().split(" "))
        answer = output(N, J)
        print "Case #%d: %s" % (t + 1, answer)
