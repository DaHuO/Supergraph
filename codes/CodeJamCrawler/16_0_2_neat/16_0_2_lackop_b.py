def otoc(kolace, hl):
    newkolace = []
    for k in reversed(kolace[:hl]):
        if k == '-':
            newkolace.append('+')
        else:
            newkolace.append('-')
    newkolace.extend(kolace[hl:])

    return newkolace

strom = []
stromold = []

def spracujhlbku(stromin, stromout):
    for s in stromin:
        for i in range(1, len(s) + 1):
            n = otoc(s, i)
            f = False
            for ch in n:
                if ch == '-':
                    f = True
                    break
            if not f:
                stromout.append(n)
                return 1
            else:
                if not n in stromout:
                    stromout.append(n)
    return 0



f = open('B-small.in', 'r')
out = open('B-small.txt', 'w')
T = int(f.readline())

for case in range(T):
    print(case)
    line = f.readline().strip()
    stromin = [[]]
    for a in line:
        stromin[0].append(a)

    fa = False
    for ch in line:
        if ch == '-':
            fa = True
            break
    if not fa:
        out.write("Case #" + str(case + 1) + ": 0\n")
    else:
        count = 1
        strom = []
        #print(stromin, strom)
        while not spracujhlbku(stromin, strom):
            stromin = strom.copy()
            strom = []
            #print(stromin, strom)
            count += 1
            #stromin = []
            #if (spracujhlbku(strom, stromin)):
            #    break
            #count += 1

        #print(count)
        out.write("Case #" + str(case + 1) + ": " + str(count) + "\n")

#print(spracujhlbku([['+', '-', '-', '+']], strom))

#print(strom)

# def prehladavanie(kolace, hlbka):
#     if hlbka > 20:
#         return
#     for i in len(kolace):
#         prehladavanie(otoc(kolace, i), hlbka)
#
# kol = ['+', '-', '-', '+']
#
# print(kol)
# for i in range(1, len(kol) + 1):
#     print(otoc(kol, i))
#
#

# f = open('A-large.in', 'r')
# out = open('out-large.txt', 'w')
# T = int(f.readline())
#
# for case in range(T):
#     line = f.readline()
#     pattern = line.strip().split()
#     max = int(pattern[0])
#
#     audience = pattern[1]
#
#     sum = 0
#     invite = 0
#     for i in range(max + 1):
#         if (int(audience[i]) + sum) < i + 1:
#             invite += 1#i + 1 - (int(audience[i]) + sum)
#             sum += 1#i + 1 - (int(audience[i]) + sum)
#         else:
#             sum += int(audience[i])
#
#     print(invite)
#     out.write("Case #" + str(case + 1) + ": " + str(invite) + "\n")
#
#
