def result(input):
    r = 0
    input += '+'
    for i in range(len(input) - 1):
        if input[i] != input[i + 1]:
            r += 1
    return r

if __name__ == "__main__":
    with open('B-large.in') as f:
        with open('B-large.out', 'w') as w:
            r = f.readlines()

            for i in range(len(r) - 1):
                w.write('Case #%d: %d\n' % (i + 1, result(r[i + 1][:-1])))