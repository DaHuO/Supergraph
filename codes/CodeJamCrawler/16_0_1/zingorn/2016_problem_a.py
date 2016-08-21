dir = "./"
in_name = dir + "input_1.txt"
# filename = v_dir + "A-small-practice.in"
# filename = v_dir + "A-large-practice.in"

f_in = open(in_name)
out_name = "output_1.txt"
f_out = open(out_name, 'w')

number_of_tests = int(f_in.readline())

test_number = 1

while test_number <= number_of_tests:
    first_number = int(f_in.readline())
    num = 0
    t = []

    while (len(t) < 10 and first_number != 0):
        num += first_number
        t.extend(list(str(num)))   # add digits from new number
        t = list(set(t))                # delete dublicates

    if first_number != 0:
        f_out.write("Case #" + str(test_number) + ": " + str(num) + "\n")
    else:
        f_out.write("Case #" + str(test_number) + ": " + 'INSOMNIA' + "\n")
    test_number += 1
