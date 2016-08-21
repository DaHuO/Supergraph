# Counting Sheep

def last_num(base):
    if base == 0:
        return 'INSOMNIA'

    digits = set()
    count = 0
    while len(digits) < 10:
        count += 1
        num = count * base

        while num > 0:
            digits.add(num % 10)
            num /= 10
    return count * base

def main():
    f_in = open('A-large.in.txt', 'r')
    f_out = open('A-large.out.txt', 'w')

    n_tests = int(f_in.readline())
    for i in range(n_tests):
        base = int(f_in.readline())
        f_out.write('Case #{}: {}\n'.format(i + 1, last_num(base)))

    f_in.close()
    f_out.close()

if __name__ == "__main__":
    main()
