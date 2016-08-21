import sys
sys.stdin = open('input.in', 'r')
sys.stdout = open('output.out', 'w')
t = int(input())
for k in range(t):
    s = input()
    ans = 0
    for i in range(1,len(s)):
        if s[i-1] != s[i]:
            ans+=1
    ans += (s[-1] == '-')
    print('case #', k+1, ': ',ans, sep = '')
    