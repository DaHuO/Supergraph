num=int(input())
y=num
n=[]
output_text= open("output3.txt","w")
while num!=0:
    n.append(int(input()))
    num=num-1
while num<y:
    a=[int(x) for x in str(n[num])]
    a=list(set(a))
    i=2
    n1=n[num]
    while len(a)<10 and n[num]!=0:
        n[num]=n1*i
        i=i+1
        b=[int(x) for x in str(n[num])]
        a=a+list(set(b)-set(a))
    if n[num]==0:
        s= "Case #" + str(num+1) + ": INSOMNIA"
        output_text.writelines(s)
        output_text.writelines("\n")
    else:
        s= "Case #" + str(num+1) + ": "+str(n[num])
        output_text.writelines(s)
        output_text.writelines("\n")
    num=num+1
output_text.close()
