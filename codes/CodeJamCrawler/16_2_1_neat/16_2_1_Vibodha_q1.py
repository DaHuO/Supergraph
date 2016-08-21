for j in range(int(input())):
    l = list(input())
    num = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    dic = {'E':0,'F':0,'G':0,'H':0,'I':0,'N':0,'O':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Z':0}
    for i in l:
        dic[i] += 1

    #print(dic)

    num[0] = dic['Z']
    dic['E'] -= dic['Z']
    dic['R'] -= dic['Z']
    dic['O'] -= dic['Z']

    num[2] = dic['W']
    dic['T'] -= dic['W']
    dic['O'] -= dic['W']

    num[4] = dic['U']
    dic['F'] -= dic['U']
    dic['O'] -= dic['U']
    dic['R'] -= dic['U']

    num[5] = dic['F']
    dic['I'] -= dic['F']
    dic['V'] -= dic['F']
    dic['E'] -= dic['F']

    num[6] = dic['X']
    dic['S'] -= dic['X']
    dic['I'] -= dic['X']

    num[7] = dic['S']
    dic['E'] -= dic['S']
    dic['V'] -= dic['S']
    dic['E'] -= dic['S']
    dic['N'] -= dic['S']

    num[8] = dic['G']
    dic['E'] -= dic['G']
    dic['I'] -= dic['G']
    dic['H'] -= dic['G']
    dic['T'] -= dic['G']

    num[1] = dic['O']
    dic['N'] -= dic['O']
    dic['E'] -= dic['O']

    num[9] = dic['I']

    num[3] = dic['T']
    
    #print(num)
    print("Case #" + str(j+1) + ": ", end="")
    for i in num:
        print(str(i)*num[i], end="")

    print("")
            
