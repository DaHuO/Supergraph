
# coding: utf-8

# In[ ]:




# In[16]:

input_txt = 'A-large.in'
with open (input_txt, 'r', encoding= 'utf8') as questions:
    case_number = int(questions.readline())
    print(case_number)
    i = 0
    ans = []
    while i < case_number:
        digit_set = set()
        number = int(questions.readline())
        print (number)
        for j in range(1000000):
            
            temp_number_instr = str((j+1)*number)
            for digit in temp_number_instr:
                digit_set.add(digit)
            if len(digit_set) == 10:
                ans.append(temp_number_instr)
                break
        if len(digit_set) !=10:
            ans.append('INSOMNIA')
        i += 1
    print (ans)


# In[17]:

"""
output should be
Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3
"""
output_file = 'A-large.out'
with open(output_file, 'w', encoding='utf8') as fw:
    for i in range(case_number):
        fw.write('Case #%d: %s\n' % (i+1, ans[i]))


# In[ ]:



