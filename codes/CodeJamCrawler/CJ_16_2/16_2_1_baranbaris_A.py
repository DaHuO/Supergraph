import copy
dict = {0:[14,0,7,6],1:[0,5,6],2:[9,13,6],3:[9,3,7,0,0],4:[1,6,10,7],5:[1,4,12,0],6:[8,4,11],7:[8,0,12,0,5],8:[0,4,3,2,9],9:[5,4,5,0]}

dict2 = {'E':0,'F':1,'G':2,'H':3,'I':4,'N':5,'O':6,'R':7,'S':8,'T':9,'U':10,'X':11,'V':12,'W':13,'Z':14}


def solver(inp,start,result,total):
    
    if start > 9:
        return []
    temp = copy.copy(inp)

    contains = 1

    for i in dict[start]:
        if temp[i] > 0:
            temp[i] = temp[i] - 1
    
        else:
            contains = 0
            break
    left = total-len(dict[start])
    
    if left == 0 and contains == 1:
        return result+[start]
    elif left > 0 and start == 9 and contains == 0:
        
        return []

    if contains == 1:
        
        return solver(temp,start,result+[start],left) + solver(temp,start+1,result+[start],left)+ solver(inp,start+1,result,total)
    else:
        return solver(inp,start+1,result,total) # +solver(temp,start,result+[start],left)+solver(temp,start+1,result+[start],left)

t = int(input())
for i in xrange(t):

    str_ = raw_input()

    inp = [0]*15
    for j in str_:
    
        inp[dict2[j]] = inp[dict2[j]] + 1
    result = solver(inp,0,[],len(str_))
    str_result = "Case #"
    str_result = str_result + str(i+1)
    str_result = str_result + ": "
    tt = 0
    for j in result:
        if tt >= len(str_):
            break
        tt = tt+len(dict[j])
        str_result = str_result + str(j)
    print str_result






