from itertools import product
from math import sqrt

def divisors(n):
    if n % 2 == 0 and n > 2: 
        return [2]
    return [i for i in range(3, int(sqrt(n)) + 1, 2) if not n%i]


def coin_jam(n, jams):
    jammed = []
    s = [''.join(i) for i in product('10', repeat=n-2)]
    for i in s:
        j = "1" + i + "1"
        div = []
        for k in range(2,11):
            val = int(j,k)
            d = divisors(val)
            if d:
                div.append(d[-1])
            else:
                break
        if len(div) == 9:
            jammed.append(j +" "+ " ".join(map(str, div)))
        if len(jammed) == jams:
            return "\n".join(jammed)
            
                 
             
         
        
    

    
n = int(raw_input())
for i in range(n):
    length, jams = map(int, raw_input().split())
    njams = coin_jam(length, jams)
    print "Case #{0}:\n{1}".format(i+1, njams)
    
