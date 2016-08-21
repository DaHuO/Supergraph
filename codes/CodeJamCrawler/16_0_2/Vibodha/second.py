
for t in range(int(input())):
    N = input()
    side = N[0]
    flips = 0
    for i in range(len(N) - 1):
        if N[i] != N[i+1]:
            if side == "+":
                side = "-"
            else:
                side = "+"

            flips +=1
    if side=="-":
        flips += 1
    print("Case #"+str(t+1) + ": " + str(flips))



