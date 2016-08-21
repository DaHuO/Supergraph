import fileinput


def solve(S):
    ret=[]
    for i in S:
        if ret and i<ret[0]:
            ret.append(i)
        else:
            ret=[i]+ret
    return ''.join(ret)


a=["CAB","JAM","CODE","ABAAB","CABCBBABC","ABCABCABC","ZXCASDQWE"]

case=1
for line in fileinput.input():
    if not fileinput.isfirstline():
        print("Case #"+str(case)+": "+solve(line).replace('\n',''))
        case+=1

