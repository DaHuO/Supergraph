# Read it
fin_s = "B-large.in"
fou_s = fin_s + '.out'
fin = open(fin_s, 'r')
fou = open(fou_s, 'w')

# Solve it
T = int(fin.readline())

for t in range(T):
    size = int(fin.readline())
    arr = []
    # Read routines
    for i in range(2*size - 1):
        str_arr = fin.readline().split(' ')
        for j in range(size):
            arr.append(int(str_arr[j]))
    
    clean = sorted(set(arr))
    
    missed = []
    
    for i in range(len(clean)):
        if(arr.count(clean[i]) %2 != 0):
            missed.append(clean[i])
    
    # Write routines
    fou.write('Case #' + str(t + 1) + ': ')
    for i in range(len(missed)):
        fou.write(str(missed[i]) + ' ')
    fou.write('\n')
    
# Finish it
fin.close()
fou.close()