n = int(input())
for case in range(1, n+1):
    num = int(input())
    if num == 0:
        print("Case #", case, ": ", "INSOMNIA", sep="")
        continue
    act = 0
    s = set()
    while not s == {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        act += num
        s = s.union(set((x for x in str(act))))
    print("Case #", case, ": ", act, sep="")
