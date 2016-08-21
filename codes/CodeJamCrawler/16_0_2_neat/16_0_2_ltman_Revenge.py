def optimal_flips(string):

    flips = 0
    string = list(string)
    while '-' in string:
        for x in range(len(string) - 1, -1, -1):
            if string[x] == '-':
                for y in range(0, x + 1):
                    if string[y] == '-':
                        string[y] = '+'
                    elif string[y] == '+':
                        string[y] = '-'
                flips += 1
    return flips

with open("B-large.in", 'r') as input_file:
    cases = input_file.readline()
    with open("output.txt", 'w') as output_file:
        pancakes = input_file.readlines()
        for n in range(len(pancakes)):
            count = optimal_flips(pancakes[n])
            output_file.write("Case #{}: {}\n".format(n + 1, count))
