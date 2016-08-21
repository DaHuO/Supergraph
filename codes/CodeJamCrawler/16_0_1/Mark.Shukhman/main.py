exist = [0 for i in range(10)]

def do(N):
    for c in str(N):
        exist[int(c)] = 1


def check():
    for x in exist:
        if x == 0:
            return False
    return True

def solve(N):
    if (N == 0):
        return 'INSOMNIA'
    global exist
    exist = [0 for i in range(10)]
    last = N
    end = check()
    while end == False:
        do(last)
        end = check()
        last += N

    return last - N

n = int(input())

ans = []

for j in range(n):
    ans.append('Case #' + str(j + 1) + ': ' + str(solve(int(input()))))

for x in ans:
    print(x)