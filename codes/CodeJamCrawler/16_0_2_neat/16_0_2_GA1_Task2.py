'''
@author: Kamil
'''

def task2(pancakes):
    pancakes = pancakes[::-1]
    lastIsUp = True
    counter = 0
    for p in pancakes:
        if p == '-' and lastIsUp:
            counter = counter + 1
            lastIsUp = not lastIsUp
        if p == '+' and not lastIsUp:
            counter = counter + 1
            lastIsUp = not lastIsUp
    return counter
        
            
  
f = open('output.txt','w')
  
with open('B-large.in') as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        n = lines[i]
        print("Case #" + str(i) + ": " + str(task2(n)))
#         print("Case #" + str(i) + ": " + task1(n), file = f)
          

            
    