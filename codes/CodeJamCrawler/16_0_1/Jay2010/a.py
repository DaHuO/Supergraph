in_file= open("a.in", "r")
in_file2= open("a.out", "w")
in_data= in_file.readline()
for j in range(int(in_data)):
    number1=int(in_file.readline())
    digits=['0','1','2','3','4', '5', '6', '7', '8', '9']

    number=number1
    if(number==0):
            in_file2.write("Case #"+str(j+1)+": "+"INSOMNIA"+"\n")
    else:
        cnt=0
        while(digits!=[]):
                cnt=cnt+1
                number=number1*cnt
                strnumber=str(number)
                i=0
                while(i<len(digits)):
                    if digits[i] in strnumber:
                        digits.remove(digits[i])
                        i=i-1
                    i=i+1
                print(number)
                print(digits)
        
        in_file2.write("Case #"+str(j+1)+": "+str(number)+"\n")
in_file.close()
in_file2.close()