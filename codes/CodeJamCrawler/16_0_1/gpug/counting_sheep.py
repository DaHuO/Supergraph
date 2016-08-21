import sys

def n_sheep(num):
    if num == 0: 
        return "INSOMNIA"
    
    digits = {str(n): False for n in range(10)}

    dig_to_count = num
    multiply = 2
    while True:
        
        str_dig = str(dig_to_count)
        for dig in str_dig:
            if digits[dig] == False:
                digits[dig] = True
            
        #if a number hasn't been seen yet        
        if False in digits.values():
            dig_to_count = num * multiply
            multiply += 1
        #if all numbers have been seen
        else:
            return dig_to_count
            break


infile = sys.stdin
next(infile)
count = 1
for line in infile:
    if not line:
        break
    
    nice_line = line.rstrip()

    print "Case #" + str(count) + ": " + str(n_sheep(int(nice_line)))
    count += 1
    
