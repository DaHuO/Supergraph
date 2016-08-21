

t = int(input())
for i in range(t):
    n = int(input())
    if n == 0:
        print('Case #' + str(i+1) + ': INSOMNIA')
        continue
    digits = set()
    j = 0
    while len(digits) < 10:
        j += 1
        for c in str(j * n):
            digits.add(c)
    print('Case #' + str(i+1) + ': ' + str(j * n))
