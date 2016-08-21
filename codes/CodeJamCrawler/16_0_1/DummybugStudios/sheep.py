case =0
f = open('input.in')
f.readline()
while True:
    try:
        base = int(f.readline())
    except ValueError:
        break
    num = base
    seen = []
    allnums = [i for i in range (10)]

    counter = 0
    c=0
    while 1:
        c+=1
        added_this_round = 0
        for i in str(num):
            if not(int(i) in seen): 
                seen.append(int(i))
                counter = 0
                added_this_round += 1
        seen.sort()
        if seen == allnums:
            case += 1
            print('Case #%d:'%case, end= " ")
            print(num)
            break
        elif counter > 50:
            case += 1
            print('Case #%d:'%case, end= " ")
            print('INSOMNIA')
            break
        elif added_this_round == 0:
            counter += 1
        num = c*base
