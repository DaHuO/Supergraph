file = open("./A-large.in")
limit = int(file.readline())
index = 1
while limit > 0:
    N = int(file.readline())
    if N == 0:
        print("Case #%d: INSOMNIA" % index)
    else:
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        count = 0
        while len(nums) != 0:
            count += 1
            NN = N * count
            strN = str(NN)
            for i in range(len(strN)):
                if strN[i] in nums:
                    nums.remove(strN[i])
        print("Case #%d: %s" % (index, strN))
    limit -= 1
    index += 1
