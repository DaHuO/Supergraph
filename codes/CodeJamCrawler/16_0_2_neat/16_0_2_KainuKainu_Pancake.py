T = int(input())
C = 1
while (C<=T):
    print("Case #%d: " % C,end="")
    S = input()
    reg = 0
    prev = ""
    for x in S:
        if x != prev:
            prev = x
            reg += 1
    if prev == "+": print(reg-1)
    else: print(reg)
    C += 1
