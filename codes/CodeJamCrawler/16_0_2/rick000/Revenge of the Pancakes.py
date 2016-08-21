file_name_fix = "B-large"
file_name = file_name_fix + ".in"

result_str = ""

File = open(file_name, "r")  # Open file for read

T = int(File.readline())  # Reads First Line: T - Number of Test Cases

for i in range(T):

    S = File.readline()  # N: Stack of pancakes
    S = S.replace("\n", "")  # Removes the EOL character
    length = len(S)
    happy = False

    moves = 0

    while not happy:

        first_dash_index = S.find("-")

        # If there are no '-', it means there are only '+'
        # So, no move is needed
        if first_dash_index == -1:
            happy = True
            break

        # If there are no '+', it means there are only '-'
        # So, it is needed just one more flip
        if S.find("+") == -1:
            moves += 1
            happy = True
            break

        first_dashplus_index = S.find("-+")  # Finds the first appearance of the sequence '-+'
        first_plusdash_index = S.find("+-")  # Finds the first appearance of the sequence '+-'

        # print 'S: ' + S
        # print 'caso ' + str(i + 1) + ', first_dashplus_index = ' + str(first_dashplus_index) + ', first_plusdash_index = ' + str(first_plusdash_index)

        # Determines which sequence appears first (taking into account that one of them could not appear at all)
        if first_plusdash_index == -1:
            flip_until = first_dashplus_index
        elif first_dashplus_index == -1:
            flip_until = first_plusdash_index
        elif first_dashplus_index < first_plusdash_index:
            flip_until = first_dashplus_index
        elif first_plusdash_index < first_dashplus_index:
            flip_until = first_plusdash_index

        # Gets the string to be flipped
        str_to_flip = S[:flip_until + 1]

        # Reverses the string
        str_flipped = str_to_flip[::-1]

        # Changes the '+' for '-', and the '-' for '+'
        for j in range(len(str_flipped)):
            if str_flipped[j] == "+":
                str_flipped = str_flipped[:j] + "-" + str_flipped[j + 1:]
            elif str_flipped[j] == "-":
                str_flipped = str_flipped[:j] + "+" + str_flipped[j + 1:]

        # Reorganizes the stack of pancakes
        S = str_flipped + S[flip_until + 1:]

        moves += 1

    result_str += "Case #" + str(i + 1) + ": " + str(moves) + "\n"

File.close()  # Close file

result_str = result_str[:-1]  # Removes the last EOL

# Output
output_file = file_name_fix + ".out"

File = open(output_file, "w")  # Open file for write

File.write(result_str)

File.close()  # Close file