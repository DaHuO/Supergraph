from sys import stdin
import subprocess

def factor(n):
    result = subprocess.run('gfactor {}'.format(n), shell=True, universal_newlines=True, stdout=subprocess.PIPE)
    return int(result.stdout.split()[1])

stdin.readline()

N, J = map(int, stdin.readline().strip().split())
N -= 2

print('Case #1:')

for i in range(2**N):
    if J > 0:
        bits = bin(2*2**N + i * 2 + 1)[2:]
        numbers = list(int(bits, j) for j in range(2, 11))
        factored = list(map(lambda x: factor(x), numbers))
        if not any(map(lambda x: x[0] == x[1], zip(numbers, factored))):
            print(bits, *factored)
            J -= 1
