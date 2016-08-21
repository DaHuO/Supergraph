def sheep(n):
    if n == 0:
        return 'INSOMNIA'
    num = 0
    count = set()
    while len(count) < 10:
        num += n
        count.update(str(num))
    return num

if __name__ == '__main__':
    lines = []
    with open('A-large.in') as f:
        f.readline()
        for i, line in enumerate(f, 1):
            lines.append('Case #%d: %s\n' % (i, sheep(int(line))))
    with open('output_large', 'w') as f:
        f.writelines(lines)
