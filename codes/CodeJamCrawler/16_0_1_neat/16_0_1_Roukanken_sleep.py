def work():
    s = set()
    x = int(input())
    
    res = 0

    for i in range(1, 2000):
        s |= set(str(i*x))

        if len(s) == 10: 
            res = i
            break

    return res*x if res != 0 else "INSOMNIA"

T = int(input())
for test_case in range(T):
    print ("Case #{}:".format(test_case+1), work())