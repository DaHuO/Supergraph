
def result(str):
    r = ['']
    for i in range(0, len(str)):
        if str[i] >= r[0]:
            r.insert(0,str[i])
        else:
            r.append(str[i])
    return r

T = int(input())
for l in range(1,T+1):
    str = list(input())
    print("Case #",l,": ","".join(result(str)), sep='')
