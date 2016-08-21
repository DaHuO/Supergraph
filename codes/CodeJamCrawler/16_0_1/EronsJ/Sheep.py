import random

__author__ = 'Erons J'





def strategy( Nu, case ):
    index = 1
    digitaccount = {}
    Check = [11,11,11,11,11,11,11,11,11,11]
    while(index < 101):
        N = (index) * Nu
        #print(str(Nu * index)+" =" + str((index))+"*"+str(Nu))
        for d in str(N):
            if d in digitaccount:
                pass
            else:
                digitaccount[d] = 1
                Check[int(d)] = int(d)
            if len(digitaccount) == 10:
                return "Case #"+str(case)+": "+str(N)
                #print(Check)
                #print(digitaccount)

        index += 1
    #print(Check)
    #print(digitaccount)
    return "Case #"+str(case)+": INSOMNIA"

#
# file = open("output.txt","w")
# input = open("input.txt", "r")
# i = 0
# for N in input:
#     if i == 0:
#         i+=1
#         continue
#     print(str(N)+" " + strategy(int(N),i))
#     file.write(strategy(int(N),i)+"\n")
#     if i == 100:
#         break;
#     i+=1
#
#
# print(i)