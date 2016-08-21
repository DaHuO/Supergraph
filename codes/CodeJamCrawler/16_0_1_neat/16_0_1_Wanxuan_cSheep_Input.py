t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    all_num = [0,1,2,3,4,5,6,7,8,9]
    num = int(raw_input())
    count_num = []
    j = 1
    while set(count_num) != set(all_num):
        new = num
        if new == 0:
            break
        new = num * j
        j += 1
        if new >= 10:
            count_num += [int(a) for a in str(new)]
        else:
            count_num.append(new) 
    if num == 0:
        print "Case #{}: {}".format(i, "INSOMNIA")
    else: 
        print "Case #{}: {}".format(i, new)