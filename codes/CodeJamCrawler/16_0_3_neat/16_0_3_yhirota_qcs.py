
# coding: utf-8

# In[4]:

from sets import Set
import numpy as np

N=16
J=50

out_lines = []
out_lines.append("Case #1:\n")
ok_count = 0
for i in range(2**(N-2)):
    jamcoin = "1"
    num = i
    for j in range(N-2):
        if num / 2**((N-3)-j) >= 1:
            jamcoin += "1"
        else:
            jamcoin += "0"
        num = num % 2**((N-3)-j)
    jamcoin += "1"
    
    is_true_jamcode = True
    proof = ""
    num_bases = []
    for base in range(2,11):
        num_base = 0
        for j in range(N):
            num_base += base**(N-j-1) * int(jamcoin[j])
        #print num_base
        num_bases.append(num_base)
        
        # 素数判定
        is_prime = True
        check_end = num_base
        j=2
        while j < check_end:
            if num_base % j == 0:
                proof += " " + str(j)
                is_prime = False
                break
            else:
                check_end = int(float(num_base) / j)+1
            j+=1
                
        #print is_prime
        
        if is_prime:
            is_true_jamcode = False
    
    if is_true_jamcode:
        out_lines.append("%s%s\n"%(jamcoin, proof))
        ok_count += 1
    
    if ok_count == J:     
        break
        
f = open('out_qcs.txt', 'w') # 書き込みモードで開く
f.writelines(out_lines) # シーケンスが引数。
f.close()


# In[ ]:



