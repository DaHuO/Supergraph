
# coding: utf-8

# In[3]:

def insomnia(N):
    Numbers = {}
    count =1

    while True:
        integer = N* count
        string_integer = str(integer)
        for i in string_integer:
            if Numbers.has_key(str(i)) is False:
                Numbers[i] = 1
        count+=1

        check = 0
        for j in range(10):
            if Numbers.has_key(str(j)):
                check+=1

        if check ==10:
            Not_insomnia = False
            return(integer)
        if count > 20000:
            return("INSOMNIA")


# In[5]:

with open('A-large.txt') as input_file:
    next(input_file)
    output_file = open('output-A-large-attempt0.txt', 'w')
    i=0
    for item in input_file:
        i+=1
        output_file.write("Case #"+str(i)+": %s\n" % insomnia(int(item)))


# In[ ]:



