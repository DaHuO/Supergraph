def result(num):
    if num == 0: return "INSOMNIA"
    flag = "0123456789"
    b = 1
    while flag != "":
        strNum = str(b*num)
        i=0
        strLen=len(strNum)
        while i < strLen:
            if flag.find(strNum[i]) != -1:
                flag = flag.replace(strNum[i], "")
            i=i+1
        b = b+1
    return strNum

def counting_sheep():
    f = open("A-large.in", "r")
    N = int(f.readline() )

    i=0
    a = []
    while i < N:
        a.append( int(f.readline()) )
        i = i+1

    f2 = open("output.in","w")
    i=1
    while i <= N:
        r = result(a[i-1])
        f2.write( "Case #" + str(i) + ": " + r +"\n")
        i = i+1

    f2.close()
    f.close()
counting_sheep()