from sys import *
f_i = open(argv[1])
f_o = open(argv[2], 'w')
cases = int(f_i.readline() [:-1])
for c in range(1, cases + 1):
    header = 'Case #' + str(c) + ': '
    c_cases = int(f_i.readline() [:-1])
    nums = {}
    for d in range(c_cases * 2 - 1):
        heights = [int(n) for n in f_i.readline() [:-1].split(' ')]
        for h in heights:
            if h not in nums.keys():
                nums[h] = 1
            else:
                nums[h] += 1
    odds = []
    for nn in nums.keys():
        if nums[nn]%2 == 1:
            odds.append(nn)
    f_o.write(header + ' '.join([str(m) for m in sorted(odds)]) + '\n')
f_o.close()
