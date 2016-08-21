'''
@author: Kamil
'''

def task1(number):
    if number == 0:
        return "INSOMNIA"
    digits = set()
    j = 1    
    x = number
    while True:
        x = number*j
        digitsStr = str(x)
        for d in digitsStr:
            digits.add(d)
        if len(digits) == 10:
            break
        j = j + 1
    return x
            
 
f = open('output.txt','w')
 
with open('A-large.in') as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        n = int(lines[i])
        print("Case #" + str(i) + ": " + str(task1(n)))
#         print("Case #" + str(i) + ": " + task1(n), file = f)
         

            
    