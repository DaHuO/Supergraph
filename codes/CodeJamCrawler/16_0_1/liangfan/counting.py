import sys, math

# nums = []
# for line in sys.stdin:
#     nums.append(int(line.strip()))
#
# n = nums[0]
# tcase = 1
# while tcase <= n:
#     x = nums[tcase]
#     if x == 0:
#         print "Case #%d: INSOMNIA" % tcase
#     else:
#         all_nums = set([str(i) for i in xrange(10)])
#         t = 1
#         while True:
#             all_nums = all_nums - set(str(x))
#             if len(all_nums) == 0:
#                 print "Case #%d: %d" % (tcase, x)
#                 break
#             t += 1
#             x = t * nums[tcase]
#     tcase += 1

tcase = 1
with open(sys.argv[1], 'r') as fin:
    n = -1
    for line in fin.readlines():
        line = line.strip()
        if n == -1:
            n = int(line)
        else:
            xi = int(line)
            if xi == 0:
                print "Case #%d: INSOMNIA" % tcase
            else:
                all_nums = set([str(i) for i in xrange(10)])
                t = 1
                x = xi
                while True:
                    all_nums = all_nums - set(str(x))
                    if len(all_nums) == 0:
                        print "Case #%d: %d" % (tcase, x)
                        break
                    t += 1
                    x = t * xi
            tcase += 1
