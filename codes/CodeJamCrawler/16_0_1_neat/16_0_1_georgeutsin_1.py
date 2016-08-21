t = input()
nums = []
for i in range(t):
    nums.append(input())

for i in range(t):
    n = nums[i]
    count = 1
    curN = n
    digits = [0,0,0,0,0,0,0,0,0,0]
    while 0 in digits:
        curN = n*count
        curstr = str(curN)
        for a in curstr:
            digits[int(a)] = 1
        count += 1
        if(count > 1000000):
            break
    if 0 in digits:
        print "Case #" + str(i+1) + ": INSOMNIA"
    else:
        print "Case #" + str(i+1) + ": " + str(curN)
    
    