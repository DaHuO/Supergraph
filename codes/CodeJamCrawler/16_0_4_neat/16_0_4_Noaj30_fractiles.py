# Google Code Jam Qualification Round 2016
# Problem D. Fractiles

# String of length n.

# Complexity 1: Check every tile. (n)
# Complexity 2:

# (i) G -> G, L -> L (1)

# (ii)
# GG -> GGGG
# GL -> GGGL
# LG -> LGGG
# LL -> LLLL (1)

# (iii)
# GGG -> GGGGGGGGG
# GGL -> GGGGGGGGL
# GLG -> GGGGLGGGG
# GLL -> GGGGLLGLL
# LGG -> LGGGGGGGG
# LGL -> LGLGGGLGL
# LLG -> LLGLLGGGG
# LLL -> LLLLLLLLL (2)

# Start with string s of length K. Obtain f(s).
# Suppose the 2nd element of f(s) is 'L'.
# Then, the first and second elements of s are 'L'.
# Suppose the 2K + 4th element of f(s) is 'L' as well.
# Then, the third and fourth elements of s are 'L' also. It should take K/2 tries.

# It should take K/2 tries unless C = 1 in which case it will take K.

# Given K, C, S, which spaces do we check?
# First space 2.
# Complexity 2: Second space 2*K + 4.
# Complexity 3: Second space ???

# S = K on the small dataset. In other words, we are allowed to clean as many stones as we need.

# If the first stone is L, then we already start with the original sequence, no matter what the complexity is. Therefore, we can just check the first n stones.

def clean(K, C, S):
    s = ''
    for i in range(1, K):
        s += str(i) + ' '
    return s + str(K)

def fractiles():
    f = open('commands.txt', 'r')
    g = open('fractiles.txt', 'w')
    line = 0
    for i in f:
        if line == 0:
            T = int(i)
            line = 1
        else:
            spaces = 0
            K = ''
            C = ''
            S = ''
            for j in i:
                if j == ' ':
                    spaces += 1
                    if spaces == 1:
                        K = int(K)
                    else:
                        C = int(C)
                elif j == '\n':
                    S = int(S)
                else:
                    if spaces == 0:
                        K += j
                    elif spaces == 1:
                        C += j
                    else:
                        S += j
            g.write('Case #' + str(line) + ': ')
            g.write(clean(K, C, S))
            g.write((T != line)*'\n')
            line += 1
    f.close()
    g.close()
