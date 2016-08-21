def solve(l):
    Name = ['A','B','C','D','E','F','G','H']
    ANS = []
    if len(l) == 1: #listreform
        l = l[0]

    for TestTime in xrange(1000000):
        
        if max(l[1]) == 0:
            break
                
                for j in xrange(2):
                    
                    if max(l[1]) == 0:
                        break
                            
                            for i in xrange(l[0][0]):
                                
                                if l[1][i] == max(l[1]):
                                    ANS.append(Name[i])
                                        l[1][i] -= 1
                                            break
                                                
                                                if sum(l[1]) == l[0][0] - l[0][0]%2:
                                                    break
                                                        
                                                        ANS.append(" ")
                                                            
                                                            
                                                            
                                                            return ''.join(ANS)




rl = lambda: map(int, raw_input().split())

t = int(raw_input())
for case in xrange(t):
    for _ in xrange(1): #Input quantity
        l = [rl() for i in xrange(2)]      #input Lenght
            ans = solve(l)
                print "Case #{}: {}".format(case+1,ans)
