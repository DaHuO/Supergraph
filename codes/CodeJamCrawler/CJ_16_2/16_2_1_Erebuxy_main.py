num = int(raw_input())
for i in range(1,num+1):
    n = raw_input()
    print "Case #"+str(i)+":",
    num = [0 for j in range(10)]
    dic = {'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'N':0, 'O':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Z':0}
    for j in n:
        dic[j] += 1
    num[0] = dic['Z']
    num[2] = dic['W']
    num[6] = dic['X']
    for j in "ZERO":
        dic[j] -= num[0]
    for j in "TWO":
        dic[j] -= num[2]
    for j in "SIX":
        dic[j] -= num[6]
    num[7] = dic['S']
    for j in "SEVEN":
        dic[j] -= num[7]
    num[5] = dic['V']
    for j in "FIVE":
        dic[j] -= num[5]
    num[4] = dic['F']
    for j in "FOUR":
        dic[j] -= num[4]
    num[3] = dic['R']
    for j in "THREE":
        dic[j] -= num[3]
    num[8] = dic['H']
    for j in "EIGHT":
        dic[j] -= num[8]
    num[1] = dic['O']
    for j in "ONE":
        dic[j] -= num[1]
    num[9] = dic['I']
    for j in "NINE":
        dic[j] -= num[9]    
    ans = ""
    for j in range(10):
        if num[j] > 0:
            ans += str(j) * num[j]
    print ans