f = open("A-large.in", 'r') #opens a file at the beginning
line=f.readline() #reads the next line of the file (until next \n)
T=int(line)

for t in range(T):
    line=f.readline() #reads the next line of the file (until next \n)
    numbers = [0]*10
    charcters = {}
    for char in line:
        if char in charcters:
            charcters[char] += 1
        else:
            charcters[char] = 1
    if 'Z' in charcters: numbers[0] = charcters['Z']
    if 'W' in charcters: numbers[2] = charcters['W']
    if 'U' in charcters: numbers[4] = charcters['U']
    if 'O' in charcters: numbers[1] = charcters['O']-numbers[4]-numbers[2]-numbers[0]
    if 'F' in charcters: numbers[5] = charcters['F']-numbers[4]
    if 'X' in charcters: numbers[6] = charcters['X']
    if 'V' in charcters: numbers[7] = charcters['V']-numbers[5]
    if 'G' in charcters: numbers[8] = charcters['G']
    if 'H' in charcters: numbers[3] = charcters['H']-numbers[8]
    if 'N' in charcters: numbers[9] = (charcters['N']-numbers[1]-numbers[7])//2   
    answer = ''
    for i,often in enumerate(numbers):
        for j in range(often):
            answer += str(i)
    print('Case #'+str(t+1)+': '+answer)