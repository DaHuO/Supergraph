
def finish():
    flag = 0
    global visited
    for i in range(10):
        if visited[i]==1:
            flag+=1
        else:
            return 0
    if flag == 10:
        return 1


def setnum():
    global visited
    global num1
    for i in range(len(num1)):
        visited[int(num1[i])]=1


n = int(input())
for i in range(1,101):
    num = num1 = list(input())
    visited = []
    for j in range(10):
        visited.append(0)
    setnum()
    k=2
    if int("".join(num)) == 0:
        print("Case #%d: INSOMNIA" %i)
    else:
        while finish() == 0:
            temp = k*int("".join(num))
            # print(temp)
            num1 = list(str(temp))
            setnum()
            k += 1
        if finish() == 1:
            print("Case #%d: %s" %(i,"".join(num1)))






        