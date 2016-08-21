f_in=open("1.in")
f_out=open("output.txt",'w')
input=int(f_in.readline())
def modify_list(list1):
    for i in range(len(list1)-1,-1,-1):
        if(list1[i]=='-'):
            return list1[:i+1]
    
    return list1[:i]
        

for k in range(input):
    list1=str(f_in.readline())
    list1=modify_list(list1)
    inversion=0
    for i,j in zip(list1,list1[1:]):
        if(i!=j):
            inversion=inversion+1
    if list1:
        inversion= inversion+1 

    f_out.write("Case #"+str(k+1)+': '+ str(inversion)+"\n")
            
            
f_out.close()
