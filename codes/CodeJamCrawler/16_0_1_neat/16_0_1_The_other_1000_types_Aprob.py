# Import the file
in_file = 'A-large.in'
Type = 'small' if in_file.count('small') > 0 else 'large' if in_file.count('large') > 0 else 'test'
out_file = 'A-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

data2 = data.copy()
# Format the data
Tt = int(data[0])
del data[0]

OUT = []
for k in range(Tt):
    # Enter code here
    N = int(data[k])
    if k % 1000 == 0: print(k, N)
    if N == 0:
        OUT.append("INSOMNIA")
        continue
    Seen = set(str(N))
    Count = 1
    while True:
        #print(Seen, Count)
        if len(Seen) == 10:
            OUT.append(N*Count)
            break
        else:
            Count += 1
            Seen = Seen.union(set(str(N*Count)))
        
        

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i]))
