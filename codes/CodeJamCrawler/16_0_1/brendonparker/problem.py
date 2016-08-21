from sys import argv

input_file = argv[1]+'/A-large.in'
f = open(input_file)
o = open(input_file.replace('.in', '.out'), 'w')

test_count = int(f.readline())

def parseNumber(num, nums):
    for x in str(num):
        nums[x] = True
    #print (num, nums)

for case_number in range(1, test_count+1):
    n = int(f.readline())
    i = 0
    print 'Case %d' % n
    if n != 0:
        nums = {}
        while len(nums.keys()) != 10:
            i += 1
            #print n * i
            parseNumber(n*i, nums)
        o.write("Case #%d: %d\n" % (case_number, n * i))
    else:
        o.write("Case #%d: INSOMNIA\n" % case_number)

print 'Done'