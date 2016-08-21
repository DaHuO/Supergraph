

def find_all_digits(tmp_nums,digits,N):
    if N == 0:
        return "INSOMNIA"

    for num in tmp_nums:
        for digit in str(num):
            digits[int(digit)] = int(digit)

    if -1 not in digits:
        return True
    else:
        return False

t = int(input())
nums = []
find = False

for x in range(0,t):
    nums.append(int(input()))
indx = 0

for N in nums:
    indx += 1
    tmp_nums = []
    counter = 1
    digits = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    find = False
    last_num = N

    while find == False and find != "INSOMNIA":
        tmp_nums.append(N*counter)
        find = find_all_digits(tmp_nums,digits,N)
        last_num = N*counter
        counter += 1

    if find == "INSOMNIA":
        print("Case #{}: {}".format(indx,find))
    else:
        print("Case #{}: {}".format(indx,last_num))