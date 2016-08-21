def flipcakes(order):
    counter = 0
    while '-' in order:
        counter += 1
        first_pancake_pos = order[0]
        new_pos = '-' if first_pancake_pos == '+' else '+'
        try:
            slide_point = order.index(new_pos)
            rest = order[slide_point:]
        except ValueError:
            slide_point = len(order)
            rest = ''
        order = new_pos * slide_point + rest

    return counter

f = open("B-large.in")

t = int(f.readline())
tcs = f.readlines()

o = open("B-large.out", "w")
for ix, tc in enumerate(tcs):
    res = flipcakes(tc.strip())
    o.write("Case #{}: {}\n".format(ix+1, res))


