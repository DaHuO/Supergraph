
# coding: utf-8

# In[28]:

import math
input_txt = 'C-large.in'
with open (input_txt, 'r', encoding= 'utf8') as questions:
    case_number = int(questions.readline())
    print(case_number)
    i = 0
    ans = []
    while i < case_number:
        N, J=questions.readline().split()
        N, J= int(N), int(J)
        print (N,J)
        if N%2==0:
            for j in range(J):
                ans.append([0]*10)
                number = int(2*j+2**(N/2-1)+1)
                ans[j][0] = bin(int(number+number*(2**(N/2))))[2:]
                for k in range(1,10):
                    ans[j][k] = int(bin(number)[2:], (k+1))
        else:
            for j in range(J):
                ans.append([0]*10)
                number = int(2*j+2**((N-3)/2)+1)
                ans[j][0] = bin(int(number+number*2**((N+1)/2)))[2:]
                for k in range(1,10):
                    ans[j][k] = int(bin(number)[2:], (k+1))
        i+=1
        


# In[29]:

"""
Case #1:
100011 5 13 147 31 43 1121 73 77 629
111111 21 26 105 1302 217 1032 513 13286 10101
111001 3 88 5 1938 7 208 3 20 11
"""
output_file = 'C-large.out'
with open(output_file, 'w', encoding='utf8') as fw:
    for i in range(case_number):
        fw.write('Case #%d:\n' % (i+1))
        for j in range(J):
            fw.write('%s '%ans[j][0])
            for k in range(2, 10+1):
                fw.write('%d '%ans[j][k-1])
            fw.write('\n')
            


# In[ ]:



