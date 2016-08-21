input=open("input.txt","r")
output=open("output.txt","w")
digits_list=[]
T = int(input.readline())
for cases in range(1,T+1):
    digits_list=[]
    coef=1
    N=int(input.readline())
    number=0
    if N==0:output.write("Case #"+str(cases)+": INSOMNIA\n")
    else:
        while len(digits_list)<10:
            number=coef*N
            for digit in str(number):
                if digit not in digits_list:digits_list.append(digit)
            coef=coef+1
        output.write("Case #"+str(cases)+": "+str(number)+"\n")
    print str(cases)+" "+str(number)
