tests=int(input())
for test in range(1,tests+1):
    my_dict={}
    st=input()
    for ch in st:
        if ch in my_dict:
            my_dict[ch]+=1
        else:
            my_dict[ch]=1
    soln_count=[0]*10
    if 'Z' in my_dict:
        soln_count[0]=my_dict['Z']
        my_dict['E']-=soln_count[0]
        my_dict['R']-=soln_count[0]
        my_dict['O']-=soln_count[0]
        my_dict.pop('Z')

    if 'W' in my_dict:
        soln_count[2]=my_dict['W']
        my_dict['T']-=soln_count[2]
        my_dict['O']-=soln_count[2]
        my_dict.pop('W')

    if 'U' in my_dict:
        soln_count[4]=my_dict['U']
        my_dict['F']-=soln_count[4]
        my_dict['O']-=soln_count[4]
        my_dict['R']-=soln_count[4]
        my_dict.pop('U')

    if 'X' in my_dict:
        soln_count[6]=my_dict['X']
        my_dict['S']-=soln_count[6]
        my_dict['I']-=soln_count[6]
        my_dict.pop('X')

    if 'G' in my_dict:
        soln_count[8]=my_dict['G']
        my_dict['E']-=soln_count[8]
        my_dict['I']-=soln_count[8]
        my_dict['H']-=soln_count[8]
        my_dict['T']-=soln_count[8]
        my_dict.pop('G')

    if 'O' in my_dict and not (my_dict['O']==0):
        soln_count[1]=my_dict['O']
        my_dict['N']-=soln_count[1]
        my_dict['E']-=soln_count[1]

    if 'H' in my_dict and not (my_dict['H']==0):
        soln_count[3]=my_dict['H']
        my_dict['T']-=soln_count[3]
        my_dict['R']-=soln_count[3]
        my_dict['E']-=2*soln_count[3]

    if 'F' in my_dict and not (my_dict['F']==0):
        soln_count[5]=my_dict['F']
        my_dict['I']-=soln_count[5]
        my_dict['V']-=soln_count[5]
        my_dict['E']-=soln_count[5]

    if 'S' in my_dict and not (my_dict['S']==0):
        soln_count[7]=my_dict['S']
        my_dict['E']-=2*soln_count[7]
        my_dict['V']-=soln_count[7]
        my_dict['N']-=soln_count[7]

    if 'I' in my_dict and not (my_dict['I']==0):
        soln_count[9]=my_dict['I']
        my_dict['N']-=2*soln_count[9]
        my_dict['E']-=soln_count[9]
    soln=""
    for i in range(10):
        for count in range(soln_count[i]):
            soln+=str(i)
    print("Case #{}: {}".format(test,soln))
