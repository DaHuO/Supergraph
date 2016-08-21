
def flip(n, i):
    bits = bin(n)[2:]
    if len(bits) < 10:
        bits = '0' * (10 - len(bits)) + bits
    last = bits[-i:]
    newlast = "".join(['0' if c == '1' else '1' for c in last])
    new = bits[:-i]+newlast
    return int(new, 2)
    

def toInt(S):
    pot = 1
    sum = 0
    for c in S:
        if c == "-":
            sum += pot
        pot *= 2
    return sum


def solveB():
    T = int(input())
    c = 0
    
    # + = 0, - = 1
    # most significant is bottom
    vals = [-1] * 1024
    vals[0] = 0
    steps = 1
    todo = [0] # all happy side
    while len(todo) > 0:
        newtodo = []
        for current in todo:
            for i in range(1, 11):
                result = flip(current, i)
                if vals[result] == -1:
                    vals[result] = steps
                    newtodo += [result]
        todo = newtodo
        steps += 1
        
        
    while c < T:
        c += 1
        S = input()
        
        solution = vals[toInt(S)]
        result = "Case #%i: %i" % (c, solution)
        print(result)
        
solveB()
