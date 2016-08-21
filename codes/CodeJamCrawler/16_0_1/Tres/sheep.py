import fileinput

if __name__ == "__main__" :

    test_case = 1
    for line in fileinput.input() :
        nums = [ False for i in range(10) ]
        last_num = 0
        if fileinput.isfirstline() :
            continue

        val = int(line)
        mult = 1

        while not all(nums) :
            if mult * val == last_num :
                last_num = "INSOMNIA"
                break

            res = mult * val
            last_num = res

            if res == 0 :
                nums[res] = True

            while res > 0 :
                nums[ res % 10 ] = True
                res //= 10

            mult += 1

        print("Case #{}: ".format(test_case), end="")
        print(last_num)
        test_case += 1