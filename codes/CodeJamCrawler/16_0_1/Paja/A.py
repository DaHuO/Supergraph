import fileinput

def solve(N):
    if N == 0:
        return "INSOMNIA"
    else:
        digits = {}
        m = N
        while True:
            s = str(m)
            for digit in s:
                if digit not in digits:
                    digits[digit] = True
            if len(digits) == 10:
                return m
            m += N


n = int(raw_input())
for line in range(n):
    d = raw_input()
    print "Case #{}: {}".format(line + 1, solve(int(d)))
    
