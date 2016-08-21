def rank_and_file(r):
    res = ""
    for n in r:
        res = res + " " + str(n)

    return res.strip()


test_cases = int(input())
for tc in range(test_cases):
    nums = [0]*2501
    num_lines = int(input()) * 2
    for n in range(num_lines-1):
        temp = input().split(" ")
        for t in temp:
            t = int(t)
            if nums[t] > 0:
                nums[t] = 0
            else:
                nums[t] = t

    result = list(set(nums))[1::]
    result.sort()
    result_txt = "Case #" + str(tc+1) + ": "
    print(result_txt, rank_and_file(result), sep="")
