def all_and(array):
    ans = True
    for v in array:
        ans = ans and v
    return ans

def solve(N, j):
    if N == 0:
        print("Case #" + str(j) + ": INSOMNIA")
        return
    digits = [ False for i in range(10)]
    i = 1
    l = N * i
    while not all_and(digits):
        for d in str(l):
            digits[int(d)] = True
        i += 1
        l = N * i
    print("Case #" + str(j) + ": " + str(N * (i - 1)))

T = int(input())
for j in range(1, T + 1):
    solve(int(input()), j)

