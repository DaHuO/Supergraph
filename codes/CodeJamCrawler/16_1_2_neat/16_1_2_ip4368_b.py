from collections import defaultdict

t = int(raw_input())
for i in range(1,t+1):
    n = int(raw_input())
    d = defaultdict(int)
    for j in range(n*2-1):
        temp = raw_input()
        temp_list = [int(a) for a in temp.split()]
        for num in temp_list:
            d[num] += 1
    f_list = []
    for key, value in d.items():
        if value%2:
            f_list.append(key)
    f_list.sort()
    new_list = [str(a) for a in f_list]
    print("Case #"+str(i)+": " + " ".join(new_list))
