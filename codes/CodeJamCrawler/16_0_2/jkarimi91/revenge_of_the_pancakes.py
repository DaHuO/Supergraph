
# coding: utf-8

# In[ ]:

t = int(raw_input())
for case in range(1,t+1):
    side = str(raw_input())
    side = list(side[::-1])
    manuevers = 0
    for i in range(len(side)):
        if side[i] == '-':
            manuevers += 1
            for j in range(i,len(side)):
                if side[j] == '-':
                    side[j] = '+'
                else:
                    side[j] = '-'
    print "Case #{}: {}".format(case,manuevers)

