output = open("output.txt", "w")
input =  open("D-small-attempt2.in", "r")
next(input)
n = 1
for line in input:
    k,c, s = (int(x) for x in line.split())
    output.write("Case #" + str(n) + ":")   
    for i in range (1, k+1):
        output.write(' ' + str(i))
    output.write("\n");
    n += 1
input.close()
output.close()
