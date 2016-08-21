
T = int(input().strip())
for casen in range(1, T + 1):
    x = input().strip()
    count = 0
    for i in range(len(x) - 1):
        if x[i] == '+' and x[i+1] == '-':
            count += 1
    print('Case #%d: %d' % (casen, 2*count if x[0] == '+' else 2*count + 1))
