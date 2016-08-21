
T = int(input())
for i in range(T):
    N = int(input())
    if(N==0):
        print("Case #",i+1,": INSOMNIA",sep = '')
        continue
    global_temp = 0
    list_of_No = [0,1,2,3,4,5,6,7,8,9]
    mult = 1
    while list_of_No!=[]:
##        print("list not empty loop")
        number = N*mult
        mult = mult+1
        global_temp = number
        while int(number):
##            print("disintegration")
            flag = True
            digit = int(number%10)
            try:
                list_of_No.index(digit)
            except:
                flag = False
            if flag == True:
                list_of_No.remove(digit)
            number = number/10
    print("Case #",i+1,": ",global_temp,sep = '')
