
input_file = open("A-large.in")
count = input_file.readline()
case = 0
output_file = open("counting_sheep_result.txt", "w")
for number in input_file:
    case += 1
    number = number.strip()
    n = 0
    a = set()
    if number == "0":
        #print("Case #{!s}:".format(case), "INSOMNIA")
        output_file.write("Case #{!s}: ".format(case))
        output_file.write("INSOMNIA" + "\n")
        continue

    while len(a) != 10:
        n += 1
        p = int(number) * n
        for j in str(p):
            a.add(j)
    output_file.write("Case #{!s}: ".format(case))
    output_file.write(str(p) + "\n")
   # print("Case #{!s}:".format(case), p)
