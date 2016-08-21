
def solve(K, C, S):
    solution = []
    for i in range(K):
        solution += [K ** (C-1) * i + 1]
    return " ".join(map(str,solution))

def solveC():
    T = int(input())
    c = 0
      
        
    while c < T:
        c += 1
        string = input()
        [K, C, S] = map(int, string.split())
        
        result = "Case #%i: %s" % (c, solve(K, C, S))
        print(result)
        
solveC()
