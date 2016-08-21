

def do_print(case, positions):
    out.write("Case #{0}:".format(case))
    for i in positions:
        out.write(" {0}".format(i))
    out.write("\n")

def calc_position(K, C, positions):
    if len(positions) != C:
        print("WARNING")
        for _ in range(C-len(positions)):
            positions.append(0)

    x = list(reversed(range(C)))
    ret = 1
    for i in range(C):
        ret = ret + (K**x[i])*positions[i]
    # print("RET: {}".format(ret))
    return ret


f = open("D-large.in")
out = open("out.txt", "w")
T = int(f.readline())
print(T)

for i in range(T):
    K,C,S = map(int, f.readline().split())
    print("kcs {0},{1},{2}".format(K,C,S))
    # if S >= K:
    #     do_print(i+1, [p+1 for p in range(S)])
    #     continue
    if C*S >= K:
        pos_list = []
        pos = []
        for p in range(K):
            pos.append(p)
            if len(pos) == C:
                pos_list.append(calc_position(K, C, pos))
                pos = []
        # print("POS: {}".format(pos))
        if len(pos) != 0:
            pos_list.append(calc_position(K, C, pos))
        do_print(i+1, pos_list)
        continue
    out.write("Case #{0}: {1}\n".format(i+1, "IMPOSSIBLE"))
