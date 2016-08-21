input_file = 'A-large.in'
output_file = 'A-large.out'
in_file = open(input_file)
out_file = open(output_file,'w')

counter = 0
for line in in_file:
    if counter > 0:
        N = int(line.strip())
        length_of_N = 10000
        last_N = int(line.strip())
        i = 0
        num = '0123456789'
        num_list = list(num)
        len_list = len(num_list)
        list_not_reduced = 0
        while True:
            i+=1
            last_len_list = len_list
            last_N = i*N
            #print set(list(str(last_N)))
            num_list = list(set(num_list)-set(list(str(last_N))))
            len_list = len(num_list)
            if last_len_list == len_list: 
                list_not_reduced+=1
            #print "%s | %s  | %s  | %s  | %s  | %s" % (N, i,last_len_list,last_N,len_list,list_not_reduced)
            if not num_list: 
                break
            if list_not_reduced == length_of_N:
                last_N = -1
                break
        if last_N < 0:
            out_str = 'INSOMNIA'
        else :
            out_str = str(last_N)
        if counter > 0:
            print("Case #{}: {}".format(counter,out_str))
            out_file.writelines("Case #{}: {}\n".format(counter,out_str))
    counter += 1
out_file.close()