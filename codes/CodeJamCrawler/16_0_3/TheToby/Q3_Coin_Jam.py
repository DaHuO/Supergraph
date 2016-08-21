'''
Created on 9 Apr 2016

@author: toby8
'''
'''with open("2T_part1.txt", "r") as fin:
    filein = fin.read().splitlines()

out = set()
for i in filein:
    s = i.split(' ')
    for nums in s[0].split('\t'):
        out.add(int(nums))

with open("out2.txt", "w") as fout:
    for num in out:
        fout.write(str(num) + "\n")'''

from math import sqrt
def get_divisor(val):
    i = 1
    while(True):
        if(i>sqrt(val)): return(-1)
        i+=1
        if(val % i == 0): return i
        
def get_and_print_divisor(bin_string, counter):
    outs = [bin_string]
    for i in range(2, 11):
        current_val = int(bin_string, i)
        divisor = get_divisor(current_val) 
        outs.append(divisor)
    return " ".join(str(v) for v in outs)
    
with open("out2.txt", "r") as fin:
    filein = fin.read().splitlines()

out = set()
for i in filein:
    out.add(int(i))
print "Set Made: WE DONE"

answer = []

n = input()
j = input()
s = 2**(n-1)+1

for i in xrange(0,(2**(n-2)-1)):
    s+=2
    
    flag = True
    temp = bin(s)[2:]
    for i in xrange(2,11):
        var = int(temp,i)
        if var in out:
            flag = False
            break
        
    if flag:
        answer.append(temp)
    
    if len(answer)>=j:
        break


answer1 = []
for num in answer:
    answer1.append(get_and_print_divisor(num, 1))
    print "."


with open("output.in", "w") as fout:
    fout.write('Case #1:\n')  
    count = 0
    for i in answer1:
        if i.find("-1") == -1:
            fout.write(i+"\n")
            count+=1
        if count >49:break
    
                
    
        
    