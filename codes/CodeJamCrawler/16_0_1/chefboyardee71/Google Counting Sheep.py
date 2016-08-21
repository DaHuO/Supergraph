f = open('Google Counting Sheep Large.in','r')
g = open('Google Counting Sheep Large.out','w')

def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

def count_digits(n):
    if n == 0:
        return 'INSOMNIA'
    remaining = 10
    d = {}
    k = n
    answer = 0
    for i in range(100):
        s = list(str(k))
        for j in s:
            if not d.get(j):
                d[j] = True
                remaining -= 1
                if remaining == 0:
                    answer = i
                    break
        if answer:
            break
        k += n
    if answer == 0:
        return 'INSOMNIA'
    else:
        return n*(answer+1)

cases = int(f.readline())
answers = []
for i in range(cases):
    answers.append(count_digits(int(f.readline())))
Google_print(g,answers)
f.close()
g.close()


        
                    
                
