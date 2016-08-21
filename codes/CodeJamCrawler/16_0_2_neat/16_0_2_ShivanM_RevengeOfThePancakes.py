infile = open("B-large.in", "r")
outfile = open("B-large.out", "w")

def flipit(list, i):
    stack = list[i:]
    splice = list[:i]
    for looper in range(len(splice)):
        if (splice[looper] == '+'):
            splice = splice[:looper] + '-' + splice[looper+1:]
        elif (splice[looper] == '-'):
            splice = splice[:looper] + '+' + splice[looper+1:]
    return  splice[::-1] + stack 

T = int(infile.readline())
print T
S = []

for case in range(T):
    S.append(infile.readline().strip("\n"))
    


for case in range(T):
    allplus = False
    tries = 0
    
    while(allplus == False):
        for letter in range(len(S[case])):
            
            
            if (S[case][letter - 1] != S[case][letter] and letter != 0):
                S[case] = flipit(S[case],letter  )
                tries += 1
                
                continue
            if(letter + 1 == len(S[case])):
                if(S[case][letter] == "-"):
                    S[case] = flipit(S[case],letter + 1 )
                    tries += 1
                    
                else:
                    allplus = True
                    continue
 
    S[case] = str(tries)
for case in range(T):
    outfile.write("Case #" + str(case + 1) + ": " + S[case] + "\n")
infile.close()
outfile.close()
