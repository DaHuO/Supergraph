#!/usr/bin/python

f = open('A-small.in','r')
#dataset = open('A-large.in','r')

def solve(num, p_set):
    ALP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    while(int(num) != 0):
        index_1 = 0
        index_2 = 0
        max = 0
        pair=""

        for i in range(0, len(p_set)):
            i = int(i)
            if (int(p_set[i]) > int(max)):
                max = p_set[i]
                index_1 = i
        p_set[index_1] = int(p_set[index_1]) - 1
        pair = pair+ALP[index_1]
        #print("pair1 is "+pair)
        if(p_set[index_1] == 0):
            num = int(num) - 1

        #print(p_set)
        max = 0
        for i in range(0, len(p_set)):
            i = int(i)
            if (int(p_set[i]) > int(max)):
                max = p_set[i]
                index_2 = i
        after = int(p_set[index_2]) - 1
        if(int(after) == 0 and int(num) == 2):
            dummy = "boo"
        else:
            p_set[index_2] = int(p_set[index_2]) - 1
            pair = pair+ALP[index_2]
            #print("pair2 is "+pair)
            if(p_set[index_2] == 0):
                num = int(num) - 1

        #print("biggest is "+str(max)+" at "+str(index_1)+" th")
        #print(p_set)
        res.append(pair)

    return res

data = f.readlines()
num = data[0]
del data[0]
data.pop()
prob_num = 1
for i in range(0, len(data),2):
    num_of_senate = data[i].strip()
    #print(str(num_of_senate))

    p_set = data[i+1].strip().split(" ")
    #print(p_set)

    res = solve(num_of_senate, p_set)

    print("Case #"+str(prob_num)+": "+' '.join(res))
    prob_num = prob_num + 1