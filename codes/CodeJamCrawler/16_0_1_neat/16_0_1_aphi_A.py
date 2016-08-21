from sys import stdin, stdout

def solve(N):
    if N == 0:
        return "INSOMNIA"

    nums = set()

    i = 1
    while True:
        nums.update(str(N * i))
        
        if len(nums) == 10:
            return N * i

        i += 1




T = int(stdin.readline())

for t in range(T):
    N = int(stdin.readline())

    result = solve(N)

    stdout.write("Case #%d: %s\n"%(t+1, result))