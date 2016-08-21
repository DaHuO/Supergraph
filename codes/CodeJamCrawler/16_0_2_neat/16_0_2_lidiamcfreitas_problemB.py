def solve(teste):
    flips = 0
    
    begin = 0               # points to first char on the left
    end   = len(teste) - 1 
    
    current_symbol = teste[0]
    
    # remove +s to the right
    while (end != -1 and teste[end] == '+'): 
        end -= 1
    if end == -1:
        return 0
    
    end += 1 # represents end of string
    

    for i in range(0,end):
        if teste[i] != current_symbol:
            flips += 1
            if current_symbol == '+':
                current_symbol = '-'
            else:
                current_symbol = '+'
                
    if current_symbol == '+':
        print( "is this possible?", teste)
        return flips
    else:
        return flips + 1
    

t = int(input())

for i in range(1, t + 1):
    n = str(input())
    res = solve(n)
    print("Case #{}: {}".format(i, res))