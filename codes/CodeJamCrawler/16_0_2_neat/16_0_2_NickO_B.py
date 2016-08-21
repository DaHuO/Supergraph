def flip(i, stack: str):
    flipped = stack[:i]
    not_flipped = stack[i:]
    flipped = flipped.replace('-', '_').replace('+', '-').replace('_', '+')[::-1]
    return flipped + not_flipped


def happy(stack, target):
    return all(map(target.__eq__, stack))


def solve(stack, target='+'):
    if happy(stack, target):
        return 0
    else:
        for i in range(1, len(stack)+1):
            top = stack[:i]
            bottom = stack[i:]
            if happy(bottom, target):
                unhappy = top
                break
        return solve(unhappy, flip(1, target)) +1


def parse(file):
    lines = file.readlines()
    assert int(lines[0]) == len(lines)-1
    results = []
    for i in range(1, len(lines)):
        try:
            results.append('Case #{}: {}\n'.format(i, solve(lines[i].strip())))
        except:
            raise Exception('Test case {}: {} caused an exception'.format(i,lines[i]))
    return results


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        with open(sys.argv[2], 'w') as f2:
            f2.writelines(parse(f))