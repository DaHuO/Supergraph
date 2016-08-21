#Counting Sheep.
in_f = open("A-large.in")
lines = [int(i.strip("\n")) for i in in_f.readlines()]
tcs = lines[0]

with open("output_large.ot", "w") as out_f:
    for i in range(1, tcs+1):
        if lines[i] == 0:
            out_f.write("Case #%s: INSOMNIA\n"%(i))
        else:
            t = 1
            temp = 0
            cnt = {i:0 for i in range(0,10)}
            while(cnt.values().count(0) != 0):
                temp = t*lines[i]
                for j in str(temp):
                    cnt[int(j)] += 1
                t += 1
            out_f.write("Case #%s: %s\n"%(i, temp))
