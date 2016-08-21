boo = 0
answers = []

with open('lastwordinput.txt', 'r') as fi:
    for line in fi:
        if boo == 0:
            boo = 1
            continue
        
        vals = str(line.split()[0])
        #print vals
        
        lastword = str(vals[0])
        vals = vals[1:]

        for letter in vals:
            if letter >= lastword[0]:
                lastword = str(letter) + lastword
            else:
                lastword = lastword + str(letter)

        answers.append(lastword)
        
    fi.close

val = 1
with open('lastwordoutput.txt', 'a') as fi:
    for answer in answers:
        fi.write('Case #' + str(val) + ': ' + str(answer) + '\n')
        val += 1
    fi.close
