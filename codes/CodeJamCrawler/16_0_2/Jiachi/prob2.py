
fh = open('prob2.txt','w')

testcase_num = int(input())
testcase_idx = 0
while testcase_idx < testcase_num:
    line = input()
    pancake_list = list(line)
    rotate_idx = 0
    while len(pancake_list) != 0:
        #input()
        #print(pancake_list)
        if pancake_list[-1] == '+':
            pancake_list.pop()
        elif pancake_list[0] == '-' and pancake_list[-1] == '-':
            rotate_idx += 1
            #print("add idx")
            new_pancake_list = list()
            for pancake_idx in range(len(pancake_list)):
                #print(pancake_idx,pancake_list)
                if pancake_list[pancake_idx] == '-':
                    new_pancake_list.append('+')
                elif pancake_list[pancake_idx] == '+':
                    new_pancake_list.append('-')
            pancake_list = new_pancake_list
        elif pancake_list[0] == '+' and pancake_list[-1] == '-':
            rotate_idx += 1
            for pancake_idx in range(len(pancake_list)):
                if pancake_list[pancake_idx] == '+':
                    pancake_list[pancake_idx] = '-'
                else:
                    break
    fh.write("Case #"+str(testcase_idx+1)+': '+str(rotate_idx)+'\n')
    testcase_idx += 1
fh.close()
