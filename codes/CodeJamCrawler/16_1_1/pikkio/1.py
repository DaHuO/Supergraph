input_file = open("A-large.in", "r")
output_file = open("results.txt", "w+")

T = int(input_file.readline())

for i in range(0, T):
    S = input_file.readline()
    
    S_out = S[:1]
    for a in S[1:]:
        if a >= S_out[0]:
            S_out = a + S_out
        else:
            S_out = S_out + a
            
    output_file.write("Case #" + str(i+1) + ": " + S_out)
    i += 1

input_file.close()
output_file.close()
