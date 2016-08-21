def solver(n):
    if n == 0:
        return "INSOMNIA"
    numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = 0
    mult = 1

    while counter < 10:
        aux = n*mult
        while aux >= 10:
            l = aux % 10
            if numbers[l] == 0:
                numbers[l] = 1
                counter += 1
            aux = aux//10
        if numbers[aux] == 0:
            numbers[aux] = 1
            counter += 1
        mult += 1

    return n*(mult-1)

with open("output.txt", 'w') as f:
    cases = int(input())
    for i in range(cases):
        n = int(input())
        print("Case #{}: {}".format(i+1, solver(n)), file=f)