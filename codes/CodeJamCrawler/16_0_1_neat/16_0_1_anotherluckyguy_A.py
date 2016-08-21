lines = open('input.txt').readlines()
lines.remove(lines[0])
output = open('out.txt', 'w')
lines = [int(i) for i in lines]
a = 1
for it in lines:
    nums = set()
    n = 1
    good = True
    while len(nums) < 10:
        res = it * n
        for digit in str(res):
            nums.add(digit)
        print(n, nums, res * n)
        n += 1
        if n > 100:
            good = False
            break
    if good:
        output.write('Case #{}: '.format(a) + str(it * (n - 1)))
    else:
        output.write('Case #{}: '.format(a) + 'INSOMNIA')
    output.write('\n')
    a += 1
