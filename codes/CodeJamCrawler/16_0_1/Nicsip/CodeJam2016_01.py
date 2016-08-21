def fall_asleep(number):
    
    if number == 0:
        return 'INSOMNIA'
   
    found = [False] * 10
    i = 1
    
    while found.count(False) != 0:
        num = number * i
        numstring = str(num)
        for n in numstring:
            found[int(n)] = True
        i += 1
    
    return num

with open('A-large.in','r') as f:
    cases = [num.strip() for num in f]

with open('A-large-output.txt','w') as f:
    x = 1
    for i in cases[1:]:
        f.write('Case #' + str(x) + ': ' + str(fall_asleep(int(i))) + '\n')
        x += 1
