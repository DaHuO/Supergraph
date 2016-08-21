f = open('input_2.txt', 'r')
fout = open('output.txt', 'w+')
total = int(f.readline())
print total
for i in range(total):
    num_s = f.readline()
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    n = 1
    arr_hit = 0
    num = int(num_s)
    if num == 0:
            fout.write("Case #%d: INSOMNIA\n" % (i+1))
            print "Case #%d: %s INSOMNIA" % (i+1, num_s[:-1])
            continue
    while n < 100*len(num_s):
        num_c = num*n
        for j in range(len(str(num_c))):
            if arr[int(str(num_c)[j:j+1])] == 1:
                pass
            else:
                arr[int(str(num_c)[j:j+1])] = 1
                arr_hit += 1
            if arr_hit == 10:
                break
        if arr_hit == 10:
            break
        n += 1
    if arr_hit == 10:
            fout.write("Case #%d: %d\n" % (i+1, num_c))
            print "Case #%d: %s %d" % (i+1, num_s[:-1], num_c)
    else:
            fout.write("Case #%d: INSOMNIA" % (i+1))
            print "Case #%d: %s INSOMNIA" % (i+1, num_s[:-1])

f.close()
fout.close()
