def read(file):
    with open(file,'r') as f:
        inp = [line[:-1] if '\n' in line else line for line in f]
    for line in inp:
        yield line
def addline(file,line):
    with open(file,'a') as f:
        f.write(line)

f = read('input.txt')
num_lines = int(next(f))
cn = 1
for num in f:
    num = int(num)
    if num == 0:
        addline('output.txt',"Case #{}: INSOMNIA\n".format(cn))
    else:
        counts = [0]*10
        i = 1
        while 0 in counts:
            n = i*num
            for digit in str(n):
                counts[int(digit)] += 1
            i += 1
        addline('output.txt',"Case #{}: {}\n".format(cn,n))
    cn += 1
    
        
