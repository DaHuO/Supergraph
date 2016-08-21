from itertools import count


def get_count(n):
    if n == 0:
        return 'INSOMNIA'

    numbers = set()

    for i in count(start=1):
        val = n * i
        res = val

        while val > 0:
            numbers.add(val % 10)
            val = val // 10

        if len(numbers) >= 10:
            return res


with open('a.out', 'wt') as f_out:
    with open('A-large.in') as f_in:
        next(f_in)

        i = 1

        for line in f_in:
            n = int(line)
            res = get_count(n)

            f_out.write('Case #{}: {res}\n'.format(i, res=res))
            print('Case #{}: {res}'.format(i, res=res))

            i += 1
