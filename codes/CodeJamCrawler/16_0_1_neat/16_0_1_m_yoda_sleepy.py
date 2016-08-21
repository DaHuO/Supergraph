def sleepy(lis, tc):
    output = []
    for k in lis:
        digits = []
        i = 2
        x = k
        
        if(k == 0):
            output.append('INSOMNIA')
            
            
        while(k!=0):
            num_str = str(k)
            len_num = len(num_str)
            for j in range(len_num):
                digit = num_str[j:j+1]
                #print(digit)
                if digit not in digits:
                    digits.append(digit)
            #print(digits)
            if(len(digits)==10):
                output.append(str(k))
                break
            k = x * i
            
            i += 1
    return output        

tc = int(input())
lis = []
for i in range(tc):
    num = int(input())
    lis.append(num)
#print(lis)    
asas = sleepy(lis,i)
for i in range(len(asas)):
    print("Case #%s:" %(i+1),end=" ")
    print(asas[i])
    
