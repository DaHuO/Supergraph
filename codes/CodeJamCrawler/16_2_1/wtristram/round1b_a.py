def lcons(num, letrs):
    for c in num:
        if c not in letrs:
            return False
        letrs.remove(c)

    return True


t = int(input())

for tc in range(1, t + 1):
    res = []
    s = input()

    letr = [c for c in s]
    
    nums = ['SIX', 'ZERO', 'EIGHT', 'TWO', 'THREE', 'SEVEN', 'FIVE', 'FOUR', 'ONE', 'NINE']
    numm = {'EIGHT': '8', 'THREE': '3', 'SEVEN': '7', 'ZERO': '0', 'FIVE': '5', 'FOUR': '4', 'SIX': '6', 'ONE': '1', 'TWO': '2', 'NINE': '9'}

    while len(letr) > 0:
        if lcons(nums[0], [x for x in letr]):
            res.append(numm[nums[0]])


            for c in nums[0]:
                letr.remove(c)
        else:
            nums.remove(nums[0])

    res.sort()
    print("Case #{}: {}".format(tc, ''.join(res)))
