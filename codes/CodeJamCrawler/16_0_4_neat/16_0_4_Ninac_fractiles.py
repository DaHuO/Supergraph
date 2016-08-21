
def main():
    file = open('D-small-attempt1.in', 'rU')
    lines = iter(file.readlines())
    file.close()

    case_count = int(next(lines))
    output = open('output', 'w')
    for case_idx in range(case_count):
        k, c, s = [int(x) for x in next(lines).split()]

        solution = 'IMPOSSIBLE'

        if s == k:
            solution = ' '.join(map(str, list(range(1, k + 1))))

        elif c > 1 and s >= (k - 1):
            solution = ' '.join(map(str, list(range(2, k + 1))))

        print('Case #{}: {}'.format(case_idx + 1, solution), file=output)
    output.close()


if __name__ == '__main__':
    main()