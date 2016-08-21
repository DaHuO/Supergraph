get_bin = lambda x, n: format(x, 'b').zfill(n)
final = []
with open('testtt.in') as g:
    for line in g:
        temp = ''
        for x in line:
            if x == '-':
                temp += '0'
            if x == '+':
                temp += '1'
        final.append(temp)
casecounter = 0
for i in final:
    count, count0s, count1s = 0,0,0
    casecounter += 1
    temporary = ''
    for realshit in range(len(i)):
        if i[realshit] == '0':
            count0s += 1
        else:
            count1s += 1
    if count0s == len(i):
        print ("Case #" + str(casecounter) + ": 1")
        continue
    elif count1s == len(i):
        print ("Case #" + str(casecounter) + ": 0")
        continue
    while True:
        count += 1
        doit = True
        done = False
        for all0 in range(len(i)):
            if i[all0] == '1':
                doit = False
        if doit:
            print ("Case #" + str(casecounter) + ": " + str(count))
            break
        for well in range(len(i)):
            if i[well] == '1':
                if temporary == '':
                    break
                else:
                    i = temporary + i[well:]
                    done = True
                    break
            else:
                temporary += '1'
        nicetry = 1
        for w in i:
            if w == '0':
                nicetry = 0
                break
        if nicetry != 0:
            print ("Case #" + str(casecounter) + ": " + str(count))
            break
        temparray = ''
        for well in range(len(i)):
            if i[well] == '1':
                temparray += '0'
            else:
                i = temparray + i[well:]
                if done == True:
                    count += 1
                break
            
