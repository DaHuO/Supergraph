
def case_(start_num):

    if start_num == 0:
        return "INSOMNIA"

    final_data = set()

    for digit in str(start_num):
            final_data.add(digit)

    for i in range(1, 100):
        start_num_temp = i * start_num

        for digit in str(start_num_temp):
            final_data.add(digit)

        if len(final_data) == 10:
            return start_num_temp

    return "INSOMNIA"

with open("A-large.in", "r") as data, open("output.in", "w")as data1:
    count = 0

    p = data.readline()
    offsets = range(2, int(p))

    for i in data:
        count += 1
        ans = case_(int(i))
        data1.write("Case #{}: {}\n" .format(count, ans))
