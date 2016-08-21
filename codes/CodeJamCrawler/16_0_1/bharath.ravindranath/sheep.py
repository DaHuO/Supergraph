def sheep(case):
    #seen = {0: 0, 1: 0, 2: 0, 3: 0,4: 0,5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    seen = []
    i = 1;
    base = int(input())
    if base == 0:
        print('Case #', case, ': INSOMNIA', sep='')
        return
    else:
        while len(seen) != 10:
            base1 = i*base;
            number_string = str(base1)
            for ch in number_string:
                if ch not in seen:
                    seen.append(ch)
            #print(seen)
            i = i+1
        print('Case #', case, ': ',base1, sep='')
        
        


T = int(input())
for i in range(1,T+1):
    sheep(i)

