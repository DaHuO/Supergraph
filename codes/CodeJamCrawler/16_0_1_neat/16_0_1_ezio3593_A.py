def get_digits(n):
    digits = set()
    while n != 0:
        digits.add(n % 10)
        n //= 10
    return digits


def get_answer(n):
    seen_numbers = set()
    if n == 0:
        return 'INSOMNIA'

    cur_n = n
    while True:
        seen_numbers.update(get_digits(cur_n))
        if len(seen_numbers) == 10:
            break
        cur_n += n
    return cur_n


# t = int(raw_input())
# for i in xrange(1, t + 1):
#     n = int(raw_input())
#     print "Case #{}: {}".format(i, get_answer(n))

out = open('out.txt', 'w')

with open("A-large.in") as f:
    data = f.read().split('\n')
    t = int(data[0])
    for i in xrange(1, t + 1):
        n = int(data[i])
        out.write("Case #{}: {}\n".format(i, get_answer(n)))

out.close()
