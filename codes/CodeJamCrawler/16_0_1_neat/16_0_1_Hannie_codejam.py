ip = open("A-large.in", 'r')
op = open("output.txt", "w")

num_cases = ip.readline()
num_cases = int(num_cases)
values = ip.readlines()

for x in range(num_cases):
    N = int(values[x].rstrip('\n'))
    seen_numbers = []
    last_num = 0
    i = 0
    if N == 0:
        last_num = "INSOMNIA"
    else:
        while len(seen_numbers) < 10:
            curr_num = (i+1)*N
            list_curr_num = (list(str(curr_num)))
            for each in range(len(list_curr_num)):
                if list_curr_num[each] not in seen_numbers:
                    seen_numbers.append(list_curr_num[each])
                else:
                    pass
            last_num = curr_num
            i += 1
    op.write("Case #" + str(x+1) +": " + str(last_num) + "\n")
ip.close()
op.close()
