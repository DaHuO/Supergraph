input = open('B-large.in', 'r')
output = open('B-large.out', 'w')
N = int(input.readline())
for case in range(1, N + 1):
    print("Case #", case, sep = "", end = ": ", file = output)
    sides = input.readline().rstrip()
    side = sides[0]
    i = 1
    ans = 0
    while i < len(sides):
        if sides[i] != side:
            ans += 1
            side = sides[i]
        i += 1
    if sides[-1] == '-':
        ans += 1
    print(ans, file = output)
input.close()
output.close()