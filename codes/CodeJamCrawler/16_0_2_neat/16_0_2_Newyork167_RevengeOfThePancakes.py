def start():
    output_file = open('output.txt', 'w+')
    t = int(raw_input().strip())
    for x in range(t):
        flip_count = 0
        p = raw_input().strip()
        for y in xrange(len(p) - 1, -1, -1):
            if p[y] == "-":
                flip_count += 1
                p = flip(p[:y + 1]) + p[y + 1:]
        output_file.write("Case #{case}: {result}\n".format(case=x+1, result=flip_count))

def flip(p):
    return ''.join([''.join(x) for x in ["+" if x == "-" else "-" for x in p]])