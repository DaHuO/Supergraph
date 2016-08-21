f = open('A-large.in')

N = int(f.readline().strip())
results = [0 for i in range(N)]

def add_all(s, n):
    for x in str(n):
        s.add(x)

def sleep_steps(n):
    if n <= 0:
        return 'INSOMNIA'
    seen = set()
    add_all(seen, n)
    for i in range(1, 100):
        curr = n*i
        add_all(seen, curr)
        if len(seen) == 10:
            return curr
    return 'INSOMNIA'

i = 0
for line in f:
    num = int(line.split()[0])
    results[i] = sleep_steps(num)
    i += 1

with open('sheep_out.txt', 'w') as f:
    for result, i in zip(results, range(N)):
        w = 'Case #{}: {}\n'.format(i+1, result)
        f.write(w)
