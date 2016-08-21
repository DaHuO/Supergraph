
def solution(val):
    count = 1
    dict_ = {i:0 for i in range(0,10)}
    while val:
        temp_val = val * count
        count += 1
        temp = list(str(temp_val))
        for i in temp:
            if int(i) in dict_:
                dict_[int(i)] = 1
        if sum(dict_.values()) == 10:
            return temp_val
    return -1


out = open("output_file.txt","w")
file_in = []
with open("A-large.in",'r') as inp:
    for n in inp:
        file_in.append(int(n))
for i, val in enumerate(file_in[1:]):
    ans = solution(val)
    if ans == -1:
        out.write("Case #" + str(i+1) + ": " + "INSOMNIA\n")
    else:
        out.write("Case #" + str(i+1) + ": " + str(ans) + "\n")

inp.close()
out.close()