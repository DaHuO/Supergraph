import sys

N = int(sys.stdin.readline())

def count(num):
    if num == 0:
        return "INSOMNIA"
    n = num
    nums = set()
    nums.update(str(num))    
    while len(nums) < 10:
        num += n
        nums.update(str(num))

    return num


for case in range(N):
    num = int(sys.stdin.readline())
    print("Case #" + str(case + 1) + ":", count(num))    
