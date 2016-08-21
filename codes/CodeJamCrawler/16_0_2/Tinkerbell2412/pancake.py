with open('B-large.in', 'r') as f:
    read_data = f.read()

# print read_data
data_from_file = read_data.split()
# print data_from_file
no_of_entries = data_from_file.pop(0)
# print no_of_entries
# print data_from_file
list_of_nos = []
done = 0
num = 0
    
def flip(list, index):
    # print list
    for x in range(0,index+1):
        if list[x] == False:
            list[x] = True
        else:
            list[x] = False
    # print list
    # exit()
    return list
    
for i in range(0, int(no_of_entries)):
    list_of_p_m = list(data_from_file[i])
    list_of_nos = [False] * len(list_of_p_m)
    for x in range(0, len(list_of_p_m)):
        if list_of_p_m[x] == '+':
            list_of_nos[x] = True
        else:
            list_of_nos[x] = False
    # print list_of_nos
    if list_of_nos.count(True) == len(list_of_nos):
        num = 0
        done = 1
    else:
        num = 0
        for x in range(len(list_of_nos)-1, -1, -1):
            if (list_of_nos[x] == True):
                # print list_of_nos
                continue
            else:
                # print list_of_nos
                list_of_nos = flip(list_of_nos, x)
                num += 1
                # print num   
                # print list_of_nos
            if list_of_nos.count(True) == len(list_of_nos):
                # print "done!"
                # exit()
                done = 0;
                break
            
        # print list_of_nos.count(True)
        
    print 'Case #'+str(i+1)+': '+str(num)
