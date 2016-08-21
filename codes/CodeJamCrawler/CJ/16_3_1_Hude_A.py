def sol_print(value):
    sol_print.line_number += 1;
    print "Case #%d: %s"%(sol_print.line_number, value)
sol_print.line_number = 0

N = int(raw_input())

inputs = []
for i in range(N):
    evacuation = dict()
    evacuation['N'] = int(raw_input())
    evacuation['nb_by'] = map(int, raw_input().split())
    inputs.append(evacuation)


for evacuation in inputs:
    tamere = ""
    while evacuation['nb_by'] != [0] * evacuation['N']:
        toto = ""
        # print evacuation['nb_by']
        # CHOSE FIRST
        max1 = evacuation['nb_by'][0]
        idx1 = 0
        for idx, nb in enumerate(evacuation['nb_by']):
            if nb > max1:
                max1 = nb
                idx1 = idx
        f1 = chr(idx1 + 65)
        evacuation['nb_by'][idx1] -= 1
        tamere += str(f1)


        if evacuation['nb_by'] == [0] * evacuation['N']:
            break
        # # ACTUAL SUM IF WE MOVE 1 GUY
        sum = 0
        for party in evacuation['nb_by']:
            sum += party

        # # CHOSE SECOND
        max2 = evacuation['nb_by'][0]
        idx2 = 0
        for idx, nb in enumerate(evacuation['nb_by']):
            if nb > max2:
                max2 = nb
                idx2 = idx
        f2 = chr(idx2 + 65)
        evacuation['nb_by'][idx2] -= 1
        for party in evacuation['nb_by']:
            if party > sum / 2:
                evacuation['nb_by'][idx2] += 1
                f2 = ""

        tamere += str(f2) + " "

    test = tamere.split(" ")
    if len(test[len(test) - 1]) == 1:
        tmp = test[len(test) - 1]
        test[len(test) - 1] = test[len(test) - 2]
        test[len(test) - 2] = tmp

    tamere = " ".join(test)
    sol_print(tamere)