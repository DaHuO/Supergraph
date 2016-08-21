import itertools

file_name = "A-small-attempt2"


def read_file():
    with open(file_name+".in", "r") as f:
        return map(str.strip, f.readlines(int(f.readline())))


def write(lines):
    with open(file_name+".out", "w") as out:
        for index, answer in enumerate(lines):
            out.write("Case #"+str(index+1)+": "+str(answer)+"\n")


def order_string(string):
    current_char = string[0]
    builder = ""
    for char in string:
        if char >= current_char:
            current_char = char
            builder = char + builder
        else:
            builder += char
    return builder


write(map(order_string, read_file()))