# -*- coding: utf-8 -*-
with open('config.txt') as f:
    lines = f.read().splitlines()
    
for j in range(int(lines[0])):
    tracker=[0,1,2,3,4,5,6,7,8,9]
    multiplier=1
    a=int(lines[j+1])
    breaker=0
    while len(tracker) !=0:     
        Value_To_Remove_Int=a*multiplier
        Value_To_Remove_Str = str(Value_To_Remove_Int)
        multiplier=multiplier+1
        breaker=breaker+1
        for each_digit_str in Value_To_Remove_Str:
            if int(each_digit_str) in tracker:    
                tracker.remove(int(each_digit_str))
        if (((breaker ==9) and (len(tracker) >=9))):
            print "Case #",j+1,": " , "INSOMNIA"
            break
    else:
        print "Case #",j+1,":" , Value_To_Remove_Int
               
        
        