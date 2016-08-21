ifile = 'A-large.in'
ofile = 'output.txt'
input = open(ifile, 'r')
output = open(ofile, 'w')
t = int(input.readline())
ref = ord('A')
str = 'ZWUXGOFVRI'
numbers = ['ZERO','TWO', 'FOUR', 'SIX', 'EIGHT', 'ONE', 'FIVE', 'SEVEN', 'THREE', 'NINE']
digits = ['0', '2', '4', '6', '8', '1', '5', '7', '3', '9']
for t_i in range(t):
    s = input.readline().strip()
    l = [0]*26
    ans = ''
    for c in s:
        l[ord(c)-ref]+=1
    for i in range(10):
        count = l[ord(str[i])-ref]
        for c in numbers[i]:
            l[ord(c)-ref]-=count
        ans +=digits[i]*count
    ans = ''.join(sorted(ans))
    output.write('Case #%d: %s\n'%(t_i+1, ans))