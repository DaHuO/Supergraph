def pancakeflip(pancakestack,n):
    topstack=pancakestack[0:n]
    bottomstack=pancakestack[n:len(pancakestack)]

    topstack.reverse()
    for i in range(len(topstack)):
        if topstack[i]=='-':
            topstack[i]='+'
        else:
            topstack[i]='-'
    return topstack+bottomstack

file = open("c:/CodeJam/problemB/B-large.in")
line = file.next()

## Number of Test Cases:  1<=T<=100
T=int(line)

## Tests each case
for testcase in range(T):
    FlipCount=0
    FlippingStatus=1
    
    S = file.next().split()

    Stack=[]
    
    for each in S[0]:
        Stack.append(each)


    while FlippingStatus==1:
        TrimmingStatus=1

        if Stack.count('-')==0:
            break
        else:
            ## Checks and trims bottom (most right) '+' pancakes from stack  

            while TrimmingStatus==1:
                if Stack[-1]=='+':
                    lastremoved=Stack.pop(-1)
                else:
                    TrimmingStatus=0

            ## Finds first '-' pancake

            FlipIndex= Stack.index('-')

            if FlipIndex==0:
                Stack=pancakeflip(Stack,len(Stack))
                FlipCount+=1

            if FlipIndex>0:
                Stack=pancakeflip(Stack,FlipIndex)
                Stack=pancakeflip(Stack,len(Stack))
                FlipCount+=2
      
             
        
    print('Case #{}: {}'.format(testcase+1,FlipCount))
           
        
        
        
    

    
    

