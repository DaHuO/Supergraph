import os


in_file = 'f.in'
o_file = 'results.out'
cases = 0


is_first = True
counter = 0

out_lines = []

iopen = open(in_file, 'r')


def process_line(line):
    global out_lines,needed_nums
    current_num = int(line)
    orig_num = int(line)
    needed_nums = [0,1,2,3,4,5,6,7,8,9]
    found_nums = []
    print(current_num)
    inner_count = 1


    ## pre list ###
    current_list = list(map(int,list(str(current_num))))


    if current_num == 0:
        out_lines.append('Case #' + str(counter)+': ' + 'INSOMNIA')
        return
    elif current_list[0] == 1 and (len(set(current_list)) == 1) and len(current_list)  > 1:
        #print('CASE --- ' + str(counter))
        #print(current_num)
        #print(len(set(current_list)))
        #print(len(current_list))
        #print('\n')
        final_num = current_num * 10
        out_lines.append('Case #' + str(counter)+': ' + str(final_num))
        return

    elif len(current_list) > 1 and current_list[0] == 1 and current_list[1] == 0 and len(set(current_list[1:])) == 1:
        print('CASE --- ' + str(counter))
        print(current_num)
        print(len(set(current_list)))
        print(len(current_list))
        print('\n')
        final_num = current_num * 9
        out_lines.append('Case #' + str(counter)+': ' + str(final_num))
        return

    while(len(needed_nums) > 0):
        strnum = str(current_num)
        l = list(map(int,list(strnum)))
        l.sort()

        for x in needed_nums[:]:
            #print(x)
            #print(l)
            if x in l:
                #print('removing ' + str(x))
                needed_nums.remove(x)
                found_nums.append(x)

        if(len(needed_nums) != 0):
            current_num = orig_num * inner_count

        inner_count = inner_count + 1

    out_lines.append('Case #' + str(counter)+': ' + str(current_num))
    return


def write_line():
    ofile = open(o_file,'w')
    for o in out_lines:
        ofile.write(o)
        ofile.write('\n')
        print(o)
    ofile.close()


for line in iopen:
    if counter == 0:
        cases = int(line)
        counter = counter + 1

        continue
    process_line(line)
    counter = counter + 1

write_line()

iopen.close()


