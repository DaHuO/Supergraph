N = int(input())

for i in range(N):
    s = input().strip() + '+'
    print("Case #{}: {}".format(i+1, s.count('+-') + s.count('-+')))

