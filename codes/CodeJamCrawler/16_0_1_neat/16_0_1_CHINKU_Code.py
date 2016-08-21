with open("input.txt") as f:
    f_write = open('output.txt','w')
    test_cases = int(f.readline())
    for i in range(test_cases):
        n = int(f.readline())
        new_number = n
        digits = set([int(j) for j in str(n)])
        insomnia = True
        for k in range(1000000):
            if len(digits) == 10:
                insomnia = False
                f_write.write("Case #"+str(i+1)+": "+str(new_number)+"\n")
                break
            new_number += n
            digits.update([int(j) for j in str(new_number)])
        if insomnia:
            f_write.write("Case #"+str(i+1)+": INSOMNIA\n")
