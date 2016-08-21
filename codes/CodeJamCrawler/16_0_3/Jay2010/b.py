def baseconvo(n,b):
    num=0
    mul=1
    while(n!=0):
        num=num+n%10*mul
        n=n//10
        mul=mul*b
    return  num
def reverseconvo(n):
    str1=""
    while(n!=0):
        str1=str(n%2)+str1
        n=n//2
    return str1
def divisor(n):
    for i in range(2, 500):
        if(n%i==0):
            return i
infile= open("C-large.in", "r")
infile2= open("b.out", "w")
for testcase in range(int(infile.readline())):
    line=infile.readline()
    line=line.split()
    for i1 in range(len(line)):
        line[i1]=int(line[i1])
    infile2.write("Case #"+str(testcase+1)+": ")
    cnt=0
    totalnumbers=line[1]
    totallength=line[0]
    templine=""
    for tempnumber in range(0,pow(2,totallength-2)):
        l=[]
        for base in range(2,11):
            number1=pow(2, totallength-1)+1+tempnumber
            tempnumber_string=reverseconvo(tempnumber)
            tempnumber_string="0"*(totallength-2-len(tempnumber_string))+str(tempnumber_string)
            number2=int("1"+tempnumber_string+"1")
            number=baseconvo(number2, base)
            div=divisor(number)
            if(div!=None):
                l.append(div)
            else:
                break
        if len(l)==9:
            cnt=cnt+1
            templine=templine+"\n"+str(number2)
            for i in l:
                templine=templine+" "+str(i)
            if(cnt==totalnumbers):
                break
infile2.write(templine)
# for base in range(2,11):
#     print(baseconvo(100011, base))
infile.close()
infile2.close()
# print(reverseconvo( 470184985873))
# pow(2,12)
#divisor(470184985873)
# print("HI")
# for i in range(2,11):
#     print(baseconvo(100001, i))
#     print(divisor(baseconvo(100001, i)))
