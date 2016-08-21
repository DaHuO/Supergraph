one={'O':1,'N':1,'E':1}
two={"T":1,"W":1,"O":1}
three={"T":1,"H":1,"R":1,"E":2}
four={"F":1,"O":1,"U":1,"R":1}
five={"F":1,"I":1,"V":1,"E":1}
six={"S":1,"I":1,"X":1}
seven={"S":1,"E":2,"V":1,"N":1}
eight={"E":1,"I":1,"G":1,"H":1,"T":1}
nine={"N":2,"I":1,"E":1}
zero={"Z":1,"E":1,"R":1,"O":1}
lst=[zero,one,two,three,four,five,six,seven,eight,nine,zero]
alpha={}
for i in lst:
    for j in i:
        if j not in alpha:
            alpha[j]=1
##fin={}
##huge={}
##def count(s):
##    dic={}
##    for i in s:
##        nu=lst[int(i)]
##        for w in nu:
##            if w in dic:
##                dic[w]+=nu[w]
##            else:
##                dic[w]=nu[w]
##    return(dic)
##
##for i in range(1000000):
##    num=[]
##    for j in str(i):
##        num.append(int(j))
##        num.sort()
##    s=''
##    for j in num:
##        s+=str(j)
##    if s in fin:
##        pass
##    else:
##        fin[s]=1
##        huge[s]=count(s)

def sub(dic1,dic2,x):
    for i in dic2:
        dic1[i]-=dic2[i]*x

file=open("A-large.in")
k=file.readline()
a=int(k[:-1])
w=open("output.txt","w")
for num in range(a):
    k=file.readline()[:-1]
    dic={}
    for i in k:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in alpha:
        if i not in dic:
            dic[i]=0
    lst=[]
    lst+=[6]*dic["X"]
    sub(dic,six,dic["X"])
    lst+=[0]*dic["Z"]
    sub(dic,zero,dic["Z"])
    lst+=[7]*dic["S"]
    sub(dic,seven,dic["S"])
    lst+=[5]*dic["V"]
    sub(dic,five,dic["V"])
    lst+=[4]*dic["F"]
    sub(dic,four,dic["F"])
    lst+=[8]*dic["G"]
    sub(dic,eight,dic["G"])
    lst+=[3]*dic["H"]
    sub(dic,three,dic["H"])
    lst+=[2]*dic["W"]
    sub(dic,two,dic["W"])
    lst+=[9]*dic["I"]
    sub(dic,nine,dic["I"])
    lst+=[1]*dic["O"]
    sub(dic,one,dic["O"])
    lst.sort()
    s=""
    for i in lst:
        s+=str(i)
    s="case #"+str(num+1)+": "+str(s)+"\n"
    w.write(s)
    print(s)
w.close()
            

            



