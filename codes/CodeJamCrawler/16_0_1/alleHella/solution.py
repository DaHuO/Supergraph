def Appeared(listA):
   for i in listA:
       if i == 10:
           return True
   return False

T = input()
for i in range (int(T)):
    N = input()
    N = int(N)
    if(i!=0):
       print()
    checkV = [10,10,10,10,10,10,10,10,10,10]
    if N!=0:
        x = 0
        while(Appeared(checkV)):
            x +=1
            for index in str(N*x):
                checkV[int(index)] = int(index)
                #print(index)
           

        print("Case #" + str(i+1) + ": " + str(N*(x)),end="")
    else:
        print("Case #" + str(i+1) + ": INSOMNIA",end="")


