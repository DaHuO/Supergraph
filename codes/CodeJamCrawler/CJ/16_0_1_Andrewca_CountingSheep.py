'''
Created on 08.04.2016

@author: Chris Andrews    
'''
import math

def getDigits(num):
    digits = [False,False,False,False,False,False,False,False,False,False,False]
#     print("Log: " + str(int(math.floor(math.log(num,10)))))
    if int(math.floor(math.log(num,10))) > 0:
        for i in range(0,int(math.floor(math.log(num,10))+1)):
#             print("Num1: " + str(num))
#             print("i: " + str(i))
#             print("10^i: " + str(math.pow(10, i+1)))
            digit = num%math.pow(10,i+1)
#             print("Digit1: " + str(digit))
            num -= digit
#             print("Num2: " + str(num))
            digit = digit/math.pow(10, i)
#             print("Digit2: " + str(digit))
#             print("True digit set: " + str(digit))
            digits[int(digit)] = True
    else:
#         print("True digit set: " + str(num))
        digits[int(num)] = True
    return digits

def countSheep(N):
    results = [False,False,False,False,False,False,False,False,False,False,False]
    resultsTrue = 0
    if N==0:
        return None
    else:
        i = 1
        while resultsTrue < 10:
#             print("index: " + str(i))
            digits = getDigits(i * N)
#             print("Digit return: " + str(digits))
            for index in range(len(digits)):
                if digits[index]:
                    results[index] = True
            resultsTrue = 0
            for result in results:
                if result:
                    resultsTrue += 1
#                     print("True: " + str(resultsTrue))  
            i += 1               
        return i-1
        
def fileToStruct(fileName):
    f = open(fileName)
    for line in f:
        line = int(float(line))
        if countSheep(line):
            line = countSheep(line) * line
        print(line)
    f.close()
    return 

# fileToStruct("C:\\Users\\Andrews\\Documents\\numbers.txt")

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    line = int(raw_input())  
    N = countSheep(line)
    if N:
        line = "Case #" + str(i)+ ":\t" + str(N * line)
    else:
        line = "Case #" + str(i)+ ":\tINSOMNIA"
    print(line)
    
    
    
    
    
