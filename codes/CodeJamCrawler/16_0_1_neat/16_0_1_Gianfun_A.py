f = open("A-large.in", "r")
output = open("A-large.out", "w")

T = int(f.readline().strip())

for i in range(T):
    N = int(f.readline().strip())
    if N == 0:
        output.write("Case #%d: INSOMNIA\n"%(i+1))
        print("Case #%d: INSOMNIA"%(i))
        continue

    nums = {}
    for c in range(10):
        nums[str(c)] = False

    multiplier = 1
    while 1:
        numberBeingCounted = multiplier * N
        for char in str(numberBeingCounted):
            nums[char] = True
        if False not in nums.values():
            output.write("Case #%d: %d\n"%(i+1, numberBeingCounted))
            print("Case #%d: %d"%(i, numberBeingCounted))
            break
        multiplier += 1
f.close()
output.close()
        
    
