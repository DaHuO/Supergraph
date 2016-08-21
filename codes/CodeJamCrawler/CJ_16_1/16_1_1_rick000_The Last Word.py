file_name = "A-large"

input_file = file_name + ".in"

result_str = ""

File = open(input_file, "r")  # Open file for read

T = int(File.readline())  # Reads First Line: N - Number of Test Cases

for i in range(T):

    S = File.readline()  # L: List of Words
    S = S.replace("\n", "")  # Removes the EOL character

    last_word = S[0]

    for l in range(1, len(S)):

        if S[l] < last_word[0]:
            last_word = last_word + S[l]
        else:
            last_word = S[l] + last_word

    # print "Case #" + str(i+1) + ": " + R

    result_str += "Case #" + str(i + 1) + ": " + last_word + "\n"

File.close()  # Close file

result_str = result_str[:-1]  # Removes the last EOL

# Output
output_file = file_name + ".out"

File = open(output_file, "w")  # Open file for write

File.write(result_str)

File.close()  # Close file