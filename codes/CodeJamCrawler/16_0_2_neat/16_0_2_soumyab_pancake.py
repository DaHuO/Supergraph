T = int(raw_input())

for i in range(T):
    pancakes = str(raw_input())
    num_flips = 0

    pancakes = pancakes.split('+')

    if len(pancakes[0]) > 0:
        num_flips += 1

    for stream in pancakes[1:]:
        if len(stream) > 0:
            num_flips += 2

    print ("Case #{0}: {1}".format(i+1, num_flips))
