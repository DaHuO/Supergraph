def count_sheep(n):
    if n == 0:
        return "INSOMNIA"
    nums = []
    a, c = 0, 1
    while len(nums) < 10:
        a = c * n
        nums = nums + [x for x in list(set(str(a))) if x not in nums]
        c += 1
    return a

def start():
    output_file = open('output.txt', 'w+')
    t = int(raw_input().strip())
    for test in xrange(t):
        n = int(raw_input().strip())
        print "Case #{case}: {result}".format(case=test+1, result=count_sheep(n))
        output_file.write("Case #{case}: {result}\n".format(case=test+1, result=count_sheep(n)))