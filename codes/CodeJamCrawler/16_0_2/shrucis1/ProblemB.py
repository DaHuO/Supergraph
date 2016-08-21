#import heapq

global solved
solved = {}

def doflip(seq,n):
    flipped = ['-' if a=='+' else '+' for a in reversed([seq[x] for x in range(n)])]
    return [flipped[i] if i<n else seq[i] for i in range(len(seq))]

def simplify(seq):
    while(seq[-1] == "+"):
        seq.pop(-1)

#holycrap this is basically dijkstra/bfs
        
def minflips(seq):
    global solved
    if "-" not in seq:
        return 0
    simplify(seq)
    alreadyreached = [seq]
    possibilities = [(0,seq)] # a
    #heapq.heappush(possibilities, (0,seq,
    while(len(possibilities)>0):
        #print("possibilities: " + str(possibilities))
        curposs = possibilities.pop(0)
        #print(curposs)
        newpos = None
        for i in range(len(curposs[1])):
            newposs = doflip(curposs[1],i+1)
            #print("newposs=" + str(newposs))
            if("-" not in newposs):
                return curposs[0]+1
            simplify(newposs)
            if(newposs not in alreadyreached):
                possibilities.append((curposs[0]+1,newposs))
                alreadyreached.append(newposs)
    #print(seq)

f = open(r"C:\Users\Neil\Documents\Coding Competitions\Codejam 2016\B-small-attempt1.in")
s = f.read().split("\n")
f.close()
t = int(s[0])
print(s)
for j in range(t):
#while True:
    print("Case #" + (str(j+1)) + ": " + str(minflips(list(s[1+j]))))
    #s = input("> ")
    #print(minflips(list(s)))
