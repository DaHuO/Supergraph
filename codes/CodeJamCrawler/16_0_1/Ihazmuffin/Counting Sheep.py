__author__ = 'Hunter'

digits = []
nums = []

f = open("A-large.in", "r")
for line in f:
    nums = f.readlines()

nums = [int(x) for x in nums]

print(nums)
f.close()

ncases = (len(nums))
#ncases = 1000001

for i in range (ncases):
    #print("APPENDING")
    digits.append([])

for i in range (len(nums)):
    factor = 1
    my_num = 0

    if nums[i] == 0:
        print ("CASE #" + str(i+1) + ": INSOMNIA")
        continue

    while len(digits[i]) != 10:
        my_num = nums[i] * factor
        my_str = str(my_num)
        factor += 1

        for j in range (len(my_str)):
            if my_str[j] not in digits[i]:
                digits[i].append(my_str[j])

    print("CASE #" + str(i+1) + ": " + my_str)