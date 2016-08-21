import sys


input_data = open(sys.argv[1])
filename = ".".join(sys.argv[1].split(".")[:-1])
def readline():
    return input_data.readline().rstrip()

output_data = open(filename + ".out","w")

num_tests = int(readline())


# for i in range(1):
for test_ind in range(1,num_tests+1):
    coders, jammers = readline().split(" ")
    res_coders = [sym for sym in coders]
    res_jammers = [sym for sym in jammers]
    sol = []
    def check_if_better():
        c_score = int("".join(res_coders))
        j_score = int("".join(res_jammers))
        cur_diff = abs(c_score-j_score)
        global sol
        if len(sol)==0:
            sol = (c_score, j_score, cur_diff)
        if sol[2] < cur_diff:
            return
        if sol[2] > cur_diff:
            sol = (c_score, j_score, cur_diff)
            return
        if c_score < sol[0]:
            sol = (c_score, j_score, cur_diff)
            return
        if c_score==sol[0]  and j_score < sol[1]:
            sol = (c_score, j_score, cur_diff)
            return sol


    broken = []
    def traverse(cur):
        team, ind = broken[cur]
        for digit in range(10):
            if team=='c':
                res_coders[ind] = str(digit)
            if team=='j':
                res_jammers[ind] = str(digit)
            if cur==len(broken)-1:
                check_if_better()
            else:
                traverse(cur+1)

    length = len(coders)
    for i, sym in enumerate(coders):
        if sym=='?':
            broken.append(('c',i))
    for i, sym in enumerate(jammers):
        if sym=='?':
            broken.append(('j',i))

    traverse(0)
    def pad(num):
        val = str(num)
        padding = length - len(val)
        return ''.join(['0' for _ in range(padding)]) + val
    output_data.write("Case #%s: %s %s\n" % (test_ind, pad(sol[0]), pad(sol[1])))