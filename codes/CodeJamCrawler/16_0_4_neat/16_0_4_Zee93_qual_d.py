
# since K == S then no need to do anything. xD

f = open('D-small-attempt0.in')
n = int(f.readline()[:-1])

output = []
for i in range(1, n + 1):
    k, c, s = map(int, f.readline()[:-1].split(' '))
    output.append('Case #{}: {}\n'.format(i, ' '.join([str(j) for j in range(1, k + 1)])))

with open('d.out', mode='a+') as f:
    f.writelines(output)
