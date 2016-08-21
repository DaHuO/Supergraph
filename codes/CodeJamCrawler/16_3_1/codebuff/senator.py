# from utilities import nonstd
# std = nonstd.IO(in_file='sen.in', out_file='sen.out')
# #std = nonstd.In(in_file='gtd.in')

tcs = int(input())

for tc in range(1, tcs+1):
    print('Case #'+str(tc)+": ", end="")
    party = dict()
    nump = int(input())
    total = 0
    p_m = input().strip().split()
    for i in range(nump):
        party[chr(65 + i)] = int(p_m[i])
        total += party[chr(65 + i)]
    while party:
        sp = sorted(party, key=lambda x:party[x], reverse=True)
        if len(party) == 3 and total == 3:
            print(sp[0], end=" ")
            print(sp[1]+sp[2], end=" ")
            party = None
            continue
        print(sp[0]+sp[1], end=" ")
        party[sp[0]] -= 1
        party[sp[1]] -= 1
        total -= 2
        if party[sp[0]] == 0:
            del party[sp[0]]
        if party[sp[1]] == 0:
            del party[sp[1]]
    print()


