with open('B-large.in') as input:
    with open('B-large-ans.txt', 'w') as out:
        tests = int(input.readline())
        for t in range(tests):
            str = input.readline().strip()
            while len(str) > 0 and str[-1] == '+':
                str = str[0: -1]
            flips = 1 if len(str) != 0 else 0
            for i in range(1, len(str)):
                if str[i] != str[i - 1]:
                    flips += 1
            out.write('Case #{0}: {1}\n'.format(t + 1, flips))