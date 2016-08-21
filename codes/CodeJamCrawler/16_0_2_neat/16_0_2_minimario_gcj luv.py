for i in range(int(input())):
    k=input()
    k=k[::-1]
    while len(k)!=0 and k[0]=='+':
        k=k[1:]
    k=k[::-1]
    a=0
    for j in range(len(k)-1):
        if k[j] != k[j+1]:
            a+=1
    print("Case #"+str(i+1)+": ", end = '')
    if k == '':
        print(0)
    else:
        print(a+1)
