N = eval(input())
seq = ["W","U","F","G","H","Z","X","V","O","I"]
num = [2,4,5,8,3,0,6,7,1,9]
tel = [0,0,0,0,0,0,0,0,0,0]
for t in range(1,N+1):
    S = input()
    strlist = list(S)
    for i in range(10):
        n = strlist.count(seq[i])
        tel[num[i]] = n
    tel[5] -= tel[4]
    tel[3] -= tel[8]
    tel[7] -= tel[5]
    tel[1] -= (tel[2] + tel[4] + tel[0])
    tel[9] -= (tel[5] + tel[8] + tel[6])
    print("Case #{}: ".format(t), end="")
    for i in range(10):
        print(str(i)*tel[i],end="")
    print()
    
