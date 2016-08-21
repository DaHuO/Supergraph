# -*- coding: utf-8 -*-

def solve_case(n):
    if n == 0: return "INSOMNIA"
    digits = list(range(10))
    
    j=1
    while digits:
        nn = n*j
        i = 1
        while i <= nn:
            digit = (int((nn/i)%10))
            try:
                digits.remove(digit)
            except ValueError:
                pass
            i*=10
        j+=1
    return nn
        

if True:
    with open("out.txt", 'w') as out:
        with open("sheep.data") as file:
            n = int(file.readline())
            for i in range(n):
                sol = solve_case(int(file.readline()))
                out.write("Case #{}: {}\n".format(i+1,sol))