from sets import Set
import numpy as np

f = open('A-large.in')
lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines2: リスト。要素は1行の文字列データ
 
numbers = []
for line in lines:
    numbers.append(int(line))

outlines = []
for n in range(1, numbers[0]+1):
    unique = Set()
    i=0
    while len(unique) < 10:
        if numbers[n] == 0:
            answer = "INSOMNIA"
            break
        answer = (i + 1) * numbers[n]
        
        sanswer = str(answer)
        for c in range(0, len(sanswer)):
            unique.add(sanswer[c:c+1])
        i += 1
    outlines.append("Case #%d: %s\n" % (n, str(answer)))
    
f = open('out.txt', 'w') # 書き込みモードで開く
f.writelines(outlines) # シーケンスが引数。
f.close()