
def solve(file):
    f = open(file,'r')
    nums = [x.strip('\n') for x in f.readlines()]
    t = int(nums[0])
    cases = nums[1:]
    case = 0

    for k in cases:
        num = int(k)
        i = 1
        digits = []
   #     print(digits)
        while digits != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            multiple = num * i
            if multiple == 0:
                multiple = "INSOMNIA"
                break
            else:
                n = str(multiple)
                for c in n:
                    if int(c) not in digits:
                        digits.append(int(c))
                digits.sort()
 #               print(digits)
                i += 1
        case += 1
        print("Case #{}: {}".format(case, multiple))
