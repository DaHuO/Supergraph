# Counting Sheep

f = open('A-large.in', 'r')
g = open('output', 'w')

t = int(f.readline().strip())

for count in range(t):
    digit_list = set()
    i = 1
    n = int(f.readline().strip())
    num = str(n)
    if n == 0: g.write('Case #' + str(count+1) + ': INSOMNIA\n')
    else:
        while True:
            d = set(digit for digit in num)
            digit_list = digit_list.union(d)
            if len(digit_list) == 10:
                break
            num = str((i+1)*n)
            i += 1
        g.write('Case #' + str(count+1) + ': ' + num + '\n')

f.close()
g.close()
