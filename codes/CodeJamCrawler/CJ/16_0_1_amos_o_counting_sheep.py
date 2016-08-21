with open("A-large.in", "r") as text:
    line_count = 0

    for line in text:
        if line_count == 0:
            T = line

        if line_count > 0:
            if int(line) == 0:
                with open("output.txt", "a") as output:
                    output.write("Case #{}: INSOMNIA\n".format(line_count))
            else:
                number = int(line)
                seen_list = set(list(str(number)))
                current_multiple = 0
                current_multiplier = 2

                while(len(seen_list) < 10):
                    current_multiple = number * current_multiplier

                    temp = str(current_multiple)

                    for char in temp:
                        if char not in seen_list:
                            seen_list.add(char)

                    current_multiplier += 1
                else:
                    with open("output.txt", "a") as output:
                        output.write("Case #{}: {}\n".format(line_count,
                                                           str(current_multiple)))

        line_count += 1
