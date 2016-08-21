import sys

def read_file_lines():
    if len(sys.argv) < 2:
        print('First argument should be the dataset file')
        exit(1)

    with open(sys.argv[1]) as f:
        file_lines = [line.strip() for line in f.readlines()]
    assert int(file_lines[0]) == len(file_lines[1:])
    return file_lines[1:]

cases = read_file_lines()

for i, case in enumerate(cases):
    s = case[0]
    for c in case[1:]:
        if s[0] > c:
            s = s + c
        else:
            s = c + s
    print "Case #%d: %s" % (i + 1, s)
