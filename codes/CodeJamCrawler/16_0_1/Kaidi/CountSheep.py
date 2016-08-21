f = open('A-large.in', 'r')
total = f.readline()
counter = 1
for line in f:
    lst = [False] * 10
    num = int(line)
    multiplier = 1
    final = ''
    for i in range(100):
        n = num * multiplier
        for digit in str(n):
            index = int(digit)
            lst[index] = True
        status = True
        for i in lst:
            if not i:
               status = False
        if status:
            final = str(n)
            break
        multiplier += 1
    if final:
        with open('A-large.out', 'a') as w:
            w.write('Case #' + str(counter) + ': ' + final + '\n')
    else:
        with open('A-large.out', 'a') as w:
            w.write('Case #' + str(counter) + ': INSOMNIA' + '\n')
    counter += 1
        
    
    
