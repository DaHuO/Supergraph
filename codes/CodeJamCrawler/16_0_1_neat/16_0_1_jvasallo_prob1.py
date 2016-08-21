# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())  # read a list of integers, 1 in this case

    # start solution
    num_dict = {}
    x = 1
    while len(num_dict) != 10:
        answer = x * n
        for digit in str(answer):
            num_dict[digit] = num_dict.get(digit, 0) + 1
            if num_dict[digit] == 1000000:
                answer = 'INSOMNIA'
                break
        x+=1
        if answer == 'INSOMNIA':
            break
    # end solution

    print("Case #{}: {}".format(i, answer))
    # check out .format's specification for more formatting options
