def flip(a):
    if a == '-':
        return '+'
    else:
        return '-'


def serve(case, n=0):
    last = case.rfind('-')
    if last == -1:
        return n
    else:
        top = case[:last+1]
        top = "".join(map(flip, top))
        top[::-1]
        pancakes = top + case[last+1:]
        return serve(pancakes, n + 1)

with open('B-large.in') as infile:
    lines = infile.readlines()
    T = int(lines[0])
    cases = lines[1:]

with open('output.txt', 'w') as outfile:
    for index, case in enumerate(cases):
        outfile.write("Case #%d: %s\n" % (index + 1, serve(case)))
