f = open("B-large.in", "rb")
lines = []

for line in f:
    lines.append(line)

c = 1
for i in range(0, int(lines[0])):
    n = int(lines[c])
    c += 1
    nums = []
    missing = []
    for j in range(c, c + 2*n-1):
        nums += lines[j].split(" ")
        if (j != len(lines)-1):
            nums[-1] = nums[-1][:-1] 
    for x in nums:
        if missing.count(int(x)) == 0:
            if nums.count(x) % 2 == 1:
                missing.append(int(x))
    
    missing.sort()
    ans = ""
    for num in missing:
        ans += str(num) + " "

    ans = ans[:-1]
    c += (2*n) - 1
    print "Case #" + str(i+1) + ": " + ans
