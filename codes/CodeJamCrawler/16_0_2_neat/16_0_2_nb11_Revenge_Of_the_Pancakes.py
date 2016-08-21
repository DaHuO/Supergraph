def rever(list):
    item = list[0]
    l=len(list)-1
    i=0
    while i <= l:
        if list[i] == item:
            i = i+1
        else:
            break
    l=0
    while l<i:
        if list[l] == "+":
            list[l] = "-"
        else:
            list[l] = "+"
        l = l+1

    return list

def result(str):
    stack = []

    i=0
    l = len(str)
    while i < l:
        stack.append(str[i])
        i = i+1

    R = 0
    while stack.count("-") != 0:
        stack = rever(stack)
        R = R+1

    return R


def counting_sheep():
    f = open("B-large.in", "r")
    N = int(f.readline() )

    i=0
    a = []
    while i < N:
        a.append( (f.readline()).replace("\n","") )
        i = i+1

    f2 = open("output.txt","w")
    i=1
    while i <= N:
        r = result(a[i-1])
        f2.write( "Case #" + str(i) + ": " + str(r) +"\n")
        i = i+1

    f2.close()
    f.close()
counting_sheep()