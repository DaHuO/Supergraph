fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

tests_count = int(fin.readline())

def solve():
    n = int(fin.readline())
    if n == 0:
        return "INSOMNIA"
    count = [0] * 10
    current = n
    while sum(count) < len(count):
        tmp = current
        while tmp:
            count[tmp % 10] = 1
            tmp /= 10
        current += n
    return current - n

for test in range(1, tests_count + 1):
    answer = solve()
    fout.write("Case #{}: {}\n".format(test, answer))
