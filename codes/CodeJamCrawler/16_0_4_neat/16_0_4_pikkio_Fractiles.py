input_file = open("D-small-attempt0.in", "r")
output_file = open("results.txt", "w+")

T = int(input_file.readline())

for i in range(0, T):
    line = input_file.readline()
    (K, C, S) = line.split()
    K = int(K)
    C = int(C)
    S = int(S)
    
    # will remove this limitation for large dataset
    assert(K == S)
    
    pos = 1
    inc = pow(K, C-1)
    positions_str = "" 
    for j in range(S):
        positions_str += str(pos) + " "
        pos += inc
    
    positions_str = positions_str[:-1]
    
    output_file.write("Case #" + str(i+1) + ": " + positions_str + "\n")

input_file.close()
output_file.close()
