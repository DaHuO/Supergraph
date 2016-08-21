
with open('A-large.in') as input:
    with open('qual-a-big-ans.txt', 'w') as out:
        tests = int(input.readline())
        for t in range(tests):
            out.write('Case #{0}: '.format(t + 1))
            cur = n = int(input.readline())
            if n == 0:
                out.write('INSOMNIA\n')
                continue
            mark = set()
            while len(mark) != 10:
                for ch in str(cur):
                    mark.add(ch)
                cur += n
            out.write(str(cur - n) + '\n')