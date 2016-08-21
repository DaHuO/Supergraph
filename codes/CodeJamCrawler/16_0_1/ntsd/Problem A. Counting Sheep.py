
def check_digit(num2):
    global digit
    lis = []
    strnum = str(num2)
    for i in strnum:
        if int(i) not in digit:
            digit += [int(i)]
            #print(lis)

def count_sheep(num):
    i = 1
    global digit
    digit = []
    if num == 0:
        return "INSOMNIA"
    while 1:
        check_digit(num*i)
        #print(digit)
        if sorted(digit) == [0,1,2,3,4,5,6,7,8,9]:
            return num*i
        i+=1
    
    
for i in range(int(input())):
    print("Case #"+str(i+1)+": "+str(count_sheep(int(input()))))
