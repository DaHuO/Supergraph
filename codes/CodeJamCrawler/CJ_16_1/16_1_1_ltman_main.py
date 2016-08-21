def reverse_alpha(string):
    start = string[0]
    answer = ""
    for char in string:
        if char >= start:
            answer = char + answer
            start = char
        else:
            answer = answer + char
    answers.append(answer)

answers = []

with open('input.in') as input_file:
    cases = int(input_file.readline())
    for i in range(cases):
        word = input_file.readline()
        reverse_alpha(word)

with open('output.txt', 'w') as output_file:
    for i in range(cases):
        # if i != cases:
        #     output = "Case #{}: {}\n".format(i, answers[i])
        #     output_file.write(output)
        # else:
        output = "Case #{}: {}".format(i + 1, answers[i])
        output_file.write(output)

