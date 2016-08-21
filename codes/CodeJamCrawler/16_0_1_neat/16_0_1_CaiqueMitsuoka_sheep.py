def VerChar(Ovelhas,num):
    Ovelhas = list(Ovelhas)
    if '0' in Ovelhas:
        num[0] = True
    if '1' in Ovelhas:
        num[1] = True
    if '2' in Ovelhas:
        num[2] = True
    if '3' in Ovelhas:
        num[3] = True
    if '4' in Ovelhas:
        num[4] = True
    if '5' in Ovelhas:
        num[5] = True
    if '6' in Ovelhas:
        num[6] = True
    if '7' in Ovelhas:
        num[7] = True
    if '8' in Ovelhas:
        num[8] = True
    if '9' in Ovelhas:
        num[9] = True
    return num

casos = int(input())
for case in range(1,casos+1):
    NOvelhas = str(input())
    cont = 1
    insonia = True
    num = [False,False,False,False,False,False,False,False,False,False]
    NNvelhas = NOvelhas
    if (int(NOvelhas) == 0):
        print('Case #{}: INSOMNIA'.format(case))
        continue
    while True:
        num = VerChar(NNvelhas,num)
        chares = 0
        for charc in num:
            if charc:
                chares += 1
        if chares == 10:
            print('Case #{}: '.format(case), NNvelhas)
            break;
        # print(NNvelhas)
        NNvelhas = str(int(NOvelhas) * cont)
        cont += 1
