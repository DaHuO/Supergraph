import itertools

def base2to10(n):
    bases = []
    for i in range(2,11):
        bases.append(int(str(n),i))
    return bases

def primality_check(base):
    numbers = [2,3,5,7,9]
    for num in numbers:
        if base % num == 0:
            return num
            print num, base
            break
    return 0

def f(nums,j):
    result = []
    for num in nums:
        bases = base2to10(num)
        intermediate = []
        intermediate.append(num)
        for base in bases:
            test = primality_check(base)
            if test > 0:
                intermediate.append(test)
            if len(intermediate) == 10:
                result.append(intermediate)
        if len(result) == j:
            return result

def coin_jam_create(num):
    num.append(1)
    num.insert(0,1)
    num = int(''.join(map(str,num)))
    return num


with open("C-small-attempt0.in", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

n, j = map(int,array[1].split(' '))

nums = map(list, list(itertools.product([0,1], repeat=n-2)))
nums = map(coin_jam_create, nums)
result = f(nums,j)


file = open('small-result.txt', 'w')
file.write("CASE #1: \n")
for res in result:
    res =  ' '.join(str(e) for e in res)
    file.write(res + '\n')

