def napln(cislo, cisla):
    c = cislo
    while c != 0:
        d = c % 10
        if not d in cisla:
            cisla.append(d)
        c = c // 10
        #print(d)


# for n in range(1, 1000000):
#     nn = n
#     #print(n)
#     end = False
#     cisla = []
#     napln(n, cisla)
#     while not end:
#         #print(cisla)
#         nn += n
#         napln(nn, cisla)
#         if len(cisla) == 10:
#             end = True
#             print(n, nn)

f = open('A-small-attempt0.in', 'r')
out = open('A-large.txt', 'w')
T = int(f.readline())

for case in range(T):
    N = int(f.readline())
    if N == 0:
        out.write("Case #" + str(case + 1) + ": INSOMNIA\n")
    else:
        cisla = []
        end = False
        nn = 0
        print(N)
        while not end:
            nn += N
            napln(nn, cisla)
            if len(cisla) == 10:
                end = True
                out.write("Case #" + str(case + 1) + ": " + str(nn) + "\n")