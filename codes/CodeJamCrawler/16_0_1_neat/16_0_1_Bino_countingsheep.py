import math

def counting(N):
    seen = [0] * 10
    number = 0
    cur = N
    while True:
        org = cur
        while cur > 0:
            digit = cur % 10
            if seen[digit] == 0:
                seen[digit] = 1
                number = number+1
            cur = cur / 10
            if number == 10:
                return org
        cur = org+N


if __name__ == "__main__":
    input = "A-large"
    f = open(input + ".in")
    output = open(input + ".out", "w")
    cases = int(f.readline())
    print(cases)
    for i in range(cases):
        N = int(f.readline())
        if N == 0:
            output.write("Case #" + str(i+1)+ ": INSOMNIA\n")
        else:
            output.write("Case #" + str(i+1)+ ": " + str(counting(N))+"\n")
    f.close()
    output.close()