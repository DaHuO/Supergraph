

def flip_top_N_from_pos_Nminus1(a,pos):
    #a = b + c
    
    b = a[:pos+1]
    c = a[pos+1:]
    
    b.reverse()
    b = [x*(-1) for x in b]

    a = b + c
    return a
    
    
    
def return_last_negative_index(a):   
    for i in reversed(range(len(a))):
        if a[i] == -1: return i
    return -1

def top_positive_index(a):
    for i in range(1,len(a)):
        if a[i] == -1: return i-1
        
        

def calculate(input):
    
    a = []
    
    for x in list(str(input)):
        if x == '-': a.append(-1)
        elif x == '+': a.append(1)
    
    iter = 0  
    
    
    
    while(1):
     last_minus = return_last_negative_index(a)
     if last_minus == -1: return iter
     else:
        
        if a[0] == 1:
           first_plus = top_positive_index(a)
           a = flip_top_N_from_pos_Nminus1(a,first_plus)
           iter +=1 
        
       
        a = flip_top_N_from_pos_Nminus1(a,last_minus)    
        iter +=1          
            
        
    
    
    



file = open('B-large.in','r')
total = int(file.readline())
for i in range(1,total+1):
    
    input = file.readline()

    output = calculate(input)

   
    print 'case #%d: %d' % (i,output)
