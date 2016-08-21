def find_num(n, repeat_num, a):
    tmp_list = [int (d) for d in str(n * repeat_num)]
    for i in tmp_list:
        if a[i - 1] == 0:
            a[i - 1] = 1
    
    if sum(a) != 10:
        return find_num(n, repeat_num + 1, a)
    else:
        return n * repeat_num
        
    
t = int(raw_input())
for i in range(1, t+1):
    n = int(raw_input())
    if not n:
        print 'Case #{0}: {1}'.format(i, 'INSOMNIA')
    else:
        r = find_num(n, 1, [0] * 10)
        print 'Case #{0}: {1}'.format(i, r)
