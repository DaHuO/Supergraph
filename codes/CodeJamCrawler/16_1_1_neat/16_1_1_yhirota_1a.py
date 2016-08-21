
# coding: utf-8

# In[4]:

from sets import Set
import numpy as np

f = open('1as')
in_lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines2: リスト。要素は1行の文字列データ

case_count = int(in_lines[0])

numbers = []
outlines = []
for i in range(case_count):
    string = in_lines[i+1]
    
    last_word = ""
    
    for j in range(len(string)):
        # last_wordがないならそのまま追加。
        if last_word == "":
            last_word += string[j]
        else:
            #当該文字と今の頭文字を比較
            if string[j] >= last_word[0]:
                #前方に追加
                last_word = string[j] + last_word
            else:
                last_word += string[j]
    outlines.append("Case #%d: %s" % (i+1, str(last_word)))
    
f = open('out.txt', 'w') # 書き込みモードで開く
f.writelines(outlines) # シーケンスが引数。
f.close()


# In[ ]:



