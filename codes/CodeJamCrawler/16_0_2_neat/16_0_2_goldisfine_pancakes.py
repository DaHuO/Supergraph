# Sam Finegold
# Google Code Challenge
# Problem 2: Revenge of the Pancakes

from itertools import groupby

# def flip(l,i):
#     rev = l[0:i]
#     rev.reverse()
#     flipped = [abs(p - 1) for p in rev]
#     final = flipped + l[i:len(l)]
#     return final

def count_ones_streak(L):
    no_end = L[0:len(L)-1]
    return sum(no_end)

def min_flips(L):
    grouped_L = [(k, sum(1 for i in g)) for k,g in groupby(L)]
    ones_and_zeroes = [s[0] for s in grouped_L]
    ones_streak = count_ones_streak(ones_and_zeroes)
    return sum([1 for i in ones_and_zeroes if i == 0]) + ones_streak
    # print L
    # print zeroes
    # if len(zeroes) == 0:
    #     return 0
    # elif len(L) % 2 == 0:
    #     return 2*sum([1 for i in zeroes if i == 0])
    # else:
    #     return 2*sum([1 for i in zeroes if i == 0]) - 1


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
  pluses_and_minues = list(raw_input())
  zeroes_and_ones = [0 if j == '-' else 1 for j in pluses_and_minues]
  print "Case #{}: {}".format(i, min_flips(zeroes_and_ones))


# print min_flips([1,0,1]) # 2
# print min_flips([1,1,0]) # 2
# print min_flips([0,0,0,0]) # 1
# print min_flips([1,0,1,0])  # 4
# print min_flips([0,1,0,1,0]) # 5
# print min_flips([1,0,1,0,1,0]) # 6

# seq,          flips,      unique zero strk    unique zero strk with ones left
# [0,0]             1       1                   0
# [1,1]             0       0                   0
# [0,1]             1       1                   0
# [1,0]             2       1                   1
# [0,0,0]           1       1                   0
# [1,1,1]           0       0                   0
# [1,0,0]           2       1                   1
# [0,1,0]           3       2                   1
# [0,0,1]           1       1                   0
# [1,1,0]           2       1                   1
# [1,0,1]           2       1                   1
# [0,1,1]           1       1                   0
# [0,0,0,0]         0       1                   0
# [1,1,1,1]         0       0                   0
# [1,0,0,0]         2       1                   1
# [0,1,0,0]         3       2                   1
# [0,0,1,0]         3       2                   1
# [0,0,0,1]         1       1                   0
# [1,1,0,0]         2       1                   1
# [1,0,1,0]         4       2                   2
# [1,0,0,1]         2       1                   1
# [0,1,1,0]         3       2                   1
# [0,1,0,1]         3       2                   1
# [1,0,1,1]         2       1                   1
# [0,1,0,1,0]       5       3                   2
# [1,0,1,0,1,0]     6       3                   3
#
# zero +
# 2*zero - 1
# 2*zero


# Relationships between sets with (n-1) and n
