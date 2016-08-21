
with open("C:\\Users\\prakhar\\Downloads\\B-large.in") as f:
    lines = f.readlines()
def input():
    return lines.pop(0).rstrip('\n')

OUT = ""
T = int(input())
for _i in range(T):

    S = list(input())
    p = S.pop(0)
    L = len(S)
    C = 0
    for l in S:
        if l==p:
            pass
        else:
            C=C+1
        p = l
    if p=='-':
        C=C+1

    OUT += ("Case #" + str(_i+1) + ": " + str(C) + "\n")


    # print(str(C) + "->"  + str(S))
with open("JAM2.out" , 'w') as file:
    file.write(OUT)







