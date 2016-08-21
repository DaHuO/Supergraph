with open('small.in') as f:
    for i, line in enumerate(f.readlines()[1:], start=1):
        counter = 0
        last = '+'
        for x in line.strip()[::-1]:
            if x != last:
                counter += 1
                last = x
        print("Case #{}: {}".format(str(i), str(counter)))
