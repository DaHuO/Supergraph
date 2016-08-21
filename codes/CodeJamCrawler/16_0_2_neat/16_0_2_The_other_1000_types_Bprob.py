# Import the file
in_file = 'B-large.in'
Type = 'small' if in_file.count('small') > 0 else 'large' if in_file.count('large') > 0 else 'test'
out_file = 'B-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

data2 = data.copy()
# Format the data
Tt = int(data[0])
del data[0]

OUT = []
for k in range(Tt):
    # Enter code here
    # Try a greedy algorithm...
    Seq = [i for i in list(data[k]) if i in ('-', '+')]
    print('=============================')
    print(Seq)
    Base = Seq[0]
    del Seq[0]
    Count = 0
    while True:
        if len(Seq) == 0:
            if Base == '+':
                OUT.append(Count)
            else:
                OUT.append(Count+1)
            break
        if Seq[0] == Base:
            del Seq[0]
        else:
            Base = Seq[0]
            del Seq[0]
            Count += 1
            
        
        

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i]))
