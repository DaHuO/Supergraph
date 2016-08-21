def solve(sorted_nums):
    #find odd numbers of numbers
    prev = -1
    count = 0
    missing_list = []
    for curr in sorted_nums:

        if curr == prev:
            count +=1
        else:
            if prev != -1 and (count % 2) == 1:
               missing_list.append(prev)
            prev = curr
            count = 1

    if prev != -1 and (count % 2) == 1:
        missing_list.append(prev)
    missing_list = map(str, missing_list)
    formatted_list = " ".join(missing_list)
    return formatted_list

if __name__ == "__main__":
    testcases = eval(input())
    for case_num in range(1, testcases+1):
        N = eval(input())
        height_grid = []
        for i in range(N*2-1):
            for x in input().split():
                height_grid.append(int(x))

        #preprocess
        sg = sorted(height_grid, reverse=False)

        print("Case #%i: %s" % (case_num, solve(sg)))
