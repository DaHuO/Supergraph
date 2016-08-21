t = int(raw_input())
digit_set = {'1','2','3','4','5','6','7','8','9','0'}

for i in range(t):
    num = int(raw_input())
    if num==0:
        print "Case #%d: INSOMNIA" % (i+1,)
        continue
    dig_set = set()
    j = 1
    while True:
        tmp = num*j
        dig_set = dig_set.union(set(str(tmp)))
        if digit_set.issubset(dig_set):
            print "Case #%d: %d" % (i+1,tmp)
            break
        j = j+1

