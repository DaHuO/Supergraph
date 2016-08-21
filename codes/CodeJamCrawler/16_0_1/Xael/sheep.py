fi = open('A-large.in', 'r')
fo = open('output.txt', 'w')

T = int(fi.readline())

for t in range(T):
    N = int(fi.readline())
    r = N
    arr = [False] * 10
    
    if (N == 0):
        fo.write('Case #{0}: INSOMNIA\n'.format(t+1))
    else:
        i = 1
        
        while i > 0:
            r = i * N
            r_string = str(r)
            for ch in r_string:
                arr[int(ch)] = True
            if arr == ([True] * 10):
                break
            i += 1

        fo.write('Case #{0}: {1}\n'.format(t+1, str(r)))
        
    print(N)

fi.close()
fo.close()
