test = int(input().strip())
temp = []
for i in range(test):
    numbers = []
    n = int(input().strip())
    k = 1
    while True:
        num = n * k

        if (num == n) and (k != 1):
            str1 = "Case #" + str(i+1) + ": " + "INSOMNIA"
            temp.append(str1)
            break

        new_num = str(num)

        for j in new_num:
            if j in numbers:
                continue
            else:
                numbers.append(j)

        if len(numbers) == 10:
            str2 = "Case #" + str(i+1) + ": " + str(num)
            temp.append(str2)
            break

        k += 1

for i in temp:
    print(i)
