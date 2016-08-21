###    Google Jam Code - Qualification Round 2016
###    Problem B

#----------------------------------------------------------------------------------------
#--------------------------------      IMPORT     ---------------------------------------
#----------------------------------------------------------------------------------------
import re
import itertools as I

#----------------------------------------------------------------------------------------
#-----------------------------     GLOBAL VARIABLES    ----------------------------------
#----------------------------------------------------------------------------------------
INPUT_FILE = "B-large.in"

pattern = r'^[+]*$'

LINES = []
CASES = []
OUTPUT = []

#----------------------------------------------------------------------------------------
#--------------------------------     FUNCTIONS    --------------------------------------
#----------------------------------------------------------------------------------------

def parseline(file):
    return file.readline().split()


def change_side(group):
    
    if '-' in group:
        temp = group.replace('-', '+')
    else:
        temp = group.replace('+', '-')
    
    return temp 

def reorder_pancakes(stack):
    mnvr = 0
    
    for i in I.count(0,1):   
        temp = ""
             
        if i == len(stack)-1:
            if not re.search(pattern, stack):
                temp = change_side(stack)
                mnvr += 1
                stack = temp
            
            #print(stack)
       
        elif stack[i] != stack[i+1]:
            temp += change_side(stack[:i+1])
            temp += stack[i+1:]
            stack = temp
            mnvr += 1

            
            #print(stack)
            
        if re.search(pattern, stack):
                print("\nReorder finshed!\nManeuvers: {}\n".format(i))
                return mnvr



#----------------------------------------------------------------------------------------
#--------------------------------     MAIN BODY    --------------------------------------
#----------------------------------------------------------------------------------------

try:
    file = open(INPUT_FILE, "r")
    print("File was open properly!\n")
except:
    print("File not found.\n\nExit now.")
    
LINES.append(file.readline())

T = int(LINES[0])

print("T = {}\n".format(T))

for i in range(T):
    LINES.append(file.readline())
    CASES.append(LINES[i+1].strip())

#print(CASES)

for i in range(len(CASES)):
    OUTPUT.append(reorder_pancakes(CASES[i]))
    
#print(OUTPUT)

file = open("output.out", 'w')
file.close()
file = open("output.out", 'a')

for i in range(len(OUTPUT)):
    file.write("Case #{}: {}\n".format(i+1, OUTPUT[i]))
    print("Case #{}: {}".format(i+1, OUTPUT[i]))

file.close()





