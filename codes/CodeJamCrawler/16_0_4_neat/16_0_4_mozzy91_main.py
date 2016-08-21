###    Google Jam Code - Qualification Round 2016
###    Problem D

#----------------------------------------------------------------------------------------
#--------------------------------      IMPORT     ---------------------------------------
#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------
#-----------------------------     GLOBAL VARIABLES    ----------------------------------
#----------------------------------------------------------------------------------------
INPUT_FILE = "D-small-attempt2.in"

LINES = []
CASES = []
OUTPUT = []

#----------------------------------------------------------------------------------------
#--------------------------------     FUNCTIONS    --------------------------------------
#----------------------------------------------------------------------------------------

def parseline(file):
    return file.readline().split()

def tiles(K, C, S):
    y = []
    
    #if C == 1:
    if S>=K:
        return list(range(1, K+1))
    else:
        y.append("IMPOSSIBLE")

#     elif K==1:
#         y.append('1')
#     
#     elif K==2:
#         y.append('2')
#      
#     else:   
#         temp = list(range(2,(K+1)//2+1))
#         
#         if len(temp) + 1 <= S:
#             y = list(range(2,(K+1)//2+1))
#             y.append(((K+1)//2)+K**2)
#         
#         else:
#             y.append("IMPOSSIBLE")
            
    
    return y



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


print("T = {}".format(T))


for k in range(T):
    TEMP = parseline(file)
    
    K = int(TEMP[0])
    C = int(TEMP[1])
    S = int(TEMP[2])
    
    print(K,C,S)
    
    OUTPUT.append(tiles(K, C, S))


print(OUTPUT)

for i in range(len(OUTPUT)):
    y = ''
    for k in range(len(OUTPUT[i])):
        
        y += str(OUTPUT[i][k]) + ' '
        
    OUTPUT[i] = y

print(OUTPUT)


file = open("output.out", 'w')
file.close()
file = open("output.out", 'a')

for i in range(len(OUTPUT)):
    
    
    file.write("Case #{}: {}\n".format(i+1, OUTPUT[i]))
    print("Case #{}: {}".format(i+1, OUTPUT[i]))

file.close()





