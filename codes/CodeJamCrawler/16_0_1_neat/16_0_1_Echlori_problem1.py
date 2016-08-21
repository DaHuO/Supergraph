
# coding: utf-8

# In[6]:

def check_number(string,check_array):
    for c in string:
        if check_array[int(c)] == 0:
            check_array[int(c)] = 1
    return check_array
    


# In[33]:

inputfile = 'A-small-attempt0.in'
f = open(inputfile, 'r')

outputfile = 'output.txt'
g = open(outputfile, 'w')

line_no = 0
for line in f:
    number = line
    if line_no > 0:
        check_array = [0 for col in range(10)]
        for i in range(1,100):
            string = str(i*int(number))
            check_array = check_number(string,check_array)
            if sum(check_array) == 10:
                to_write = 'Case #' + str(line_no) + ': ' + string + '\n'
                g.write(to_write)
                break
            if i == 99:
                to_write = 'Case #' + str(line_no) + ': INSOMNIA' + '\n'
                g.write(to_write)
    line_no += 1


# In[ ]:



