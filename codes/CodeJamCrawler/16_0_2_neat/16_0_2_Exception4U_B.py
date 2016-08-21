def f(a):
    j = 0;
    count = 0
    while(1):
        if a[j]=='-':
             count = count+1
             while(a[j]=='-'):
                j=j+1
                if(j>=len(a)):
                    break
        break
    i=j
    while(i>=j and i <len(a)):
        if a[i]=='-':
            count = count +2
            while(a[i]== '-'):
                i=i+1
                if i >= len(a):
                    break
        else:       
            if a[i]=='+':
                while(a[i]=='+'):
                    i=i+1
                    if i >= len(a):
                        break
    return count

TT = int(input())
for i in range(1,TT+1):
	print "Case #" + str(i) + ":" + " " + str(f(raw_input()))
