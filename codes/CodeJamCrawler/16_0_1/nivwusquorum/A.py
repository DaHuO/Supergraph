def get_digits(n):
    return set(list(str(n)))

def calc(n):
    if n == 0:
        return 'INSOMNIA'
    known = set()
    for i in range(1, 100000):
        known.update(get_digits(i * n))
        if len(known) == 10:
            return i * n


if __name__ == '__main__':
    ncases = int(input())
    for case in range(1, ncases + 1):
        print("Case #%d:" % (case,), calc(int(input())))
