file = open("c:/CodeJam/problemA/A-large.in")
line = file.next()

## Number of Test Cases:  1<=T<=100
T=int(line)

## Tests each case
for testcase in range(T):
    Case = file.next().split()
    N=Case[0]
    CountingSheep=1
    SheepCount=1
    SleepIndex=[1]*10

    if int(N)==0:
        print('Case #{}: {}'.format(testcase+1,'INSOMNIA'))

    else:
        M=N
        while (CountingSheep==1):
            for each in M:
                SleepIndex[int(each)]=0
                if sum(SleepIndex)==0:
                    CountingSheep=0
                    break

            SheepCount+=1
            LastM=M
            M=str(int(N)*SheepCount)
            ##print(M)
            
             
        
        print('Case #{}: {}'.format(testcase+1,LastM))
           
        
        
        
    

    
    

