
# coding: utf-8

# In[26]:

from sets import Set
import numpy as np

f = open('1cal')
in_lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines2: リスト。要素は1行の文字列データ

case_count = int(in_lines[0])

numbers = []
outlines = []
for i in range(case_count):
    parties = in_lines[2*i+1]
    
    
    
    nums = str.split(in_lines[2*i+2])
    
    letter_idx = ord('a')
    dic = {}
    sumation = 0
    for j in range(len(nums)):
        dic[chr(letter_idx)] = int(nums[j])
        sumation += int(nums[j])
        letter_idx += 1
    
    line = "Case #%d: "%(i+1)
    while sumation > 0:
        for k, v in sorted(dic.items(), key=lambda x:x[1], reverse=True):
            #print k, v

            line += "%s"%(k.upper())
            dic[k] -= 1
            sumation -= 1
            
            if sumation%2==0:
                line += " "
                break
                
    line += "\n"
            
    outlines.append(line)
    
#print outlines
        
    
    
f = open('out_1cal.txt', 'w') # 書き込みモードで開く
f.writelines(outlines) # シーケンスが引数。
f.close()


# In[ ]:



