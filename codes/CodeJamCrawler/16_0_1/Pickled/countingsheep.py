digits = [0 for i in range(10)]



def get_digits(inpt, n):
    inpt = inpt / (10**n)
    while inpt != 0:
        digit = inpt % 10
        digits[digit] = 1
        inpt = inpt / 10



def solve(inpt):
    j = inpt;
    n = 0;
    while(sum(digits) < 10):
        #print(j)
        d = get_digits(j, n)
        j = j + inpt
    return j - inpt



f = open('A-large.in')
num = int(f.readline())
#rint('num is ', num)

o = open('output.txt', 'w')

for i in range(num):
    digits = [0] * 10
    inp = int(f.readline())
    #print(inp)
    s = ''
    if(inp == 0):
        s = ''.join(['Case #', str(i+1), ': INSOMNIA', '\n'])
    else:
        sol = solve(inp)
        s = ''.join(['Case #', str(i+1), ': ', str(sol), '\n'])
    o.write(s)

o.close()
f.close()





