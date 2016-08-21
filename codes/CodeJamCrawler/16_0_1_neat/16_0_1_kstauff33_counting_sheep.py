cases = int(raw_input())

for x in range(1, cases+1):
    not_seen = list('0123456789')
    start_num = int(raw_input())

    if start_num == 0:
        print 'Case #' + str(x) + ': INSOMNIA'
        continue

    cur_num = 0
    while len(not_seen) > 0:
        cur_num += start_num
        str_num = str(cur_num)
        ar = list(not_seen)
        for num in ar:
            if str_num.find(num) != -1:
                not_seen.remove(num)

    print 'Case #' + str(x) + ': ' + str(cur_num)
