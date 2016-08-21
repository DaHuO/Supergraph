f = open('B-large.in', 'r')
t = int(f.readline())
output_file = open('B-large.out', 'w')
for i in xrange(1, t+1):
    count = 0
    pancakes = [s for s in f.readline().strip()]
    for x in xrange(len(pancakes)):
        if pancakes[x] == '-':
            pancakes[x] = 0
        elif pancakes[x] == '+':
            pancakes[x] = 1

    for x in range(1, len(pancakes)+1):
        if pancakes[-x] == 0:
            for z in range(0, len(pancakes)):
                pancakes[z] = 1 - pancakes[z]
            count += 1
    output_file.write("Case #%d: %d\n" % (i, count))

output_file.close()
