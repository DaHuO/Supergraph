
def get_max_party(P):
    n = 0
    senators = 0
    for i in range(len(P)):
        if (P[i] > senators):
            senators = P[i]
            n = i
    return n

def get_party_carried(P, n):
    P1 = P
    if (P1[n] > 0):
        P1[n] = P1[n] - 1
    return P1

def get_party_rollback(P, n):
    P[n] = P[n] + 1
    return P

def get_party_num(P):
    n = 0
    for p in P:
        if (p > 0):
            n = n + 1
    return n

def is_more_half(P):
    half = int(sum(P) / 2)
    for p in P:
        if p > half:
            return True
    return False    

def get_party_sym(i):
    return chr(ord('A') + i)
    
def solve(N, P):
    instructions = ""
    n = N
    Parties = P
    while (sum(Parties) != 0):
        if (get_party_num(Parties) == 2) and (sum(Parties) % 2 == 0):
            for k in range(2):
                i = get_max_party(Parties)
                P1 = get_party_carried(P, i)
                instructions += get_party_sym(i)                
                Parties = P1
                #if (is_more_half(P1)):
                #    print("is_more_half: {}".format(P1))
            
        else:
            for k in range(2):                
                #print("  Parties:{}".format(Parties))
                i = get_max_party(Parties)
                #print("  i={}".format(i))
                P1 = get_party_carried(Parties, i)
                if (not is_more_half(P1)):
                    #print("  sym:{}".format(get_party_sym(i)))
                    instructions += get_party_sym(i)
                    Parties = P1
                else:
                    Parties = get_party_rollback(Parties, i)
                    
        instructions += ' '
        #print("*Parties:{}".format(Parties))
        #print("*instructions:{}".format(instructions))

    
    return instructions
 
    
if __name__ == "__main__":
    t = int(input()) 
    for i in range(1, t + 1):        
        N = int(input())
        P = [int(s) for s in input().split(" ")]
        print("Case #{}: {}".format(i, solve(N, P)))
        
