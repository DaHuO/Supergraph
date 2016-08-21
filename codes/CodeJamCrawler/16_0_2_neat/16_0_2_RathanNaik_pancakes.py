'''

Input           Output 
5               
-               Case #1: 1
-+              Case #2: 1
+-              Case #3: 2
+++             Case #4: 0
--+-            Case #5: 3

'''

test = eval(input())
ans = []                        #Answer List 
for i in range(test):
    inp = input()
    cakes = list(inp)           #Initial Pancakes stack taken as input
    count=0;                    #Count number of flips for current test case
    
    '''
    Start from the top of stack
    if any pancake is not following some order as above it (order can be + or -)
        Reverse all pancakes above it, to match the current pancake 
    '''
    for i in range(len(cakes)-1):
        if(cakes[i] != cakes[i+1]):
            count += 1
            for j in range(i+1):
                cakes[j]=cakes[i+1]
    if(cakes[0]=="-"):
        count+=1            
    ans.append(count)

count = 1;    
for i in ans:
    print("Case #",count,": ",i,sep="")
    count += 1

