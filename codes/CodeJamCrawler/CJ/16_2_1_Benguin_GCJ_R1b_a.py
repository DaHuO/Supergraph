def sol(s):
     counts = dict((letter,s.count(letter)) for letter in set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
     print(counts)
     number = {n : 0 for n in range(0,10)}
     number[0] = counts['Z']
     number[2] = counts['W']
     number[4] = counts['U']
     number[6] = counts['X']
     number[8] = counts['G']
     number[7] = counts['S'] - number[6]
     number[3] = counts['T'] - number[2] - number[8]
     number[5] = counts['F'] - number[4]
     number[1] = counts['O'] - number[0] - number[2] - number[4]
     number[9] = int((counts['N'] - number[1] - number[7])/2)

     s = ""
     for i in range(0,10):
         s += str(i)*number[i]
     print(s)
     return s



fIn = open('input.txt', 'r')
fOut = open('output.txt', 'w')
case = 0
for line in fIn:
    print(case)
    if case > 0:
        fOut.write("Case #"+str(case)+": "+sol(line)+"\n")
    case += 1