
# coding: utf-8

# In[ ]:

def counting_sheep(n):
    num_list =[]
    temp_n = int(n)
    if int(n) == 0:
        return "INSOMNIA"
    else:
        while len(num_list) != 10:
            for i in list(str(temp_n)):
                if i not in num_list:
                    num_list.append(i)
            temp_n += int(n)
        return temp_n-int(n)
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = input()  # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i, counting_sheep(n)))

