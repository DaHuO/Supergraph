targed_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

input_list = []
while True:
    try:
        line = raw_input()
        input_list.append(line)
    except:
        break
input_list.pop(0)
for index in range(0, len(input_list)):

    if int(input_list[index]) == 0:
        print "Case #{}: {}".format(index + 1, "INSOMNIA")
        continue
    current_list = []
    i = 1
    input_copy = str(input_list[index])
    while (set(current_list) != set(targed_list)):
        input_copy = i * int(input_list[index])
        i = i + 1
        for num in str(input_copy):
            if int(num) not in current_list:
                current_list.append(int(num))

    if set(current_list) == set(targed_list):
        print "Case #{}: {}".format(index + 1, input_copy)
