__author__ = 'Thomas'

def readFrom(file_name="../files/input.txt"):
    with open(file_name, 'r') as f:
        result = []
        for line in f:
            result.append(line.rstrip())
    return result

def appendLineTo(line, file_name ="../files/codeJamResult.txt"):
   with open(file_name, 'a') as f:
        f.write(line + '\n')

def writeTo(lines, file_name="../files/codeJamResult.txt"):
    with open(file_name, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def aLine(test_number, value):
    return "Case #" + str(test_number) + ": " + str(value);


