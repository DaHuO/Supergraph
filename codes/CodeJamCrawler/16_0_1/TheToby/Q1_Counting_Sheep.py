'''
Created on 9 Apr 2016

@author: toby8
'''

with open("A-Large.in" , "r") as fin:
    filein = fin.read().splitlines()
filein.pop(0)
filein = map(int,filein)
digits = {"0","1","2","3","4","5","6","7","8","9"}

times = 1
with open("output.in", "w") as fout:
    for n in filein:
        i = 1
        temp = set()
        nstring = str(n)
        for c in nstring:
            temp.add(c)
        while digits!=temp:
            if n == 0: break
            nstring = str(n*i)
            for c in nstring:
                temp.add(c)
            i+=1
        srt1 = ""
        if n == 0: str1 = "CASE #%s: INSOMNIA" % (times)
        else: str1= "CASE #%s: %s" % (times,n*(i-1))
        fout.writelines(str1 + "\n")
        times+=1
print "done"