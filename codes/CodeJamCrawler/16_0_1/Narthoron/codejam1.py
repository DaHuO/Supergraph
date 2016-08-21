x = input()
iterator = 0
#line =  [int(i) for i in input().split()]
for i in range(int(x)):
    iterator = iterator + 1
    num = input()
    if num == '0':
        print("Case #",iterator,": INSOMNIA", sep='')
    else:
        sheeps = []
        k = 1
        while True:
            digits = [int(j) for j in str(k*int(num))]
            sheeps = sheeps + digits
            sheeps = list(set(sheeps))
            if len(sheeps) == 10:
                print("Case #",iterator,": ", k*int(num),sep='')
                break
            else:
                k = k + 1


