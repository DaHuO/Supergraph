def get_times(n):
    if n == 0: return "INSOMNIA"
    l = set()
    j = -1
    while len(l) < 10:
        j += 1
        for elem in str((j+1)*n):
            l.add(elem)
    return n*(j+1)

def read(filename):
    out = []
    with open(filename) as f:
        n = int(f.readline())
        for _ in range(n):
            value = int(f.readline())
            out.append(value)
    return out

def write(filename, out):
    with open(filename, 'w') as f:
        for i, elem in enumerate(out):
            f.write("Case #{0}: {1}\n".format(i+1, elem))

def test_a():
    assert get_times(0) == "INSOMNIA"
    assert get_times(1) == 10
    assert get_times(2) == 90
    assert get_times(11) == 110
    assert get_times(1692) == 5076

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    inp = read(filename)
    out = []
    for elem in inp:
        out.append(get_times(elem))
    write(filename+'.out', out)
