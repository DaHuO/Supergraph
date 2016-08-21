import itertools
def coin_jam():
    t = int(raw_input())
    for i in range(1,t+1):
        m = [int(s) for s in raw_input().split(" ")]
        #print m
        jams = list(itertools.product([0, 1], repeat=(m[0]-2)))
        #print type(jams)
        jams = [ [1] + list(item) + [1] for item in jams]
        index = 0
        coins = []
        #print m[1]
        while(len(coins) != m[1]):
        #while(index<len(jams)):
            #print type(jams[index])
            byte = ''.join(str(e) for e in jams[index])
            bases = []
            #print byte
            for z in range(2,11):
               # print byte,z
                bases.append(int(byte,z))
            #print bases
            bases = [isPrime(elm) for elm in bases]
            #print bases
            if 0 not in bases:
                coins.append([byte]+bases)
                #coins.extend(bases)
            index+=1
        output = "\n"
        for h in range(m[1]):
            for k in range(10):
                output+= str(coins[h][k]) + " "
            output += "\n"
        #print output
            
        
        print "Case #{}: {}".format(i, output)

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return n/i

    return 0
    
            

coin_jam()
