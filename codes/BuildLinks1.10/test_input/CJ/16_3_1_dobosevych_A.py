T = int(input())

for i in range(T):
    N = int(input())
    
    nums = input().split()
    nums = [(int(nums[i]), chr(i + ord('A'))) for i in range(N)]
    total = 0
    for t in nums:
        total += t[0]
    
    result = []
    
    
    while total != 0:
        nums.sort(reverse=True)
        
        if (nums[0][0] - 2) * 2 <= (total - 2) and nums[1][0] * 2 <= (total - 2):
            nums[0] = (nums[0][0] - 2, nums[0][1])
            total -= 2
            result.append(nums[0][1] + nums[0][1])
        elif (nums[0][0] - 1) * 2 <= (total - 1) and nums[1][0] * 2 <= (total - 1):
            nums[0] = (nums[0][0] - 1, nums[0][1])
            total -= 1                    
            result.append(nums[0][1])
        else:
            nums[0] = (nums[0][0] - 1, nums[0][1])
            nums[1] = (nums[1][0] - 1, nums[1][1])
            total -= 2
            result.append(nums[0][1] + nums[1][1])
    
    print('Case #' + str(i + 1) + ': ' + ' '.join(result))