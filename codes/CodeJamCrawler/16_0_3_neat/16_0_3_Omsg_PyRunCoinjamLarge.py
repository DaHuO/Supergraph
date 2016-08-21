import numpy as np

# ---- config ---- #

FileInput="dataCoinjamLarge.in"
FileOutput="dataCoinjamLarge.out"
HighestDivisor=20   #Set highest diversor to be found
MaxOptions=5000     #Set max numbers to be checked for a divisor
AddDigits=10        #Set number of "1" to be added to an option, to make to processing faster

# ---------------- #

def get_list_of_numbers(numberString):
    number=numberString+" "
    numberS=" "
    for i in range(9):
        numb=calc_number(numberString,int(i+2))
        numberS=numberS+" "+str(numb)
        numb=find_divisor(numb)
        number=number+str(numb)
        if i<8:
            number=number+" "
    return number
        
def start(C,J):
    result="\n"
    print "start possible_digits"
    options=possible_digits(C)
    fount_numbers=0
    for o in options:
        numberString=o
        number=get_list_of_numbers(numberString)
        if "fail" not in number:
            result=result+number+"\n"
            fount_numbers=fount_numbers+1
            print "found "+str(number)
        if fount_numbers>=J:
            break
    return result
    
def possible_digits(C):
    C=C-2-AddDigits
    optionAmount=2**(C)
    if optionAmount>MaxOptions:
        optionAmount=MaxOptions
    options=[""]*optionAmount
    print "optionAmount: "+str(optionAmount)
    for j in range(optionAmount):
        options[j]=options[j]+"1"
    for j in range(C):
        for l in range(optionAmount/(j+1)):
            if(l%2==1):
                tile="0"
            else:
                tile="1"
            for m in range(2**j):
                o=l*(2**j)+m
                if o<optionAmount:
                    options[o]=options[o]+(tile)
        print "- "+str(j)
    add_string=""
    for i in range(AddDigits):
        add_string=add_string+"1"
    for j in range(optionAmount):
        options[j]=options[j]+"1"+add_string
    print "optionAmount done"
    return options

def calc_number(numberString,basis):
    numberString=numberString[::-1]
    numberGes=0
    i=0
    for n in numberString:
        numberGes=numberGes+int(n)*basis**i
        i=i+1
    return numberGes

def find_divisor_old(numb):
    for i in range(numb-2):
        calc=float(numb)/float(i+2)
        if calc.is_integer():
            return (i+2)
    return "fail"
    
def find_divisor(numb):
    limit = numb

    if numb == 1:
        return 1

    i=2
    while i < numb:
        if (numb % i == 0):
            limit = numb / i;
            if (limit != i):
                return i;
        i=i+1
        if i>HighestDivisor:
            return "fail";

    return "fail";
    
def file_load():
    check=[]
    with open(FileInput) as f:
        for line in f:
            check.append(line)
    return check

def normal_mode():
    result = get_list_of_numbers("1010101111101111")
    print "------------------------------------"
    print "Result: "+str(result)
    print "------------------------------------"
        #Result 101: 101 fail 2 fail 2 fail 2 5 2 fail
def array_mode():
    f = open(FileOutput, 'w')
    check = file_load()
    print check
    for i in range(np.size(check)):
        if i>0:
            ch=check[i].replace("\n","").split()
            print "C: "+str(ch[0])
            print "J: "+str(ch[1])
            writeString = "Case #"+str(i)+": "+start(int(ch[0]),int(ch[1]))
            f.write(writeString+"\n")
            print writeString
    print "------------------------------------"
    f.close()
                       
if __name__ == "__main__":
    print "------------------------------------"
    print "Start program"
    print "------------------------------------"
    array_mode()