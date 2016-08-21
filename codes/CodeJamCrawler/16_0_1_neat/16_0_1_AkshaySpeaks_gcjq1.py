import math
tests =int(input())
for test in range(tests):
    D={}
    N=int(input())
    flag=0
    i=1
    if N==0:
        print("Case #",test+1,": INSOMNIA",sep='')
        continue
    while flag==0:
        number_string = str((N*i))
        for ch in number_string:
            D[ch]=ch
        if len(D)==10:
            flag=1
        else:
            i=i+1
    print("Case #",test+1,": ",N*(i),sep='')
