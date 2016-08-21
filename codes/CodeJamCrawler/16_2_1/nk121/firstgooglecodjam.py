import sys
sys.stdin = open("A-large.in", "r")
sys.stdout = open("output.txt", "w")
t = int(input())
listi = ["ZERO", "TWO", "SIX", "SEVEN", "EIGHT", "THREE", "FOUR", "FIVE", "NINE", "ONE"]
numb = ["0", "2", "6", "7", "8", "3", "4", "5", "9", "1"]
for i in range(t):
    ans = []
    s = input()
    was = dict()
    wass = set()
    for j in range(len(s)):
        if s[j] not in wass:
            was[s[j]] = 1
            wass.add(s[j])
        else:
            was[s[j]] += 1
    for j in range(10):
        minw = 1000000000
        for k in range(len(listi[j])):
            if listi[j][k] not in wass:
                minw = 0
                break
            else:
                minw = min(minw, was[listi[j][k]])
        else:
            ans.append(numb[j] * minw)
            for k in range(len(listi[j])):
                was[listi[j][k]] -= minw
    print("Case #", i + 1, ": ", "".join(sorted(ans)), sep="")