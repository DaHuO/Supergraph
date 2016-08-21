def solve(n):
    sol = []
    d = 1

    n = n[0]

    S = ["ZERO" , "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]



    z = (n.count('Z'))
    h = (n.count('H'))
    six = (n.count('X'))
    u = (n.count('U'))
    g = (n.count('G'))
    w = n.count('W')

    x = [0]*15
    for i in range(len(n)):
        if n[i] == "E":
            x[0] += 1
        if n[i] == "F":
            x[1] += 1
        if n[i] == "G":
            x[2] += 1
        if n[i] == "H":
            x[3] += 1
        if n[i] == "I":
            x[4] += 1
        if n[i] == "N":
            x[5] += 1
        if n[i] == "O":
            x[6] += 1
        if n[i] == "R":
            x[7] += 1
        if n[i] == "S":
            x[8] += 1
        if n[i] == "T":
            x[9] += 1
        if n[i] == "U":
            x[10] += 1
        if n[i] == "V":
            x[11] += 1
        if n[i] == "W":
            x[12] += 1
        if n[i] == "X":
            x[13] += 1
        if n[i] == "Z":
            x[14] += 1

    #Z
    x[14] -= z
    x[0] -= z
    x[7] -= z
    x[6] -= z

    #h
    # x[9] -= h
    # x[3]-= h
    # x[7] -= h
    # x[0]-= 2*h

    #x
    x[8] -= six
    x[4]-= six
    x[13]-= six

    #u
    x[1] -= u
    x[6]-= u
    x[10]-= u
    x[7]-= u

    #g
    x[0] -= g
    x[4]-= g
    x[2]-= g
    x[3]-= g
    x[9]-= g

    #w
    x[9] -= w
    x[12] -= w
    x[6] -= w


    xr = x[7]
    x[9] -= xr
    x[3]-= xr
    x[7] -= xr
    x[0]-= 2*xr


    xo = x[6]

    #o
    x[6] -= xo
    x[5] -= xo
    x[0] -= xo

    xs = x[8]

    #s
    x[8] -= xs
    x[0] -= 2*xs
    x[11] -= xs
    x[5] -= xs

    xv = x[11]

    #v
    x[1] -= xv
    x[4] -= xv
    x[11] -= xv
    x[0] -= xv


    xi = x[4]

    sol = "0"*z + "1" * xo + "2"*w + "3"*xr + "4"*u + "5"*xv + "6"*six + "7"*xs + "8"*g + "9"*xi

    print(sol)
    return d, sol



IN = open('input.txt', 'r')
OUT = open('output.txt', 'w')

T = int(IN.readline())

for line in range(T):
    # Instanz mit mehreren Zeilen
    yes = 0
    if yes == 0:
        #sizen = int(IN.readline())
        n = list(map(str, IN.readline().split()))
    else:
        T0 = int(IN.readline())
        n = []
        for i in range(T0):
            n.append(list(map(int, IN.readline().split())))

    if solve(n)[0] == 1:
        answer = solve(n)[1]
        OUT.write('Case #{}: {}\n'.format(line + 1, answer))
    else:
        OUT.write('Case #{}:\n'.format(line + 1))
        for i in range(len(solve(n)[1])):
            answer = (map(str,solve(n)[1][i]))
            OUT.write('{}\n'.format(answer))
    if yes == 1:
        line -= T0
IN.close()
OUT.close()