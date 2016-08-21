def check_numbers(numbers):
    for x in numbers:
        if not x:
            return False
    return True

def set(numbers, value=False):
    for i in range(len(numbers)):
        numbers[i] = value
        
f = open("A-large.in", 'r') #opens a file at the beginning
line=f.readline() #reads the next line of the file (until next \n)
N=int(line)
numbers= []
for i in range(10):
    numbers.append(False)
for i in range(N):
    set(numbers)
    line=f.readline()
    line = line.split(sep='\n')[0]
    N2 = int(line)
    
    for char in line:
        numbers[int(char)] = True
            
    if N2 == 0:
        set(numbers,True)
        line = 'INSOMNIA'
    j=2            
    while not check_numbers(numbers):
        line =str(N2*j)
        for char in line:
            numbers[int(char)] = True
        j+=1
    print('Case #'+str(i+1)+': '+line)