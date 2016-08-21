import math

factors = {}

def get_factor(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return -1

def main():
    T = raw_input()
    N, J = raw_input().strip().split()
    N = int(N)
    J = int(J)
    nums = []
    h = N / 2
    for i in range(3, 1 << h):
        if i % 2 == 0:
            continue
        d = format(i, '0' + str(h) + 'b')
        dnlz = format(i, '0b')
        e = dnlz + ('0' * (h - len(dnlz)))
        nums.append(e + d)
        if len(nums) == J:
            break

    print "Case #1:"
    for num in nums:
        line = ""
        line = line + num
        for base in range(2, 11):
            nb = int(num, base)
            hl = len(num) / 2
            line = line + " " + str(int(num[hl:], base))
        print line

if __name__ == "__main__":
    main()