f1=open("A-large.in","r")
f2=open("a.out", "w")
a1=int(f1.readline())
def check(lst):
    for i in lst:
        if sum(lst)>0:
            if i*1.0/sum(lst)>0.5:
                return 0
    return 1
try:
    for i1 in range(a1):
        lst_len=f1.readline()
        lst=f1.readline()
        lst=lst.split()
        for i2 in range(len(lst)):
            lst[i2]=int(lst[i2])
        print lst
        f2.write("Case #"+str(i1+1)+":")
        while(sum(lst)>0):
            str1=""
            max_ele=max(lst)
            index1=lst.index(max_ele)
            lst[index1]=lst[index1]-1

            str1=str1+chr(ord(str(index1%10))+17+index1/10*10)
            if check(lst):
                    f2.write(" "+str1+" ")
                    continue
            else:
                    if max_ele in lst:
                        index2=lst.index(max_ele)
                    else:
                        max_ele=max(lst)
                        index2=lst.index(max_ele)
                    lst[index2]=lst[index2]-1
                    if check(lst):
                        str1=str1+chr(ord(str(index2%10))+17+index2/10*10)

                        f2.write(" "+str1+" ")
                        continue
        f2.write("\n")


finally:
    f1.close()
    f2.close()
