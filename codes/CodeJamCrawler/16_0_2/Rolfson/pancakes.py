f = open('small.in')
out = open('small.out', 'w')
num_cases = int(f.readline())
plus = False
counter = 0
for x in range(num_cases):
    counter = 0
    plus = False
    line = f.readline()
    for char in line[::-1]:
        if char=='-' and plus == False:
            counter = counter+1
            plus = True
        if char=='+' and plus == True:
            counter = counter+1
            plus = False
    out.write("Case #" + `x+1` + ": " + `counter` + "\n")