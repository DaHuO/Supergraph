#! /usr/bin/python3

T = int(input())

for i in range(T):
    _initialTiles, _complexity, _students = map(int, input().split())
    solution = []

    if _complexity == 1 or _initialTiles == 1:
        if _students < _initialTiles:
            print("Case #%i: IMPOSSIBLE" % (i+1))
            continue

        else: 
            solution = [k for k in range(1, _initialTiles+1)]

    elif _students < _initialTiles - 1:
        print("Case #%i: IMPOSSIBLE" % (i+1))
        continue
    
    else:
        solution = [k for k in range(2, _initialTiles*(_initialTiles-1)+1, _initialTiles+1)]
    
    print("Case #%i: %s" % (i+1, ' '.join(str(el) for el in solution)))