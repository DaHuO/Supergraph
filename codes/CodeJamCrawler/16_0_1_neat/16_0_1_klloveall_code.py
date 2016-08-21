input_file = open("input.txt")
output = open("output.txt", "w")

n = int(input_file.readline())

for i in range(1, n + 1):
    num = int(input_file.readline())
    if num == 0:
        output.write("Case #" + str(i) + ": INSOMNIA" + "\n")
        continue

    havent_seen = set()
    for j in range(0, 10):
        havent_seen.add(str(j))

    current_multiple = 0
    while len(havent_seen) > 0:
        current_multiple += 1
        print(str(num) + " " + str(havent_seen))
        temp_num = num * current_multiple
        for char in str(temp_num):
            if char in havent_seen:
                havent_seen.remove(char)

    output.write("Case #" + str(i) + ": " + str(num * current_multiple) + "\n")
