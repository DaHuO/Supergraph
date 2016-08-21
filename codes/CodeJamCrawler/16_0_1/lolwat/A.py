T = int(raw_input())
for i in range(1, T+1):
    n = int(raw_input())
    if n == 0:
        print "Case #" + str(i) + ": INSOMNIA"
        continue
    x = 0
    nums = set()
    while len(nums) != 10:
        x += 1
        for a in str(x*n):
            nums.add(int(a))
    print "Case #" + str(i) + ": " + str(x*n)