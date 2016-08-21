with open('filename') as f:
    lines = f.readlines()

test_cases = lines[0]

for i in range (1, len(lines)):
    string = lines[i]
    current_letter = string[0]
    solution = string[0]
    for t in range(1, len(string)) :
        if string[t] >= current_letter:
            new_solution = string[t] + solution
            solution = new_solution
            current_letter = solution[0]
        else:
            new_solution = solution + string[t]
            solution = new_solution
    print "Case #%d: "%i  + str(solution),
