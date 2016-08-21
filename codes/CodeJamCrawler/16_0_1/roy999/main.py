

def process(input_file, out):
    t = int(input_file.readline())

    for i in range(1, t + 1):
        line = input_file.readline().strip()

        result = solve(line)
        out.write("Case #%i: %s\n" % (i, result))


def solve(s):
    li = [s[0]]

    for c in s[1:]:
        if c < li[0]:
            li.append(c)
        else:
            li.insert(0, c)

    return ''.join(li)