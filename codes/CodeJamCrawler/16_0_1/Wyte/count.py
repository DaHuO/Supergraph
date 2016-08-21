t = int(input())
for i in range(1, t+1):
    n = int(input())
    if n == 0:
        result = 'INSOMNIA'
    else:
        s = set()
        current = 0
        while len(s) != 10:
            current += n
            for digit in str(current):
                s.add(digit)
        result = current
    print('Case #{}: {}'.format(i, result))
