import random
from math import sqrt
def find_divs(num_str):
    divs = []
    for i in range(2, 11):
        for j in range(2, int(sqrt(int(num_str, i)) + 1)):
            if int(num_str, i) % j == 0:
                divs.append(str(j))
                break
    return divs


def main():
    raw_input()
    #no for loop since n = 1 always
    nums = raw_input().split()
    n = int(nums[0])
    J = int(nums[1])
    found_nums = []
    for i in range(J):
        test_num = "1"*n
        while len(find_divs(test_num)) != 9 or test_num in found_nums:
            test_num  = "1" + "".join(random.choice("10") for x in range(n - 2)) + "1"
        divs = find_divs(test_num)
        found_nums.append(test_num)
        print test_num + " " + " ".join(divs)

if __name__ == '__main__':
    main()