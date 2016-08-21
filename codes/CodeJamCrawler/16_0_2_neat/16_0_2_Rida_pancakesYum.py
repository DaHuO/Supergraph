num=int(input())
a=[]
output_text= open("outputP2.txt","w")
for i in range(num):
    a.append(list(input()))
for j in range(num):
    flip=0
    while len(a[j])!=0:
        y=a[j]
        if all(x==y[0] for x in y) and y[0]=="+":
            break
        else:
            z=len(y)-y[::-1].index("-")
            #b=list(reversed(a[:y]))
            for i in range(z):
                if y[i]=="+":
                    y[i]="-"
                else:
                    y[i]="+"
            flip=flip+1
        
    s= "Case #" +str(j+1)+": "+str(flip)
    output_text.writelines(s)
    output_text.writelines("\n")
output_text.close()
            
