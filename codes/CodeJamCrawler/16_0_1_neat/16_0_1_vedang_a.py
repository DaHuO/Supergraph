t = int(input())

for i in range(1, t + 1):
    st = set()
    n = int(input())
    if not n:
        print("Case #{}: INSOMNIA".format(i))
        continue
    j = 1
    while len(st) != 10:
        r = j * n
        j += 1
        st.update(set(list(str(r))))
    print("Case #{}: {}".format(i, r))
