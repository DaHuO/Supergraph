f = open('B-large.in', 'r')
total = f.readline()

counter = 1
for line in f:
    top = line[0]
    bottom = line[len(line)-2]
    group = 1
    for i in range(1, len(line)-1):
        if line[i] != line[i-1]:
            group += 1
    if group == 1 and top == '+':
        final = '0'
    elif group == 1 and top == '-':
        final = '1'    
    elif bottom == '+':
        final = str(group - 1)
    else:
        final = str(group)
    with open('B-large.out', 'a') as w:
        w.write('Case #' + str(counter) + ': ' + final + '\n')
    counter += 1
    
    
    
