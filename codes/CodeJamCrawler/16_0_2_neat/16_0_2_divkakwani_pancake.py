
def count_runs(s):
    runs = 1
    head = s[0]
    for i in range(1, len(s)):
        if head != s[i]:
            runs += 1
        head = s[i]
    return runs


t = int(input())

for caseid in range(1, t+1):
    s = input()
    runs = count_runs(s)
    print("Case #%s: %s" % (caseid, runs-1 if s[-1] == '+' else runs))


