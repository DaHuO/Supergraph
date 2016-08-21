import string
tests = int(input())
def check(lb, a):
    l = lb[:]
    l[a] -= 1
    for i in range(0, len(l)):
        if sum(l)/2 < l[i]:
##            print(l)
##            print(i)
            return False
    return True

def check0(l):
    for i in range(0, len(l)):
        if l[i] != 0:
            return False
    return True

for i in range(0, tests):
    parties = int(input())
    line = input()
    nums = line.split()
    for e in range(0, len(nums)):
        nums[e] = int(nums[e])
    alpha = list(string.ascii_uppercase)
    final = ""
    while not check0(nums):
##        print(nums)
        a = nums.index(max(nums))
        final += alpha[a]
        nums[a] -= 1
##        print("b", nums)    
        b = nums.index(max(nums))
        if check(nums, b):
            final += alpha[b]
##            print(b)
            nums[b] -= 1
        final += " "
    print("Case #" + str(i+1) + ": " + final)
    
