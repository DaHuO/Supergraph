import math

def gen(n, j=2):
    n = n//2-2
    for i in range(j):
        s = '1{:0{n}b}1'.format(i, n=n)
        yield s+s

def gen_div(n, j=2):
    n = n//2-2
    for i in range(j):
        s = '1{:0{n}b}1'.format(i, n=n)
        yield s

def convert_to_base(s, b):
    if b == 10:
        return int(s)
    s = list(str(s))
    s.reverse()
    num = 0
    for i in range(len(s)):
        num += b**i * int(s[i])
    return num

T = input()
n,j = map(int,input().split())
bits = list(gen(n,j))
divs = list(gen_div(n,j))
answer = []
for i in range(j):
    temp = list(map(
        str, [convert_to_base(divs[i],k) for k in range(2,11)] 
    ))
    answer.append(bits[i] + ' ' + ' '.join(temp))
out = open('new-c-large-output.txt', 'w')
out.write('Case #1:\n')
out.write('\n'.join(answer))
