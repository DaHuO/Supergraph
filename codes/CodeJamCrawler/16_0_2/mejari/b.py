def flip(pancakes, n):
    for e in range(n):
        pancakes[e] *= -1
    return pancakes

def findN(pancakes):
    if(pancakes[0] == 1):
        for i in range(len(pancakes)):
            if(pancakes[i] == -1):
                return i
        return None
    else:
        for i in range(len(pancakes)):
            if(pancakes[i] == 1):
                return i
        return i+1
                




f = open("B-large.in", "r")

T = int(f.readline())
for t in range(T):
    plusMinus = f.readline()
    pancakes = []
    for e in plusMinus:
        if(e == '+'):
            pancakes.append(1)
        if(e == '-'):
            pancakes.append(-1)
            
    total = 0
    n = findN(pancakes)
    while(n != None):
        pancakes = flip(pancakes, n)
        total += 1
        n = findN(pancakes)
    print("Case #" + str(t+1) + ": " + str(total))
        
