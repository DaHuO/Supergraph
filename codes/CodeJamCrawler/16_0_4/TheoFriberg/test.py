with open("/tmp/input.txt", "r") as f:
    i = 0
    for line in f:
        if i != 0:
            print("Case #"+str(i)+": "+" ".join([str(x) for x in list(range(1,int(line.split(" ")[0])+1))]))
        i = i + 1
