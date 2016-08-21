file_name = "A-large"

input_file = file_name + ".in"

result_str = ""

File = open(input_file, "r")  # Open file for read

T = int(File.readline())  # Reads First Line: N - Number of Test Cases

for i in range(T):

    S = File.readline()  # L: List of Words
    S = S.strip()  # Removes the EOL character

    digits = ""

    # Zeroes
    flag = True
    zero = S[:]
    while flag:
        z = zero.find("Z")
        e = zero.find("E")
        r = zero.find("R")
        o = zero.find("O")
        if z != -1 and e != -1 and r != -1 and o != -1:
            zero = zero.replace("Z", "", 1)
            zero = zero.replace("E", "", 1)
            zero = zero.replace("R", "", 1)
            zero = zero.replace("O", "", 1)
            S = zero[:]
            digits += "0 "
        else:
            flag = False

    # Twos
    flag = True
    two = S[:]
    while flag:
        t = two.find("T")
        w = two.find("W")
        o = two.find("O")
        if t != -1 and w != -1 and o != -1:
            two = two.replace("T", "", 1)
            two = two.replace("W", "", 1)
            two = two.replace("O", "", 1)
            S = two[:]
            digits += "2 "
        else:
            flag = False

    # Fours
    flag = True
    four = S[:]
    while flag:
        f = four.find("F")
        o = four.find("O")
        u = four.find("U")
        r = four.find("R")
        if f != -1 and o != -1 and u != -1 and r != -1:
            four = four.replace("F", "", 1)
            four = four.replace("O", "", 1)
            four = four.replace("U", "", 1)
            four = four.replace("R", "", 1)
            S = four[:]
            digits += "4 "
        else:
            flag = False

    # Threes
    flag = True
    three = S[:]
    while flag:
        t = three.find("T")
        h = three.find("H")
        r = three.find("R")
        e = three.count("E")
        if t != -1 and h != -1 and r != -1 and e > 1:
            three = three.replace("T", "", 1)
            three = three.replace("H", "", 1)
            three = three.replace("R", "", 1)
            three = three.replace("E", "", 2)
            S = three[:]
            digits += "3 "
        else:
            flag = False

    # Fives
    flag = True
    five = S[:]
    while flag:
        f = five.find("F")
        I = five.find("I")
        v = five.find("V")
        e = five.find("E")
        if f != -1 and I != -1 and v != -1 and e != -1:
            five = five.replace("F", "", 1)
            five = five.replace("I", "", 1)
            five = five.replace("V", "", 1)
            five = five.replace("E", "", 1)
            S = five[:]
            digits += "5 "
        else:
            flag = False

    # Sixes
    flag = True
    six = S[:]
    while flag:
        s = six.find("S")
        I = six.find("I")
        x = six.find("X")
        if s != -1 and I != -1 and x != -1:
            six = six.replace("S", "", 1)
            six = six.replace("I", "", 1)
            six = six.replace("X", "", 1)
            S = six[:]
            digits += "6 "
        else:
            flag = False

    # Sevens
    flag = True
    seven = S[:]
    while flag:
        s = seven.find("S")
        e = seven.count("E")
        v = seven.find("V")
        n = seven.find("N")
        if s != -1 and v != -1 and n != -1 and e > 1:
            seven = seven.replace("S", "", 1)
            seven = seven.replace("E", "", 2)
            seven = seven.replace("V", "", 1)
            seven = seven.replace("N", "", 1)
            S = seven[:]
            digits += "7 "
        else:
            flag = False

    # Eights
    flag = True
    eight = S[:]
    while flag:
        e = eight.find("E")
        I = eight.find("I")
        g = eight.find("G")
        h = eight.find("H")
        t = eight.find("T")
        if e != -1 and I != -1 and g != -1 and h != -1 and t != -1:
            eight = eight.replace("E", "", 1)
            eight = eight.replace("I", "", 1)
            eight = eight.replace("G", "", 1)
            eight = eight.replace("H", "", 1)
            eight = eight.replace("T", "", 1)
            S = eight[:]
            digits += "8 "
        else:
            flag = False

    # Ones
    flag = True
    one = S[:]
    while flag:
        o = one.find("O")
        n = one.find("N")
        e = one.find("E")
        if o != -1 and n != -1 and e != -1:
            one = one.replace("O", "", 1)
            one = one.replace("N", "", 1)
            one = one.replace("E", "", 1)
            S = one[:]
            digits += "1 "
        else:
            flag = False

    # Nines
    flag = True
    nine = S[:]
    while flag:
        n = nine.count("N")
        I = nine.find("I")
        e = nine.find("E")
        if I != -1 and e != -1 and n > 1:
            nine = nine.replace("N", "", 2)
            nine = nine.replace("I", "", 1)
            nine = nine.replace("E", "", 1)
            S = nine[:]
            digits += "9 "
        else:
            flag = False

    # print "Case #" + str(i+1) + ": " + digits

    digits = digits[:-1]
    l_digits = digits.split()
    l_digits.sort()
    # print l_digits
    digits = "".join(l_digits)

    result_str += "Case #" + str(i + 1) + ": " + digits + "\n"

File.close()  # Close file

result_str = result_str[:-1]  # Removes the last EOL

# Output
output_file = file_name + ".out"

File = open(output_file, "w")  # Open file for write

File.write(result_str)

File.close()  # Close file