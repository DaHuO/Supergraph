
# coding: utf-8

# In[18]:

from sets import Set
import numpy as np

f = open('B-large.in')
lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines2: リスト。要素は1行の文字列データ
 
num_case = int(lines[0])

data = []
# convert
for i in range(num_case):
    data.append(lines[i+1].rstrip())

outlines = []
for i in range(num_case):
    #flip数をカウント
    flip_count = 0
    this_data = data[i]
    for j in range(len(this_data)):
        if j+1 == len(this_data):
            break
        elif this_data[j] != this_data[j+1]:
            flip_count += 1
            
    #末尾の符号が0か否か
    if this_data[len(this_data)-1] == "-":
        flip_count += 1
        
    outlines.append("Case #%d: %d\n" % (i+1, flip_count))
    
f = open('out_qbl.txt', 'w') # 書き込みモードで開く
f.writelines(outlines) # シーケンスが引数。
f.close()


# In[ ]:



