def solve():
    n = int(input())
    if n == 0: return 'INSOMNIA'
    s = set()
    index = 1
    while len(s) != 10:
        for digit in str(n*index):
            s.add(digit)
        index += 1
    return n * (index-1)


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t+1):
        print('Case #{}: {}'.format(i, solve()))
