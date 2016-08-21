
# coding: utf-8

# In[ ]:




# In[20]:

input_txt = 'B-large.in'
with open (input_txt, 'r', encoding= 'utf8') as questions:
    case_number = int(questions.readline())
    print(case_number)
    i = 0
    ans = []
    while i < case_number:
        cake_state = questions.readline().strip()
        print(cake_state)        
        flip_count = 0
        if len(cake_state) > 1:
            for j in range(len(cake_state)-1):
                if cake_state[j] != cake_state[j+1]:
                    flip_count += 1
        if cake_state[len(cake_state)-1] == '-':
            flip_count += 1
        ans.append(flip_count)
        i += 1
    print (ans)


# In[21]:

"""
output should be
Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3
"""
output_file = 'B-large.out'
with open(output_file, 'w', encoding='utf8') as fw:
    for i in range(case_number):
        fw.write('Case #%d: %d\n' % (i+1, ans[i]))


# In[ ]:



