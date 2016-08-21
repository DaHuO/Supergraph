
# coding: utf-8

# In[31]:

def get_digits(x):
    digits=[]
    for i in str(x):
        digits.append(i)
    return list(set(digits))
def multiply(x,y):
    return int(x)*int(y+1)


# In[37]:

already_seen=[]
full = ['1','2','3','4','5','6','7','8','9','0']
open_file=open("/Users/sp3ctr3/Downloads/A-small-attempt1.in","r")
output = open("output","w")
number = int(open_file.readline().strip())
for i in range(number):
    change_counter = 0
    ins = False
    workable = int(open_file.readline().strip())
    already_seen= get_digits(workable)
    x=workable
    previous=[]
    case_number = i+1
    for k in range(1,1000):
        if set(previous)==set(already_seen):
            change_counter += 1
        l = get_digits(x) 
        for j in l:
            if j not in already_seen:
                already_seen.append(j)
        if set(already_seen) == set(full):
            output.write("Case #"+str(case_number)+": "+str(x)+"\n")
            break
        previous = already_seen
        if change_counter == 100:
#             print previous, already_seen
            ins = True
            break
        x=multiply(workable,k)
    if ins:
        output.write("Case #"+str(case_number)+": INSOMNIA\n")
output.close()


# In[9]:

full = ['1','2','3','4','5','6','7','8','9','0']
set(full)

