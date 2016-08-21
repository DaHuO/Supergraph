for t in range(int(input())):       # First input is the number of cases.
    (K, C, S) = tuple(list(map(int, input().split())))
    SChoices  = map(lambda x: x+1, range(S))
    print("Case #%d:"%(t+1), *SChoices, sep=' ')
