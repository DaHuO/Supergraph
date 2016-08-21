

#F = open('A-small-attempt0.in')
#O = open('A-small-attempt0.out','w')

F = open('A-large.in')
O = open('A-large.out','w')


T = int(F.readline())

print T


for case in range(1,T+1):
    string = F.readline().rstrip()

    ans = ''

    for s in string:
        if ans+s > s+ans:
            ans += s
        else:
            ans = s + ans


            

    #print ans



    O.write('Case #%d: %s\n'%(case,ans))
        
        
                
                
        



F.close()
O.close()
    
        
