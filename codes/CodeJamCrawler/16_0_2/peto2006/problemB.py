n = int(input())
for case in range(1, n+1):
    s = input()
    last = '+'
    counter = 0
    for c in range(len(s)-1, -1, -1):
        if s[c] != last:
            counter += 1
            last = s[c]
    print("Case #", case, ": ", counter, sep="")