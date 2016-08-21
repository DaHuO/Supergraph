
# coding: utf-8

# In[ ]:

t = int(raw_input())
for case in range(1,t+1):
    n = int(raw_input())
    if n==0:
        solution = "INSOMNIA"
    else:
        i = 0
        seen = [0]*10
        num_seen = 0
        while num_seen !=10:
            i += 1
            value = i*n
            while value:
                digit = value%10
                value = value//10
                if not seen[digit]:
                    seen[digit] = 1
                    num_seen += 1
        solution = i*n
    
    print "Case #{}: {}".format(case,solution)

