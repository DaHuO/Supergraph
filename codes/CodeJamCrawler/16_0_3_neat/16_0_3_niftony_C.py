

def isPrime(n):
    # possible sets
    sqrt_n=pow(n,0.5)
    for x in xrange(2,int(sqrt_n)+1):
        if n%x==0:
            return (False,x)
    return (True,-1)

def convertInteger(value,base):
    sum=0
    string=str(value)
    for index in xrange(len(string)):
        sum+=int(string[index])*pow(base,len(string)-index-1)
    return sum

file=open("C.in","r")
file_out=open("C.out","wr")

case_n=int(file.readline())

for x in xrange(case_n):
    result=[]
    case_v=file.readline().split(" ")
    length=int(case_v[0])
    target=int(case_v[1])
    count=0
    value=pow(10,length-1)+1
    dif=0
    file_out.writelines("Case #1:\n")
    while count<target:
        if dif==pow(2,length-1)-2:
            print "not enough"
        # convert it to bin then convert it back
        value=int(bin(pow(2,length-1)+1+dif)[2::])

        print value,count
        one_result=[]

        base=2
        # base 2-9
        for base in xrange(2,10):
            decimal=convertInteger(value,base)
            r=isPrime(decimal)
            if r[0]:
                base=10
                continue
            else:
                one_result.append(r[1])
        # base 10
        r=isPrime(value)
        if r[0]:
            dif+=2
            continue
        else:
            one_result.append(r[1])

        if len(one_result)==9:
            result.append(one_result)
            file_out.writelines(str(value))
            for one in one_result:
                file_out.writelines(" "+str(one))
            file_out.writelines("\n")
            count+=1

        # next value
        dif+=2








