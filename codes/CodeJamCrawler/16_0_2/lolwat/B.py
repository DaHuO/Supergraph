n = int(raw_input())
for i in range(1, n + 1):
    pancakes = raw_input()
    current = pancakes[0]
    count = 0
    for j in range(1, len(pancakes)):
        if current != pancakes[j]:
            count += 1
            current = pancakes[j]
    if current != "+":
        count += 1
    print "Case #" + str(i) + ":", count