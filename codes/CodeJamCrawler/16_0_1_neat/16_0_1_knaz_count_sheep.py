def read_int():
    return int(raw_input())

T_ = read_int()

asleep = int('0b1111111111', 2)
seen_num = []
for i in range(10):
    seen_num.append(1 << 9-i)
for t_ in range(T_):
    N = read_int()
    if N == 0:
        print 'Case #%i:'%(t_ + 1), 'INSOMNIA'
    else:
        sleep_status = 0
        indx = 0
        done_ = False
        while not done_:
            last_named_num = N * (indx + 1)
            str_N = str(last_named_num)
            for ch in str_N:
                sleep_status = sleep_status | seen_num[int(ch)]
                if sleep_status == asleep:
                    done_ = True
                    break
            indx += 1
        print 'Case #%i:'%(t_ + 1), last_named_num