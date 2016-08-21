
with open('B-large.in') as inpF:
    cases = int(inpF.readline())
    results = []
    for i in range(cases):
        pancake_stack = reversed(list(inpF.readline()))
        flips = 0
        prev_pancake = ''
        for pancake in pancake_stack:
            if pancake == '-':
                if prev_pancake != '-':
                    flips += 2
            prev_pancake = pancake

        if prev_pancake == '-':
            flips -= 1
        results.append(flips)

    with open('o1', 'w+') as outF:
        for result in range(len(results)):
            outF.write("Case #{0}: {1}\n".format(result + 1, results[result]))



