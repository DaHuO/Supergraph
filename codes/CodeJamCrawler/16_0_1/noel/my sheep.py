for T in range(int(input())):
    N = int(input())
    st = set()
    num = 0
    if N is 0:
        print( "Case #" + str(T+1) + ": INSOMNIA")
    else:
        while(True):
            num += N
            lst = list(map(int,str(num)))
            for i in lst:
                st.add(i)
            if(len(st) == 10):
                break
        print("Case #" + str(T+1) + ": " + str(num))

