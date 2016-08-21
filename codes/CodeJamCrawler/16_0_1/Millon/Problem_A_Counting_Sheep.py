#py3
for T in range(1, int(input())+1):
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    N = int(input())
    count = 1
    while True:
        status = False
        name = str(N*count)
        for s in name:
            if int(s) in d:
                try:
                   d.remove(int(s))
                except ValueError:
                    pass
            if not len(d):
                status = True
        if status:
            print('Case #{0}: {1}'.format(T, name))
            break
        if count >= 100:
            print('Case #{0}: INSOMNIA'.format(T))
            break
        count += 1




# a= [1,2,3]

# print a.remove(5)
# print a
