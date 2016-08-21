def split(num):
    if(num == 0):
	return "INSOMNIA"
    digits ={}
    count =1
    num_next = num
    while(1):
        count=count+1
        for i in str(num_next):
            digits[i]=i
        if len(digits) == 10:
            return str(num_next)
        else:
            num_next = num*count

TT = int(input())
for i in range(1,TT+1):
	num = int(input())
	print "Case #"+str(i)+":"+" "+split(num)
	
