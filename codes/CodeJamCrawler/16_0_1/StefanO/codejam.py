# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
infile = open('A-large.in', 'r')
outfile = open('output.txt', 'w')
t = int(infile.readline())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(infile.readline()) # read a list of integers, 2 in this case
    x = [0,0,0,0,0,0,0,0,0,0]
    index = 1
    if (n == 0): outfile.write("Case #{}: INSOMNIA\n".format(i))
    else:
        while(sum(x) != 10):
            multi = n*index
            index += 1
            for letter in str(multi):
                x[int(letter)] = 1
        outfile.write("Case #{}: {}\n".format(i, n*(index-1)))
  # check out .format's specification for more formatting options
