file = open('input.in', 'r')
cases = int(file.readline().strip())
for case in range(cases):
    num = [0,1,2,3,4,5,6,7,8,9]
    N = int(file.readline().strip())
    number = N
    if N == 0:
        count = 'INSOMNIA'
    else:
        multi = 1
        while len(num) > 0:
            number = str(N * multi)
            for x in number:
                if int(x) in num:
                    num.remove(int(x))
            number = int(number)
            multi += 1
        count = number
    print("Case #{}: {}".format(case+1, count))
