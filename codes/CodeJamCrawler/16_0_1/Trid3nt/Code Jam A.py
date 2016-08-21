boo = 0
answers = []

with open('sheepinput.txt', 'r') as fi:
    for line in fi:
        if boo == 0:
            boo = 1
            continue
        
        vals = int(line.split()[0])
        #print vals
        
        if vals == 0:
            answers.append("INSOMNIA")

        else:
            numbers = set()
            seed = vals
            seedmult = 0
            while (len(numbers) < 10):
                seedmult += seed
                for a in str(seedmult):
                    numbers.add(int(a))
            answers.append(seedmult)
    fi.close

val = 1
with open('sheepoutput.txt', 'a') as fi:
    for answer in answers:
        fi.write('Case #' + str(val) + ': ' + str(answer) + '\n')
        val += 1
    fi.close
