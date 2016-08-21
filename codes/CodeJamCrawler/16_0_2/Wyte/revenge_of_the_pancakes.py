t = int(input())
for i in range(1, t+1):
    s = input()
    result = 0
    for p in s[::-1]:
        if p == '+':
            if result%2 == 1:
                result += 1
        if p == '-':
            if result%2 == 0:
                result += 1
    print('Case #{}: {}'.format(i, result))
