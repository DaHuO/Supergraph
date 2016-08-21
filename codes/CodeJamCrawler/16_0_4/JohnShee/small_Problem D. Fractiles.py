
# coding: utf-8

# In[22]:


input_txt = 'D-small-attempt1.in'
with open (input_txt, 'r', encoding= 'utf8') as questions:
    case_number = int(questions.readline())
    print(case_number)
    j = 0
    ans = []
    while j < case_number:
        K, C, S = [int(i) for i in (questions.readline().split())]        
        
        if C == 1:
            if S < K:
                ans.append('IMPOSSIBLE')
            else :
                ans.append([i for i in range(1, K+1)])
        else:
            if S < K-1:
                ans.append('IMPOSSIBLE')
            else:
                if K == 1:
                    ans.append([1])
                else:
                    ans.append([(i*(K**(C-1))+i+2) for i in range(K-1)])
        j += 1
    print (ans)


# In[23]:

# In[15]:

"""
output should be
Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3
"""
output_file = 'D-small-attempt1.out'
with open(output_file, 'w', encoding='utf8') as fw:
    for i in range(case_number):
        if ans[i] == 'IMPOSSIBLE':
            fw.write('Case #%d: %s' % ((i+1), ans[i]))
        else:
            fw.write('Case #%d: ' % (i+1))
            for j in ans[i]:
                fw.write(str(j)+' ')
        fw.write('\n')


# In[ ]:


# In[ ]:



