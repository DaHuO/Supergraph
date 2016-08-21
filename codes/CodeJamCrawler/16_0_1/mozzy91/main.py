###    Google Jam Code - Qualification Round 2016
###    Problem A


#----------------------------------------------------------------------------------------
#--------------------------------      IMPORT     ---------------------------------------
#----------------------------------------------------------------------------------------
import re


#----------------------------------------------------------------------------------------
#-----------------------------     GLOBAL VARIABLES    ----------------------------------
#----------------------------------------------------------------------------------------
INPUT_FILE = "A-large.in"

LINES = []
CASES = []
OUTPUT = []
PATTERN = list(range(10))


#----------------------------------------------------------------------------------------
#--------------------------------     FUNCTIONS    --------------------------------------
#----------------------------------------------------------------------------------------

def find_digits(N):
    
    FOUND = []
    
    for i in range(len(PATTERN)):
    
        if re.search(str(PATTERN[i]), str(N)):
            FOUND.append(i)

    for k in reversed(FOUND):
    
        del PATTERN[k]
    
    if not PATTERN:
        return True
    
    else:
        return False
    





#----------------------------------------------------------------------------------------
#--------------------------------     MAIN BODY    --------------------------------------
#----------------------------------------------------------------------------------------

try:
    file = open(INPUT_FILE, "r")
    print("File open properly.\n")
except:
    print("File not found!\n Now exit.")
     
LINES.append(file.readline())

T = int(LINES[0])

print("T = ", T)

for i in range(T):
    LINES.append(file.readline())
    CASES.append(int(LINES[i+1]))

file.close()
del file

print(CASES)

for case in CASES:
    i = 2
    N = case
    
    if N != 0:
        while(not find_digits(N)):
            N = case*i
            i = i+1
    
        PATTERN = list(range(10))        
        
    else:
        N = "INSOMNIA" 
    
    OUTPUT.append(str(N))

file = open("output.out", 'w')
file.close()
file = open("output.out", 'a')

for i in range(len(OUTPUT)):
    file.write("Case #{}: {}\n".format(i+1, OUTPUT[i]))
    print("Case #{}: {}".format(i+1, OUTPUT[i]))

file.close()

