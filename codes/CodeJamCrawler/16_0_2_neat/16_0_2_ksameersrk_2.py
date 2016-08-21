for case in range(1, int(input())+1):
    tmp = []
    for i in input():
        if i == '+':
            tmp.append(1)
        else:
            tmp.append(-1)

    toggle = 1
    count = 0
    for i in tmp[::-1]:
        if i * toggle == -1:
            toggle *= -1
            count += 1

    print("Case #"+str(case)+": "+str(count))
