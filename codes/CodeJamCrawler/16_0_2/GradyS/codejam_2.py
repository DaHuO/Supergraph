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

def flips(string):
    string += "+"
    groups = 0
    for char in range(len(string)):
        if char and string[char] != string[char-1]:
            groups += 1
    return groups

cases = [case for case in readfile("B-large.in").split("\n")[1:] if case != ""]
output = ""

for case in range(len(cases)):
    output += "Case #" + str(case+1) + ": " + str(flips(cases[case])) + ("\n" if case != len(cases)-1 else "")

writefile("output.txt", output)
