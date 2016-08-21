def last_num(n):
    if n == 0:
        return None
    visited_digits = set(list(str(n)))
    current_num = n
    while len(visited_digits) != 10:
        current_num += n
        visited_digits.update(list(str(current_num)))
    # all digits found
    return current_num

with open("out_large.txt", "w") as file:
    pass
with open("A-large.in", "r") as file:
    text = file.read()
text = text.splitlines()
tests = int(text[0])
for i in range(1, tests+1):
    #proc
    number = int(text[i])
    sleep = last_num(number)
    # output
    with open("out_large.txt", "a") as file:
        file.write("Case #{}: ".format(i))
        if sleep:
            file.write(str(sleep))
        else:
            file.write("INSOMNIA")
        file.write("\n")
