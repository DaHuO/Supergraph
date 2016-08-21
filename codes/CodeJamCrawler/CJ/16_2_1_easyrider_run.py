#!/usr/bin/python3
import numpy

nr_of_tasks = int(input())


num2str = {0 : "ZERO", #
           1 : "ONE", #
           2 : "TWO", #
           3 : "THREE",
           4 : "FOUR", #
           5 : "FIVE", #
           6 : "SIX", #
           7 : "SEVEN",
           8 : "EIGHT", #
           9 : "NINE"} #

"""
0
2
4
3
1
6
7
5
8
9
"""

num_order = [0,2,4,3,1,6,7,5,8,9]

#num_order = [0, 9, 4, 6, 8, 2 , 5, 3, 7, 1]

def check_number(inp_str, number):
    for chara in num2str[number]:
        try:
            if inp_str.index(chara) < 0:
                return 0
        except:
            return 0

    for chara in num2str[number]:
        try:
            del inp_str[inp_str.index(chara)]
        except:
            pass
    return 1

for task_index in range(1,nr_of_tasks+1):
    inp = input()
    inp_list = [ch for ch in inp]
    nums = {0: 0,  #
            1: 0,  #
            2: 0,  #
            3: 0,
            4: 0,  #
            5: 0,  #
            6: 0,  #
            7: 0,
            8: 0,  #
            9: 0}  #

    for num in num_order:
        temp = 1
        while True:
            if check_number(inp_list, num) == 1:
                nums[num] = nums[num] + 1
            else:
                break
    result = []
    for key in nums:
        for i in range(0,nums[key]):
            result.append(key)




    print("Case #{task}: {result}".format(task=task_index,
                             result="".join([str(ind) for ind in result])))