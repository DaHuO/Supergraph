
hasSeenAll = False

numCases = int(input())

for case in range(1, numCases+1):

    N = input()
    if(N == '0'):
        print("Case #{}: INSOMNIA".format(case))
        continue
    else:
        count = 1
        N = int(N)
        nums = [0,1,2,3,4,5,6,7,8,9]
        while (hasSeenAll != True):
            current = count * N

            #split the current number
            currentSplt = [int(i) for i in str(current)] 

            #remove any duplicates
            currentSplt = set(currentSplt)

            #keep track of numbers seen
            for i in currentSplt:
                if(i in nums):
                    nums.pop(nums.index(i))

            #check if we've seen all numbers
            if(len(nums) == 0):
                hasSeenAll = True
                print("Case #{}: {}".format(case, current))

            count += 1


    hasSeenAll = False
