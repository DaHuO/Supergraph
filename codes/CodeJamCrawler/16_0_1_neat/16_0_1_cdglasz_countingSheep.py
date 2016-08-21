import re

infile = "/Users/Christopher/Downloads/A-large.in.txt"
outfile = "/Users/Christopher/Desktop/Python/CodeJam/practice.out.txt"
txt = open(infile)
data = txt.read()
numbers = [int(l) for l in re.split('\n+', data) if l][1:]

newlines = []
for i,n in enumerate(numbers):
    line = "Case #" + str(i+1) +": "
    if not n:
        newlines.append(line + "INSOMNIA")
        continue
    unseen = set(range(10))
    j = 0
    while unseen:
        j += 1
        digits = set([int(c) for c in str(j*n)])
        unseen -= digits
    line += str(j*n)
    newlines.append(line)

lines = '\n'.join(newlines)

target = open(outfile, 'w')
target.write(lines)