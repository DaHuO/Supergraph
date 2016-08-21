
x = int(raw_input())
nums = []
for i in range(0, x):
    nums.append(int(raw_input()))

for j in range(0, len(nums)):
    if nums[j] == 0:
        print "Case #" + str(j+1) + ": INSOMNIA"
    else:
        seen = {}
        original = nums[j]
        cur = nums[j]
        times = 1
        while len(seen) != 10:
            curStr = str(cur)
            for k in range(0, len(curStr)):
                seen[curStr[k]] = 1
            times += 1
            cur = original * times
        print "Case #" + str(j+1) + ": " + str(original * (times-1))
