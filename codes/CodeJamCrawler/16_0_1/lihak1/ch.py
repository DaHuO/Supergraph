def f(num):
    num1 = num
    if num == 0:
        return 'INSOMNIA'
        return 
    
    lofn = [1,2,3,4,5,6,7,8,9,0]
    while lofn:
        num_str = str(num)
        for char in num_str:
            if char in '0123456789':
                if int(char) in lofn:
                    lofn.remove(int(char))
        
        num += num1
    return num-num1
                

t= int(raw_input())
for i in range(t):
   print "Case #"+str(i+1)+": "+str(f(int(raw_input())))
