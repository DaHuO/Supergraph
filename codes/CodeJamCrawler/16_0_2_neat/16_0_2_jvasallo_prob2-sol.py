def flip(pancake_stack):
    if pancake_stack[0] == "+":
        start_smile = 0
        while pancake_stack[start_smile] == "+":
            start_smile += 1
        start_smile -= 1
        return "-" * start_smile + pancake_stack[start_smile+1:]

    # Find the last smile...ignore trailing +++
    last_smile = len(pancake_stack) - 1
    while pancake_stack[last_smile] == "+":
        last_smile -= 1

    # Reverse the stack in one swoop from last smile
    flipped = pancake_stack[:last_smile+1][::-1]
    reverse = ""
    for c in flipped:
        if c == "+":
            reverse += "-"
        else:
            reverse += "+"

    return reverse + pancake_stack[last_smile+1:]

# input() reads a string with a line of input, stripping the '\n'
# (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = str(raw_input())  # read a list of integers, 1 in this case

    # start solution
    flip_count = 0
    while not n == "+" * len(n):
        n = flip(n)
        flip_count += 1
    # end solution

    print("Case #{}: {}".format(i, flip_count))
    # check out .format's specification for more formatting options
