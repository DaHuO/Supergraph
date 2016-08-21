with open("A-large.in", "r") as test_file:
    line_count = 0

    for line in test_file:
        if line_count == 0:
            T = line

        if line_count > 0:
            if int(line) == 0:
                with open("large_output.txt", "a") as output:
                    output.write("Case #{}: INSOMNIA\n".format(line_count))
            else:
                N = int(line)
                digits_list = range(0, 10)
                product = 1
                i = 1

                while(len(digits_list) is not 0):
                    product = N * i

                    product_string = str(product)

                    for char in product_string:
                        if int(char) in digits_list:
                            digits_list.remove(int(char))

                    i += 1
                else:
                    with open("large_output.txt", "a") as output:
                        output.write("Case #{}: {}\n".format(line_count,
                                                           str(product)))

        line_count += 1
        