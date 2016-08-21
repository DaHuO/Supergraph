f = open('p1.large.in', 'r')
num_cases = f.readline()
nums = set(str(i) for i in range(10))
for i,line in enumerate(f):
    line = line.strip()
    if line == '0':
        print("Case #{}: INSOMNIA".format(i+1))
    else:
        cur_set = set([c for c in line])
        N = int(line)
        while cur_set != nums:
            line = str(int(line) + N)
            for n in line:
                cur_set.add(n)
        print("Case #{}: {}".format(i+1, line))
f.close()
