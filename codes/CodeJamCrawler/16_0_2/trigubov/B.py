def flip(string):
    res = string.replace('-', '=')
    res = res.replace('+', '-')
    return res.replace('=', '+')

f_in = open('B-large.in.txt', 'r')
f_out = open('out.txt', 'w')

t = int(f_in.readline())


for j in range(1, t + 1):
    current = f_in.readline().strip()
    flip_count = 0
    off = True
    while off:
        if all(c == '+' for c in current):
            f_out.write("Case #{}: {}".format(j, flip_count) + '\n')
            off = False

        i = current.rfind('-')
        current = flip(current[:i + 1]) + current[i + 1:]
        flip_count += 1





