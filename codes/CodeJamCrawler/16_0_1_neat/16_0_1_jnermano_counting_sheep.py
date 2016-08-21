for t in range(1, input()+1):
    n = input()
    numbers = []
    i = 0
    while len(numbers) < 10:
        i += 1
        if n == 0:
            print "Case #{}: INSOMNIA".format(t)
            break
        else:
            xn = i * n
            for x in str(xn):
                if x not in numbers:
                    numbers.append(x)

    if len(numbers) == 10:
        print "Case #{}: {}".format(t, i * n)
        
