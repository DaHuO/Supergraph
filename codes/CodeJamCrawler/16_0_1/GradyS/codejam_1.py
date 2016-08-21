def readfile(filename):
    textfile = open(filename, 'r')
    text = ''
    while True:
        read = textfile.readline()
        if not read:
            break
        text += read
    return text

def writefile(filename, text):
    textfile = open(filename, 'w')
    textfile.write(text)
    textfile.close()

def count(val):
    digits = [False]*10
    total = 0
    while True:
        total += val
        for i in range(10):
            if str(i) in str(total):
                digits[i] = True
        if False not in digits:
            return total

cases = [case for case in readfile("A-large.in").split("\n")[1:] if case != ""]
output = ""

for case in range(len(cases)):
    output += "Case #" + str(case+1) + ": " + (str(count(int(cases[case]))) if int(cases[case]) else "INSOMNIA") + ("\n" if case != len(cases)-1 else "")

writefile("output.txt", output)
