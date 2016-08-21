
t = 0
for x in range(int(input())):
    s = raw_input()
    array = list(s)
    for i in range(len(array)-1,-1,-1):
        if array[i] == "-":
            for j in range(0,i+1):
                if array[j]=="-": array[j]="+"
                else: array[j] = "-"
            t+=1
    print("Case #%d: %d"%(x+1,t))
    t = 0
