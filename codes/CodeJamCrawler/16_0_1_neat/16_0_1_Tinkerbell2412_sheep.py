with open('A-large.in', 'r') as f:
    read_data = f.read()

# print read_data
data_from_file = read_data.split()
# print data_from_file
no_of_entries = data_from_file.pop(0)
# print no_of_entries
# print data_from_file
done = 0
for i in range(0, int(no_of_entries)):
    list_of_nos = [False] * 10
    factor = int(data_from_file[i])
    num = factor
    if factor == 0:
        print 'Case #'+str(i+1)+': INSOMNIA'
        continue
    else:
        while 1:
            
            num_list = list(str(num))
            for x in range(0,len(list_of_nos)):
                if ((list_of_nos[x] == False) and (str(x) in num_list)):
                    list_of_nos[x] = True;
                    # print list_of_nos
                if list_of_nos.count(True) == 10:
                    # print "done!"
                    done = 1;
                    break
            # print list_of_nos.count(True)
            if done == 1:
                # print "done!"
                done = 0
                break
            num += factor
    print 'Case #'+str(i+1)+': '+str(num)