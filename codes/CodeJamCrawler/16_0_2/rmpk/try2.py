def reversedigit(z,i):
    for j in range(i+1):
        if z[j]==1:
            z[j]=0
        elif z[j]==0:
            z[j]=1
    return z

def mainfunc():
    x = file.readline()
    x = x.strip()
    z = [i for i in str(x)]
    y = [w.replace('+', '1') for w in z]
    lo = [w.replace('-', '0') for w in y]
    z = [int(i) for i in lo]

    count = 0
    for i in range(len(z)-1):
        if z[i]!=z[i+1]:
            count+=1
            z = reversedigit(z,i)

    count = count+1        
    if z[0] == 0:
        number = count
    elif z[0]==1:
        number = count-1
    
    return number
        
file = open('B-large.in.txt', 'r')
file1 = open("Output.txt", "w")
times = int(file.readline())
for i in range(times):
    number = mainfunc()
    file1.write('Case #{}: {}\n'.format(i+1,number))
    print('Case #{}: {}'.format(i+1,number))
file1.close()
file.close()