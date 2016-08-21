input=open("B-large.in","r")
output=open("PBlarge.txt","w")

T = int(input.readline())

def flip(s,index):
    for loop in range(index,-1,-1):
        if s[loop] == '-':
            s[loop] = '+'
        else:
            s[loop] = '-'
    return s

def search(s):
    for loop in range(len(s)-1,-1,-1):
        if s[loop] == '-':
            return loop
    return 0

for loop in range(T):
    s = list(input.readline())
    
    nb = 0
    i = len(s)
    
    while i != 0:
        for j in range(i-1,-1,-1):
            if s[j] == '-':
                s = flip(s,j)
                nb += 1
        i = search(s)
        
    output.write("Case #{}: {}\n".format(loop+1,nb))

input.close()
output.close()