T = input()

for test_case in range(1, T+1):
    K, C, S = map(int, raw_input().split())
    print "Case #%s:" % (test_case,),
    for i in range(1, K+1):
        print i,
    print
