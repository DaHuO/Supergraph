import sys

f = open(sys.argv[1], 'r')
cases = [int(line.strip()) for line in f]

f.close()
if cases[0] != len(cases) -1:
    print "error"
    sys.exit(1)
def sheep(number):
    if number == 0:
        return 'INSOMNIA'
    digits = set()
    mult = 1
    res =0
    while len(digits) < 10:
        res = number * mult
        for digit in str(res):
            digits.add(digit)
        mult +=1
    return str(res)
f = open(sys.argv[1]+'.out', 'w')
for idx, item in enumerate(cases[1:]):
    f.write('Case #%i: %s\n' % (idx+1, sheep(item)))
f.close()
    
