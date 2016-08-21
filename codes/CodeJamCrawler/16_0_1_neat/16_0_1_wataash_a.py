import itertools

with open('a.in') as f:
    inp = f.readlines()

T = int(inp.pop(0))

for case in range(T):
    N = int(inp.pop(0))
    if N == 0:
        ans = 'INSOMNIA'
    else:
        digits = set(str(N))
        if len(digits) == 10:
            ans = N
        else:
            for i in itertools.count(start=2):
                digits |= set(str(N * i))
                if len(digits) == 10:
                    ans = N * i
                    break

    print('Case #' + str((int(case) + 1)) + ': ' + str(ans))
