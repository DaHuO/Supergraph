def toLetter(n):
    if (n == None):
        return ''

    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[n]


def f(nums):
    order = []
    firstFlag = True
    
    while(True):
        flag = False
        for i,n in enumerate(nums):
            if (n > 0):
                order.append(i)
                nums[i] -= 1
                flag = True

        if (firstFlag and len(nums) == 3):
            firstFlag = False
            order.append(None)

        if (not flag):
            break

    if (len(order)%2 == 1):
        order.append(None)

    ans = []
    order.reverse()
    for i in range(0, len(order), 2):
        ans.append(toLetter(order[i]) + (toLetter(order[i+1]) if i+1<len(order) else ''))
                   
    return ' '.join(ans)
                   
                   
t = int(input())
for i in range(t):
    n = input()
    nums = list(map(int, input().split()))

    print('Case #' + str(i+1) + ':', f(nums))
    

    
