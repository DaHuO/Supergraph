def sol_print(value):
    sol_print.line_number += 1;
    print "Case #%d: %s"%(sol_print.line_number, value)
sol_print.line_number = 0

T = int(raw_input())
inputs = []
for i in range(T):
    inputs.append(map(int, raw_input().split()))

for case in inputs:
    K = case[0]
    C = case[1]
    S = case[2]
    result = ""
    for to_clean in range(1, K):
        result += str(to_clean) + " "
    result += str(K)

    sol_print(result)