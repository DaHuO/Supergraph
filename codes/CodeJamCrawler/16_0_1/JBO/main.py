def main(n):
    if n == 0:
        return 'INSOMNIA'

    found = set()
    curr_n = n
    while len(found) < 10:
        for x in str(curr_n):
            found.add(x)
        curr_n += n

    return curr_n - n


cases = int(raw_input())
for i in range(1, cases + 1):
    print('Case #%s: %s' % (i, main(int(raw_input()))))
