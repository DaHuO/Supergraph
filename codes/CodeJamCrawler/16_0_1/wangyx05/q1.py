def countsleep(input, output, n):
    for i in range(n):
        if input[i] is 0:
            output.append(0)
            continue
        nums = set()
        j = 1
        curr_n = input[i]
        while len(nums) != 10:
            tmp = int(curr_n * j)
            while (int(tmp) != 0):
                nums.add(int(tmp) % 10)
                #print(int(tmp) % 10)
                tmp /= 10
            j += 1
        output.append(curr_n * (j-1))


input = []
output = []
with open("A-large.in") as f:
    n = int(f.readline())
    for l in f:
        input.append(int(l))

countsleep(input, output, n)
with open("output.out", "w") as f:
    for i in range(n):
        if output[i] == 0:
            f.write("Case #" + str(i+1) + ": INSOMNIA\n")
        else:
            f.write("Case #" + str(i+1) + ": " + str(output[i]) + "\n")
