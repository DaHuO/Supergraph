import sys
import os

def check_num(n,num_string,digits):
    num_check = int(num_string) * n
    num_check = str(num_check)
    if num_string == '0':
        return "INSOMNIA"
    for ch in num_check:
        ch = int(ch)
        if ch in digits:
            digits.remove(int(ch))
    if len(digits) == 0:
        return num_check
    return check_num(n+1,num_string,digits)

def pancake_flip_recurse(pancakes,num_flips):
    if '-' not in pancakes:
        return num_flips
    #if(pancakes[0] is '+'):
    #    return pancake_flip_recurse(flip_values(pancakes[:1]) + pancakes[1:],num_flips + 1)
        #base
    else:
        for x in range(len(pancakes)):
            try:
                if pancakes[x + 1] is not pancakes[x]:
                    return pancake_flip_recurse(flip_values(pancakes[:x+1]) + pancakes[1+x:], num_flips +1)
                else:
                    continue
            except:
                #i'm at the end of the list fliip everything
                return pancake_flip_recurse(flip_values(pancakes),num_flips + 1)

def flip_values(pancakes):
    for x in range(len(pancakes)):
        if pancakes[x] is '-':
            pancakes[x] = '+'
        else:
            pancakes[x] = '-'
    return pancakes


# def pancake_flip(pancakes):
#     flip_count = 0
#     while '-' in pancakes:
#         for i in range(len(pancakes)):
#             if pancakes[i] is '+':
#                 pancakes[i] = '-'
#                 flip_count = flip_count + 1
#                 break
#             if pancakes[i] is '-':
#                 try:
#                     if pancakes[i + 1] is '+':
#                         flip_count = flip_count + 1
#                         for j in range(i + 1):
#                             if pancakes[j] is '-':
#                                 pancakes[j] = '+'
#                                 break
#                             else:
#                                 pancakes[j] = '-'
#                                 break
#
#                     else:
#                         pass
#                 except:
#                     flip_count = flip_count + 1
#                     #flip everything
#                     for j in range(len(pancakes)):
#                         if pancakes[j] is '-':
#                             pancakes[j] = '+'
#                         else:
#                             pancakes[j] = '-'
#                 #check next item
#                 #if next item is plus - flip all earlier items
#                 #if next item is - # do nothing
#                 #if no items exist, flip everything
#
#     return flip_count




file_name = sys.argv[1]
file_out = open('output.txt','w')
test_list = None
line_num = 0
flips = 0
with open(file_name) as fp:
    for line in fp:
        if line_num != 0:
            flip_count = 0
            line = line.strip()
            flips = pancake_flip_recurse(list(line),0)
            file_out.write('Case #{0}: {1}\n'.format(line_num,flips))
            line_num = line_num + 1
        else:
            line_num = line_num + 1

#check if string contains _