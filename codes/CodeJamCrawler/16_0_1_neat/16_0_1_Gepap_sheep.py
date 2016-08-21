def count(N):
    numbers = range(10)
    current = N
    count = 1

    if N == 0:
        return 'INSOMNIA'

    while numbers:
        current = count * N
        digits = str(current)
        digits = map(int, digits)
        numbers = filter(lambda a: a not in digits, numbers)
        count += 1

    return current

with open('A-large.in') as infile:
    lines = infile.readlines()
    T = int(lines[0])
    cases = lines[1:]

with open('output.txt', 'w') as outfile:
    for index, case in enumerate(cases):
        outfile.write("Case #%d: %s\n" % (index + 1, count(int(case))))
