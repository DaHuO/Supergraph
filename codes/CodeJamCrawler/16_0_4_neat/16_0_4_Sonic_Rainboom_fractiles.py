import sys


    
in_file = open("D-small-attempt0.in", 'r')
out_file = open("output.txt", 'w')

size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline().strip().split(" ")
    K = int(line[0])
    C = int(line[1])
    S = int(line[2])

    choices = ""
    for i in range(1, K + 1):
        choices += str(i) + " "
        
    answer = "Case #" + str(case) + ": " + choices + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()


'''
strings = ["LLLL", "LLLG", "LLGL", "LGLL", "GLLL", "LLGG", "LGLG", "GLLG", "LGGL", "GLGL", "GGLL", "LGGG", "GLGG", "GGLG", "GGGL", "GGGG"]
print len(strings)

for string in strings:
    for char in string:
        if char == 'L':
            sys.stdout.write(string)
        else:
            sys.stdout.write("GGGG")
    sys.stdout.write("\n")

'''
'''
strings = ["LLL", "LLG", "LGL", "GLL", "LGG", "GLG", "GGL", "GGG"]

print len(strings)

for string in strings:
    new = ""
    for char in string:
        if char == 'L':
            new += string
        else:
            new += "GGG"

    final = ""
    for char in new:
        if char == 'L':
            final += string
        else:
            final += "GGG"
    final += "\n"
    final = string + " --> " + new + " --> " + final
    sys.stdout.write(final)


def gen_fractiles(K, C):
    pass
'''
