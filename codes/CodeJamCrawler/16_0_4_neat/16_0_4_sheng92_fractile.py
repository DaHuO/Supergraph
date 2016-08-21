import itertools

input ='''100
2 3 2
1 1 1
2 1 2
3 2 3
63 4 63
3 1 3
12 2 12
53 10 53
4 3 4
3 35 3
41 11 41
98 9 98
3 37 3
75 1 75
7 7 7
23 5 23
3 19 3
1 100 1
80 8 80
1 2 1
56 8 56
49 4 49
27 7 27
1 29 1
100 4 100
97 8 97
6 7 6
2 4 2
52 2 52
100 3 100
1 95 1
44 9 44
99 7 99
39 11 39
3 7 3
3 4 3
92 1 92
9 18 9
2 2 2
100 1 100
68 1 68
2 59 2
93 8 93
7 5 7
58 6 58
85 3 85
21 4 21
1 4 1
72 1 72
25 1 25
64 4 64
9 1 9
54 6 54
2 22 2
20 11 20
68 9 68
10 18 10
40 9 40
1 93 1
37 5 37
94 8 94
10 5 10
12 9 12
1 14 1
11 10 11
11 15 11
16 4 16
4 8 4
8 11 8
14 7 14
4 1 4
54 8 54
32 5 32
22 4 22
4 29 4
96 4 96
82 3 82
100 2 100
89 1 89
86 4 86
2 49 2
3 16 3
19 7 19
1 3 1
97 9 97
2 5 2
100 9 100
79 8 79
3 3 3
63 7 63
48 10 48
57 7 57
93 9 93
2 14 2
4 2 4
86 3 86
71 3 71
4 4 4
23 7 23
4 16 4

'''

def expandTile(tiles, k, c):
    tempTiles = tiles
    for i in range(c-1):
        newTiles = ''
        for tile in tempTiles:
            if tile == '0':
                newTiles += tiles
            else:
                newTiles += '1'*k
        tempTiles = newTiles
    return tempTiles

def getTile(k,c,s):
    # if k == s and k == 1:
        # return 'IMPOSSIBLE'
    # else:
        return  ' '.join(map(str,[i+1 for i in range(s)]))
    # tiles = []
    # for i in range(1, 2**k):
        # tiles += [expandTile("{0:b}".format(i).zfill(k), k, c)]
    # print tiles
    # found = False
    # for cleans in itertools.combinations(range(len(tiles[0])),s):
        # print cleans
        # leads = [False]*len(tiles)
        # for i in range(len(tiles)):
            # lead = True
            # for clean in cleans:
                # if tiles[i][clean] == '1':
                    # lead = False
            # if lead:
                # leads[i] = True
        # if not any(leads):
            # found = True
            # break
    # cleans = [i+1 for i in cleans]
    # if found:
        # return ' '.join(map(str,cleans))
    # else:
        # return 'IMPOSSIBLE'


split = input.splitlines()
for i in range(1, int(split[0])+1):
    print 'Case #%i: ' % i + getTile(*tuple([int(j) for j in split[i].split()]))
    