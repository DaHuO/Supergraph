T = int(input())

for t in range(1, T+1):
    orig = N = int(input())

    print('Case #{}: '.format(t), end='')

    nums = set(c for c in str(N))
    
    if N == 0:
        print('INSOMNIA')
        continue

    while len(nums) < 10:
        N += orig
        nums.update(set(c for c in str(N)))

    print(N)
        


