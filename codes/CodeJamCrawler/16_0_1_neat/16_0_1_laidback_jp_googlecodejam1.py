nums = []


times = int(raw_input())

for i in range(times):
    nums.append(int(raw_input()))
                

for i in range(len(nums)):
    if nums[i] == 0:
        print "Case #" + str((i+1)) +": INSOMNIA"
    else:
        temp = []
        for dig in str(nums[i]):
            if dig not in temp:
                temp.append(dig)
                
        count = 0
        while len(temp) != 10:
            count += 1
            for digit in str(nums[i]*count):
                if digit not in temp:
                    temp.append(digit)
            
        
        
    
        print "Case #"+ str((i+1)) +": "+  str(nums[i]*count)
