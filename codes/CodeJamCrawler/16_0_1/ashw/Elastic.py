def count_sheep(T, N):
    temp = [];
    j=1; 
    if N == 0:
        print 'Case #'+str(T)+': INSOMNIA'
    while N > 0:
        mulVal = j*N
        j = j+1
        string_mulVal = str(mulVal)
        for ch in string_mulVal:
            if int(ch) not in temp:
                temp.extend([int(ch)])

        if len(temp) == 10:
            print 'Case #'+str(T)+': '+string_mulVal
            break        
            
               
t = int(input())
for i in range(1, t + 1):
    count_sheep(i, int(input()))

#count_sheep(0, 1692)