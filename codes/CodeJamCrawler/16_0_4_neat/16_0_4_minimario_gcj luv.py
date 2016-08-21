for i in range(int(input())):
    a,b,c=map(int,input().split(' '))
    print("Case #"+str(i+1)+": "+' '.join([str(i) for i in range(1, a+1)]))
