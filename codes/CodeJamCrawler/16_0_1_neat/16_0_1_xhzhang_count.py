import sys

nums = []
for line in sys.stdin:
        nums.append(int(line)) 
nums = nums[1:]

for i, n in enumerate(nums, 1):
        digits = set()
        seen = set()
        j = 1
        while True:
            m = j*n
            if m in seen:
                    print "Case #" + str(i) + ": INSOMNIA"
                    break
            digits |= set(map(int, str(m)))
            if len(digits) == 10:
                    print "Case #" + str(i) + ": " + str(m)
                    break
            seen.add(m)
            j += 1

