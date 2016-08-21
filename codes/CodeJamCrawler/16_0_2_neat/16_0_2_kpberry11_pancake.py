def handle_nth_input(n, entry):
    r_entry = [i for i in entry[::-1]]
    count = 0
    for i in range(len(r_entry)):
        if r_entry[i] == '-':
            count += 1
            for j in range(i, len(r_entry)):
                if r_entry[j] == '+':
                    r_entry[j] = '-'
                elif r_entry[j] == '-':
                    r_entry[j] = '+'
    return "Case #" + str(n) + ": " + str(count) + "\n"

count = 0
results = []
with open("B-large.in") as file:
    for entry in file:
        if (count > 0):
            results.append(handle_nth_input(count, entry))
        count += 1;

with open("out.txt","w") as file:
    for i in results:
        file.write(i)
