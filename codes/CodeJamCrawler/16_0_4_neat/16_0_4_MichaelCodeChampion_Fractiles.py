#Fractiles

file = open('Input_Fractiles.txt', 'r')
out = open('Output_Fractiles.txt', 'w')

for i in next(file).split():
    length = int(i)

q = 0
for line in file:
    x = []
    for i in line.split():
        x.append(int(i))

    q += 1
    K = x[0]
    C = x[1]
    S = x[2]

    y = []
    if C == 1:
        if S < K:
            out.write("Case #%s: IMPOSSIBLE\n" % q)
        else:
            out.write(("Case #%s:" % q))
            for k in range(S-1):
                w = k+1
                out.write(" %s" % w)
            out.write(" %s\n" % S)
    elif C > 1:
        out.write("Case #%s:" %q)
        for j in range(K-1):
            w = j*pow(K,C-1) + 1
            y.append(w)
            out.write(" %s" %w)
        w = (K-1)*pow(K,C-1) + 1
        out.write(" %s\n" % w)


out.close()



#
# print(S)
#
# for i in range(K):
#     for j in range(Y):
#         S[i][j] = 1
#
# print(S)
#
# GGGGLLGLL
# LGLGGGLGL
# LLGLLGGGG
#
#
#
# 1 LG
# 2 LGGG
# 3 LGGGGGGG
# 4 LGGGGGGGGGGGGGGGG
#
#
#
# 1 GL
# 2 GGGL
# 3 GGGGGGGGL
# 4 GGGGGGGGGGGGGGGL
#
#
#
# 1 GLL
# 2 GGG-GLL-GLL
# 3 GGG-GGG-GGG--GGG-GLL-GLL--GGG-GLL-GLL
# 4 GGG-GGG-GGG--GGG-GGG-GGG--GGG-GGG-GGG---GGG-GGG-GGG--GGG-GLL-GLL--GGG-GLL-GLL---GGG-GGG-GGG--GGG-GLL-GLL-GGG-GLL-GLL
#
#
#
# 1 LGL
# 2 LGL-GGG-LGL
# 3 LGL-GGG-LGL--GGG-GGG-GGG--LGL-GGG-LGL
# 4 LGL-GGG-LGL--GGG-GGG-GGG--LGL-GGG-LGL---GGG-GGG-GGG--GGG-GGG-GGG--GGG-GGG-GGG---LGL-GGG-LGL--GGG-GGG-GGG--LGL-GGG-LGL
#
#
# 1 LLG
# 2 LLG-LLG-GGG
# 3 LLG-LLG-LLG--LLG-LLG-LLG--GGG-GGG-GGG
# 4 LLG-LLG-LLG--LLG-LLG-LLG--GGG-GGG-GGG---LLG-LLG-LLG--LLG-LLG-LLG--GGG-GGG-GGG---GGG-GGG-GGG--GGG-GGG-GGG--GGG-GGG-GGG
#
#
#
#
#
# 1 GLLLL
# 2 GGGGG-GLLLL-GLLLL-GLLLL-LLLGL
#
#
# 1 LGLLL
# 2 LGLLL-GGGGG-LGLLL-LGLLL-LLLGL
#
#
# 1 LLGLL
# 2 LLGLL-LLGLL-GGGGG-LLGLL-LLLGL
#
#
# 1 LLLGL
# 2 LLLGL-LLLGL-LLLGL-GGGGG-LLLGL
#
#
# 1 LLLLG
# 2 LLLLG-LLLLG-LLLLG-LLLLG-GGGGG
#

