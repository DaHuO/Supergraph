def handle_nth_input(n, entry):
    if entry == '0\n':
        return "Case #" + str(n) + ": INSOMNIA\n"
    else:
        count = 1
        num_entry = int(entry)
        seen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        while len(seen) > 0:
            cur_string = str(num_entry * count)
            for i in cur_string:
                seen = [j for j in seen if j != i]
            count += 1
        return "Case #" + str(n) + ": " + cur_string + "\n"


count = 0
results = []
with open("A-large.in") as file:
    for entry in file:
        if (count > 0):
            results.append(handle_nth_input(count, entry))
        count += 1;

with open("out.txt","w") as file:
    for i in results:
        file.write(i)

