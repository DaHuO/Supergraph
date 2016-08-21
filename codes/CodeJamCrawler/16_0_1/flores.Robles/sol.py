IN = open("in", 'r')
OUT = open("out", 'w+')

n = IN.readline()

for x in xrange(0, int(n)):
    number = int(IN.readline())
    if number == 0:
        outline = "Case #" + str(x+1) + ": " + "INSOMNIA" + "\n"
    else:
        ans = 0
        aSet = set()
        while len(aSet) < 10:
            ans += 1
            newNumber = ans * number
            number_string = str(newNumber)
            for ch in number_string:
                aSet.add(ch)

        outline = "Case #" + str(x+1) + ": " + str(ans * number) + "\n"
    OUT.write(outline)


# Close opended files
IN.close()
OUT.close()
