import io
file = io.open('./A-large.in.txt', 'r')
i = 1
for line in file:
    if i == 1:
        i += 1
    else:    
        line = int(line)
        if line == 0 :
            print('Case #' + str(i-1) + ': INSOMNIA')
            i += 1
        else:
            line = str(line)
            add = int(line)
            num = dict()
            last = ''
	    while len(num) < 10:
                for char in line:
                    num[char] = ''
                last = line
                line = str(int(line)+add)
            print('Case #' + str(i-1) + ': '+ last)
            i+=1


