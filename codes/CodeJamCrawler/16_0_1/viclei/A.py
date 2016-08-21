fName = 'A-large.in'
lines = open(fName, 'r')
out = open('out.txt', 'w')

N = int(lines.next())
for t in xrange(N):
    nums = {}
    digits = {}
    C = int(lines.next())
    o_C = C

    while True:
        if C in nums:
            out.write('Case #%i: INSOMNIA\n'%(t+1))
            break

        nums[C] = True
        tC = C
        while tC > 0:
            digits[tC%10] = True
            tC //= 10

        if len(digits) == 10:
            out.write('Case #%i: %i\n'%(t+1,C))
            break
        else:
            C += o_C



