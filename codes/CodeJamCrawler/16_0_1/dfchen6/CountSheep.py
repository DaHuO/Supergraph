import sys

def getDigits(N):
    digits = set()
    while N > 0:
        digits.add(N % 10)
        N = N / 10
    return digits

def lastNum(N):
    if N == 0:
        return "INSOMNIA"
    digits_seen = set()
    num = N
    while len(digits_seen) != 10:
        curr_digits = getDigits(num)
        digits_seen = digits_seen.union(curr_digits)
        num += N
    return num - N

if __name__ == "__main__":
    f = open('A-large.in', 'r')
    output = open('A-large.out', 'w')
    C = int(f.readline())
    for i in range(0, C):
        n = int(f.readline())
        output.write("Case #" + str(i + 1) + ": " + str(lastNum(n)) + "\n")
