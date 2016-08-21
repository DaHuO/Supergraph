fo=open("large.in","r+")
foo=open("output_large.txt","wb")
t=int(fo.readline())
for i in range(t):
    n=int(fo.readline())
    digits={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    curr_digit=0
    if n==0:
        ans='case #'+str(i+1)+': INSOMNIA\n'
        foo.write(ans)
    else:
        
        i1=1
        num=0
        while 1:
            num=n*i1
            num1=num
            while num1>0:
                d=num1%10
                num1=num1//10
                digits[d]+=1
            count=0
            for val in digits:
                if(digits[val]>0):
                    count+=1
            if count==10:
                break
            i1+=1
        ans='case #'+str(i+1)+': '+str(num)+'\n'
        foo.write(ans)
