file_name_fix = "A-large"
file_name = file_name_fix + ".in"

result_str = ""

File = open(file_name, "r")  # Open file for read

T = int(File.readline())  # Reads First Line: T - Number of Test Cases

for i in range(T):

    N = File.readline()  # N: Number named
    N = N.replace("\n", "")  # Removes the EOL character
    n = int(N)
    flag = True

    if n == 0:

        result_str += "Case #" + str(i + 1) + ": INSOMNIA\n"
        continue

    digits_seen = ""

    j = 0
    while flag:

        j += 1
        m = j * n
        M = str(m)

        for k in range(len(M)):

            if digits_seen.find(M[k]) == -1:
                digits_seen += M[k]

            if len(digits_seen) == 10:
                flag = False
                break

    result_str += "Case #" + str(i + 1) + ": " + str(m) + "\n"

File.close()  # Close file

result_str = result_str[:-1]  # Removes the last EOL

# Output
output_file = file_name_fix + ".out"

File = open(output_file, "w")  # Open file for write

File.write(result_str)

File.close()  # Close file