problem = open("in.in", "r")

cases = int(problem.readline())

k = [0] * cases
c = [0] * cases
s = [0] * cases
for i in range(cases):
    k[i], c[i], s[i] = [int(st) for st in problem.readline().rstrip('\n').split(' ')]

problem.close()

output = "out.out"

out = open(output, "w")

for i in range(1, cases + 1):
    st = "Case #" + str(i) + ": "
    if k[i-1] > s[i-1]:
        out.write(st + "IMPOSSIBLE\n")
    else:
        for j in range(1, s[i-1] + 1):
            st += str(j) + " "
        out.write(st.rstrip(" ") + "\n")

out.close()






#i = 1
#for test in tests:
#    out.write("Case #" + str(i) + ": ")
#    out.write(str(result(test)))
#    out.write("\n")
#    i += 1

#out.close()

