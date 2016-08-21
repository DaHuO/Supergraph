import sys
lines = sys.stdin.read().splitlines()
t = int(lines[0])
n = []
for i in range(t):
    n.append(int(lines[i + 1]))

def get_num(num):
    cur = num
    if num == 0: return 'INSOMNIA'
    nums = []
    count = 1
    while True:
        for c in str(cur):
            if c not in nums:
                nums.append(c)
        if len(nums) == 10: return str(cur)
        count += 1
        cur = num * count

for j,i in enumerate(n):
    sys.stdout.write('Case #%d: %s\n' % (j+1, get_num(i)))
