T = int(input())
for tc in range(1,T+1):
    arr = [0 for _ in range(10)]
    N = int(input())
    masukan = 0
    for i in range(1,101):
        masukan = masukan + N
        for j in str(masukan):
            arr[int(j)] = i
        if not arr.count(0):
            break

    if arr.count(0):
        print("Case #{0}: INSOMNIA".format(tc))
    else:
        print("Case #{0}: {1}".format(tc, masukan))