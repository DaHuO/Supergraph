with open("out_small.txt", "w") as file:
    pass

with open("D-small-attempt1.in", "r") as file:
    text = file.read()

text = text.splitlines()
tests = int(text[0])
for i in range(1, tests+1):
    #proc
    length, complexity, students = \
            [int(x) for x in text[i].split(" ")]
    
    # output
    with open("out_small.txt", "a") as file:
        file.write("Case #{}:".format(i))
        for i in range(1, length+1):
            file.write(" "+str(i))
        file.write("\n")
