import sys
#from math import sqrt


def get_repr(n):
    result = [n] + [0]*8

    pos = 0
    while n > 0:
        if n % 2 == 1:
            for i in range(3, 11):
                result[i-2] += pow(i, pos)
        n = int(n/2)
        pos += 1
    return result


def get_divisors(vec):
    result = [0] * 9

    for i in range(9):
        for j in range(2, 100):
            if vec[i] % j == 0:
                result[i] = j
                break

        if result[i] == 0:
            result[0] = 0
            break

    return result


def main():
    stdin = sys.stdin.readline()
    T = int(stdin)
    for i in range(T):
        stdin = sys.stdin.readline()
        N, J = stdin.split()
        N = int(N)
        J = int(J)
        print("Case #" + str(i+1) + ":")
        count = 0
        for j in range(pow(2, N-1)+1, pow(2, N), 2):
            vec = get_repr(j)
            divisors = get_divisors(vec)

            if divisors[0] != 0:
                count += 1
                print(str(vec[8]) + " " + " ".join(str(d) for d in divisors))
                if count == J:
                    break

main()
