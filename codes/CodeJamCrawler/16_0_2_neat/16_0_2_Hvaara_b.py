def get_count(inp):
    out = 0
    prev = '+'
    for elem in reversed(inp):
        if elem != prev:
            out += 1
            prev = elem
    return out

def read(filename):
    out = []
    with open(filename) as f:
        n = int(f.readline())
        for _ in range(n):
            value = f.readline().strip()
            out.append(value)
    return out 

def write(filename, out):
    with open(filename, 'w') as f:
        for i, elem in enumerate(out):
            f.write("Case #{0}: {1}\n".format(i+1, elem))

def test_b():
    assert get_count('-') == 1
    assert get_count('-+') == 1
    assert get_count('+-') == 2
    assert get_count('+++') == 0
    assert get_count('--+-') == 3

if __name__ == '__main__':
    import sys 
    filename = sys.argv[1]
    inp = read(filename)
    out = []
    for elem in inp:
        out.append(get_count(elem))
    write(filename+'.out', out)

