def flip(value):
    i = len(value) - 1
    count_minus = 0
    count_plus = 0
    while value[i] != "+" and i >= 0:
        count_minus += 1
        i -= 1

    j = 0
    while value[j] != "-" and j < len(value):
        count_plus += 1
        j += 1

    number_of_flips = 0
    if count_plus > 0:
        number_of_flips += 1
        for i in range(0,count_plus):
            value[i] = "-"
    if count_minus > 0:
        number_of_flips += 1
        value.reverse()
        for i in range(0,len(value)):
            if value[i] == "+":
                value[i] = "-"
            else:
                value[i] = "+"

    return [number_of_flips, "".join(value)]



def solve(value):
    done = "+"*len(value)
    flips = 0
    high_index = len(value)
    while value != done and high_index >= 0:
        sub_value = value[0:(high_index)]
        number_of_flips, fliped_snippet = flip(list(sub_value))
        value = fliped_snippet+value[high_index:]
        flips += number_of_flips
        while high_index > 0 and value[high_index-1] == "+":
            high_index -= 1


    return str(flips)



def main():
    input_file = open('B-large.in', 'r')
    output_file = open('B-large.out', 'w')
    number_of_cases = int(input_file.readline().strip())
    for i in range(1,number_of_cases+1):
        value = input_file.readline().strip()
        result = solve(value)
        output_file.write("Case #"+str(i)+": " + result + "\n")

    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()