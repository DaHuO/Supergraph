infile = open('input.in','r')
outfile = open('output.out','w')

T = int(infile.readline())

def finished(arr):
    for i in range (0,10):
        if not arr[i]:
            return False
    return True

for t in range(T):
    N = int(infile.readline())
    arr = []
    for i in range(10):
        arr.append(False)
    i = 1
    if N != 0:
        while not finished(arr):
            strnum = str(N*i)
            for c in strnum:
                arr[int(c)] = True
            i += 1
    print((i-1)*N)
    outfile.write("Case  #" + str(t+1) + ": ")
    if N == 0:
        outfile.write("INSOMNIA\n")
    else:
        outfile.write(str((i-1)*N) + "\n")

infile.close()
outfile.close()