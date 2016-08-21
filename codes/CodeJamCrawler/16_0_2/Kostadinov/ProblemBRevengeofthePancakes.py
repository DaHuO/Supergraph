def flip(pans, unhappy):
    
    upper = pans[0:unhappy+1]
    down = pans[unhappy+1: len(pans)]
    
    upper = [not p for p in list(reversed(upper))]
    
    return upper + down

def last_unhappy(pans):
    
    size = len(pans)
    
    last_unhappy = -1
    
    if len(pans) > 1:
        for i in range(1, size):
            if pans[i-1] != pans[i]:
                return i-1
    
    if pans[size-1] == False: #unhappy
        return size - 1
        
    return last_unhappy

def solve(str_pans):
    # Create pans
    pans = []
    for p in str_pans:
        if p == '+':
            pans.append(True)
        elif p == '-':
            pans.append(False)
            
    
    unhappy = last_unhappy(pans)
    flips = 0
    
    while unhappy >= 0:
        flips += 1
        pans = flip(pans, unhappy)
        unhappy = last_unhappy(pans)

    return str(flips)

# Read file
with open('input.txt') as f:
    content = f.readlines()

f_output = open("output.txt", "wb")
for i in range(1, int(content[0]) +1):
    f_output.write("Case #" + str(i) + ": " +solve(content[i]) + "\r\n");
f_output.close()