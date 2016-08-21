cases = int(raw_input())

for i in range(0, cases):
    nbr_list = [0 for j in range (0, 10)]
    base = int(raw_input())
    factor = 0
    if base == 0:
        print 'Case #' + str(i + 1) + ': INSOMNIA'
    else:
        while 0 in nbr_list:
            factor += 1
            nbr = list(str(base*factor))
            for char in nbr:
                if char.isdigit():
                    nbr_list[int(char)] += 1
        print 'Case #' + str(i + 1) + ': ' + str(factor * base)
    
