x = int(input())
ref = [1 for i in range(10)]
for i in range(x):
    arr = [-1 for j in range(10)]
    num = int(input())
    if num == 0:
        st = "Case #" + str(i+1) + ": INSOMNIA"
        print(st)
    else:
        count = 1
        while True:
            cur = str(num * count)
            for j in cur:
                arr[int(j)] = 1
            if arr == ref:
                print("Case #" + str(i+1) + ": " + str(num*count))
                break
            else:
                count += 1
                
