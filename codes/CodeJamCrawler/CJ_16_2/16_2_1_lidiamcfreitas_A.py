debug = True
numbers = {}

def d(string):
    if(debug):
        print(string)

test_cases = int(input())
result = {}

for test_case in range(test_cases):
    print("Case #{0}: ".format(test_case+1), end="")
    numbers["Z"] = 0
    numbers["E"] = 0
    numbers["W"] = 0
    numbers["R"] = 0
    numbers["F"] = 0
    numbers["V"] = 0
    numbers["X"] = 0
    numbers["S"] = 0
    numbers["G"] = 0
    numbers["I"] = 0    
    S = input()
    
    for i in range(0,10):
        result[i]=0
    
    for char in S:
        if char in numbers:
            numbers[char]+=1
    

    for zeros in range(numbers["Z"]):
        result[0] += 1
        for char in "ZERO":
            if char in numbers:
                numbers[char]-=1
    
    for twos in range(numbers["W"]):
        result[2] += 1
        for char in "TWO":
            if char in numbers:
                numbers[char]-=1        
    
    for sixes in range(numbers["X"]):
        result[6] += 1
        for char in "SIX":
            if char in numbers:
                numbers[char]-=1

    for eights in range(numbers["G"]):
        result[8] += 1
        for char in "EIGHT":
            if char in numbers:
                numbers[char]-=1    


    for sevens in range(numbers["S"]):
        result[7] += 1
        for char in "SEVEN":
            if char in numbers:
                numbers[char]-=1 
                
    for fives in range(numbers["V"]):
        result[5] += 1
        for char in "FIVE":
            if char in numbers:
                numbers[char]-=1  

    for nines in range(numbers["I"]):
        result[9] += 1
        for char in "NINE":
            if char in numbers:
                numbers[char]-=1  
                
    for fours in range(numbers["F"]):
        result[4] += 1
        for char in "FOUR":
            if char in numbers:
                numbers[char]-=1  

    for threes in range(numbers["R"]):
        result[3] += 1
        for char in "THREE":
            if char in numbers:
                numbers[char]-=1  

    for ones in range(numbers["E"]):
        result[1] += 1
        for char in "ONE":
            if char in numbers:
                numbers[char]-=1  
    
    for i in range(0, 10):
        print(str(i)*result[i], end="")
    print()