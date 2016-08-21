lst = list()

def isPrime(n):
    global lst
    for i in range(3,500):
        if n%i == 0:
            lst.append(i)
            return False
    return True


for T in range(int(input())):

    print("Case #" +str(T+1)+ ":")
    N,J = map(int,input().split())
    countJ = 0
    start = int("1" + "0"*(N-2) + "1",2)
    end = int("1" + "0"*N , 2)
    for n in range(start,end,2):
        lst = []
        flag = True
        bn = bin(n)[2:]
        for base in range(2,11):
            if isPrime(int(bn,base)):
                flag = False
                break
        if flag is True:
            s = ""
            for i in lst:
                s += " " + str(i)
            s = str(bn) + s
            print(s)
            countJ += 1
            if countJ == J:
                break









