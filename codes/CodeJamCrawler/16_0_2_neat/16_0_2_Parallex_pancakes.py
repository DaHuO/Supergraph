def flip_num(seq):
    happy_sad = [x == "+" for x in seq]
    count = 0
    index = -1
    length = len(seq)
    while index != -length - 1:
        if not happy_sad[index]:
            count += 1
            happy_sad[index] = True
            for index2, higher_pancake in enumerate(happy_sad[:index]):
                happy_sad[index2] = not higher_pancake
        index -= 1
    return count

with open("out_large.txt", "w") as file:
    pass

with open("B-large.in", "r") as file:
    text = file.read()

text = text.splitlines()
tests = int(text[0])
for i in range(1, tests+1):
    #proc
    sequence = text[i]
    flips = flip_num(sequence)
    # output
    with open("out_large.txt", "a") as file:
        file.write("Case #{}: ".format(i))
        file.write(str(flips))
        file.write("\n")
