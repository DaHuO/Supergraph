def solve(stack, j):
    counter = 0
    ps = list(stack)
    i = 1
    while(i < len(ps)):
        if(ps[i] != ps[i - 1]):
            counter += 1
        i += 1
    if(ps[len(ps) - 1] == '-'):
        counter += 1
    print("Case #" + str(j) + ": " + str(counter))

T = int(input())
for j in range(1, T+1):
    solve(input(), j)
