'''
Created on Apr 8, 2016

@author: Carlos
'''
f = open('D-small-attempt0.in','r')
f2 = open('D-small-attempt0.out','w')

num = 0
for line in f:
    if num==0:
        num+=1
        continue
    k,c,s = line.split(" ")
    rango = range(1,int(s)+1)
    f2.write("Case #{0}: {1}\n".format(str(num)," ".join([str(x) for x in rango])))
    num+=1
f.close()
f2.close()