f = open('A-large.in', 'r')
g = open('output_A_Large.txt', 'w')
num_loops = int(f.readline())

for i in range(0,num_loops):
    letters = list(f.readline())
    finalwords = []
    for j in letters:
        if finalwords == []:
            finalwords.append(j)
        else:
            if j >= finalwords[0]:
                finalwords = [j] + finalwords
            else:
                finalwords = finalwords + [j]
    str1 = ''.join(finalwords)
    #print(str1)
    string = str('Case #' + str(i+1) + ': ' + str1)
    g.write(string)


f.close()
g.close()

