


inputs = int(raw_input())

for i in range(inputs):
    n = int(raw_input())
    oks = [0] * 10
    ok_count = 0

    m = n

    if n == 0:
        m = "INSOMNIA"
    else:
        while ok_count < 10:
            decon = m
            while decon > 0:
                digit = decon % 10
                if oks[digit] == 0:
                    oks[digit] = 1
                    ok_count += 1
                decon = decon / 10
            if ok_count < 10:
                m += n
    print "Case #" + str(i+1) + ": " + str(m)
    
    
