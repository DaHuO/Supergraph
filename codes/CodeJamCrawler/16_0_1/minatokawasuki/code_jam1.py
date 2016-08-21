f =open('out.txt', 'w')
f1=open('A-large.in', 'r')
p=f1.readlines()
L=len(p)
ind=1
while ind<L :
    list1=[0,0,0,0,0,0,0,0,0,0]
    i=2
    flag=0
    n=int(p[ind])
    if n==0:
        f.write("Case #")
        f.write(str(ind))
        f.write(": ")
        f.write("INSOMNIA")
        f.write("\n")
    else:
        num=n
        while flag==0:
            r=str(num)
            for letter in set(r):
                index=int(letter)
                if list1[index]==0:
                    list1[index]=r.count(letter)
            if all(i > 0 for i in list1):
                flag=1
            else:
                num=(i)*n
                i=i+1
        f.write("Case #")
        f.write(str(ind))
        f.write(": ")
        f.write(str(num))
        f.write("\n")
    ind=ind+1        
f.close()
f1.close()
