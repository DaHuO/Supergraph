fin = open('A-large.in', 'r')

N = int(fin.readline())
numbers = map(lambda x: int(x), fin.readlines())

# print N
# print numbers

result = []
for n in numbers:
    if n == 0:
        result.append('INSOMNIA')
    else:
        seen = set()
        i = 0
        while len(seen) < 10:
            i += 1
            last_number = i * n
            digits = list(str(last_number))
            for digit in set(digits):
                if digit not in seen:
                    seen.add(digit)
            # print seen
        result.append(str(last_number))
    #print ""

fin.close()

fout = open('A-large.out', 'w')
for i,r in enumerate(result):
    print >> fout, "Case #" + str(i+1) + ": " + r
fout.close()