t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 1
    while not all(nums):
        if n == 0:
            result = 0
            break
        str_n = list(str(n * count))
        for s in str_n:
            if nums[int(s)] == 0:
                nums[int(s)] = 1
        result = n * count
        count += 1
    if result == 0:
        result = 'INSOMNIA'
    print('Case #{0}: {1}'.format(i + 1, result))
