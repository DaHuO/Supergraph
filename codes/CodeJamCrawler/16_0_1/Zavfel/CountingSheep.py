# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    N =  raw_input()
    baseN = int(N)
    if N=='0':
        print "Case #" + str(i) + ": " 'INSOMNIA'
        continue
    counter = []
    while True:
        for j in N:
            if j not in counter:
                counter.append(j)
                if len(counter) == 10:
                    print "Case #" + str(i) + ": " +N
                    break
        else:
            newN = int(N)+baseN
            N = str(newN)
            continue

        break
