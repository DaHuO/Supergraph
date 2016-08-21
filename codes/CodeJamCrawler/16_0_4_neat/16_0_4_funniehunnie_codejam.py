case = int(input())
for a in range(case):
    k, c, s = list(map(int,input().split()))
    string = ''
    if s < k:
        string = 'IMPOSSIBLE'
    else:
        for i in range(s):
            string += str(i+1) + ' '
    print("Case #%i: %s" %(a + 1, string))
