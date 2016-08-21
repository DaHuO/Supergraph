#!/usr/bin/python3

testNb = int(input())
for test in range(1,testNb+1) :
    time = 0
    smile = False
    begin = True
    stackPancake = [ i for i in input()]    

    if stackPancake[0] == '+' :
        smile = True
    else :
        smile = False

    for i in stackPancake[1:] :       
        if smile == True and begin == True and i == '-' :
            begin = False
            smile = False
            time += 2
        elif smile == False and begin == True and i == '+' :
            begin = False
            smile = True 
            time += 1
        elif not begin :      
            if smile == True and i == '-' :
                smile = False
                time += 2
            elif  i == '+' :
                smile = True
    
    if begin and not smile :
        print("Case #" + str(test) + ": " + str(1))
    else :
        print("Case #" + str(test) + ": " + str(time))
