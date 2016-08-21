file = open("B-large.in", 'r')
outfile = open("pancakesOUT.txt", 'w')
cases = int(file.readline())

for i in range(cases):
    pancakes = file.readline()
    count = 0
    for index in range(len(pancakes)):
        if index == 0:
            if pancakes[index] == '-':
                count += 1
        else:
            if (pancakes[index]=='-') and (pancakes[index-1]=='+'):
                count += 2
    outfile.write('Case #' + str(i+1) + ': ' + str(count))
    if i != cases - 1:
        outfile.write('\n')


file.close()
outfile.close()
