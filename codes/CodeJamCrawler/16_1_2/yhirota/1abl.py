
# coding: utf-8

# In[13]:

from sets import Set
import numpy as np

f_in = open('1abl')

# lines2: リスト。要素は1行の文字列データ

case_count = int(f_in.readline())

numbers = []
outlines = []
answers = []
for i in range(case_count):
    size = int(f_in.readline())
    
    odd_dict = {}
    for j in range(2*size-1):
        
        
        line = f_in.readline()
        numbers = line.split(" ")
        
        for k in range(len(numbers)):
            number = int(numbers[k].rstrip())
            
            if number in odd_dict:
                del odd_dict[number]
            else:
                odd_dict[number] = True
    
    answer = odd_dict.keys()
    answer.sort()
    
    answer_str = "Case #%d: "%(i+1)
    for j in range(len(answer)):
        answer_str += str(answer[j]) + " "
    answer_str = answer_str.rstrip()
    answer_str += "\n"
    
    answers.append(answer_str)
        
f_out = open('out_1abl.txt', 'w') # 書き込みモードで開く
f_out.writelines(answers) # シーケンスが引数。
f_out.close()


# In[ ]:



