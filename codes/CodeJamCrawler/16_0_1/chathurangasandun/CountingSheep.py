def sleepNumber(N):
    list = [i for i in range(0,10)]
    N = int(N)
    k = 1
    while (list != []):
        if(N == 0):
            return "INSOMNIA"
        number = N*k
        for i in str(number):
            if(list.count(int(i)) > 0):
                list.remove(int(i))
        k += 1
    return (N*(k-1))

T = int(input())


for i in range(T):
    N = input()
    print("Case #"+str(i+1)+": " +str(sleepNumber(N)))




