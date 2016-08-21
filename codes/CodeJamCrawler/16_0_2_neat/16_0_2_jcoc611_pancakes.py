cases = int(input())
i = 1

for case in range(cases):
    pancakes = input()
    count = 0

    current = pancakes[0]

    for char in pancakes[1:]:
        if(char != current):
            count += 1
            current = "+" if current == "-" else "-"

    if(current == "-"):
        count += 1

    print("Case #" + str(i) + ": " + str(count))
    i += 1
