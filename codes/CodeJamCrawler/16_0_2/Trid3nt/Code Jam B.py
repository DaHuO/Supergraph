boo = 0
answers = []

with open('pancakeinput.txt', 'r') as fi:
    for line in fi:
        if boo == 0:
            boo = 1
            continue

        vals = line.split()[0]
        print vals

        while (vals[-1] == '+'):
            vals = vals[:-1] #Remove final plusses
            if len(vals) == 0:
                break

        if (len(vals) == 0):
            answers.append(0)

        elif (len(vals) == 1):
            answers.append(1)

        else:
            count = 1
            i = 1
            while (i < len(vals)):
                if not vals[i] == vals[i-1]:
                    count += 1
                i += 1
            answers.append(count)
    fi.close

val = 1
with open('pancakeoutput.txt', 'a') as fi:
    for answer in answers:
        fi.write('Case #' + str(val) + ': ' + str(answer) + '\n')
        val += 1
    fi.close
