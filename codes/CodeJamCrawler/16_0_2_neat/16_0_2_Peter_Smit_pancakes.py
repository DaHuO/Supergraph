import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    line = line.strip()
    count = 0
    prev_char = line[0]
    for j in range(1,len(line)):
        if line[j] != prev_char:
            count += 1
            prev_char = line[j]
    if line[-1] == '-':
        count += 1
    print("Case #{}: {}".format(i, count))