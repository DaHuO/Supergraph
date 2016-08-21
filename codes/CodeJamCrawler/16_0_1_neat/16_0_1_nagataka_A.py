#!/usr/bin/python

dataset = open('A-small.in','r')
#dataset = open('A-large.in','r')


def check_digits(num):
    for i in range(len(num)):
        digit = num[i:i+1]
        #print("digit is "+digit)
        flag[int(digit)] = 1
    #print("checked "+num)

line_num = 0
for N in dataset:

    flag = [0,0,0,0,0,0,0,0,0,0]

    if(line_num==0):
        line_num+=1
    elif N == "\n":
        line_num+=1
    else:
        not_finished = True
        while not_finished:
            for i in range(1,201):
                iN = str( int(N)*i )
                #print("iN is "+iN+", i is "+str(i))
                check_digits(iN)
                if 0 not in flag:
                    not_finished = False
                    print("Case #"+str(line_num-1)+": "+iN)
                    break
            if not_finished == True:
                print("Case #"+str(line_num-1)+": INSOMNIA")
                break
    line_num+=1