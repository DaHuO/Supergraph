''' 
QUESTION:
Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. 
First, she picks a number N. 
Then she starts naming N, 2 × N, 3 × N, and so on. 
Whenever she names a number, she thinks about all of the digits in that number.She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as part of any number she has named. 
Once she has seen each of the ten digits at least once, she will fall asleep.
'''

test = eval(input())
ans = []                    #List which holds answers for all the test cases
digits = set()
for i in range(test):   
    flag=True               #To ensure that we have not seen all ten digits yet
    multi=2
    
    inp = input()
    
    #Make multiple copes so that we do not change original input,Just for safety!
    inp2=int(inp);          
    inp3=int(inp);
    
    #If number is Zero Stop execution of current test case
    if(inp2==0):
        ans.append("INSOMNIA")
        continue
    
    #Put all digits in N to the set    
    for i in inp:
        digits.add(i);
        if(len(digits)==10):
            flag=False
            
    while(flag):
        inp2 = multi*inp3
        strinp2=str(inp2)       #Convert to string as digits set is in string
        
        #Add all the digits in the new multiple
        for i in strinp2:
            digits.add(i);
            if(len(digits)==10):
                flag=False
                
        multi += 1
        
        
    if(not flag):
        ans.append(inp2)
        digits.clear()         #Clear the set inorder to start fresh for new test case

case = 1;
for i in ans:
    print("Case #",case,":"," ",i,sep="")
    case += 1
