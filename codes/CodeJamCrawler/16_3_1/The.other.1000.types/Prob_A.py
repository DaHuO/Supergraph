Type = 'large'
in_file = 'A-{0}.in'.format(Type)
out_file = 'A-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

Tt = int(data[0])
del data[0]

OUT = []

def Test_Vec(Vec):
    if max(Vec) > sum(Vec)/2:
        return(False)
    return(True)
# Must always finish with two senators in the room.
for k in range(Tt):
    N = int(data[0])
    P = list(map(int, data[1].split()))
    del data[:2]
    print(N,P)
    Alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
    Seq = []
    while sum(P) > 0:
        Test = P[:]
        Ind = Test.index(max(Test))
        Test[Ind] -= 1
        if Test_Vec(Test):
            Seq.append(Alp[Ind])
            P = Test[:]
        else:
            Ind2 = Test.index(max(Test))
            Test[Ind2] -= 1
            Seq.append(Alp[Ind]+Alp[Ind2])
            P = Test[:]
    OUT.append(' '.join(Seq))
    pass

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i]))