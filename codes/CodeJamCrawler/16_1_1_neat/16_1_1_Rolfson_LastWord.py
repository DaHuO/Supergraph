f = open("small.in")
output = open("small.out", 'w')
iterations = int(f.readline())

for x in range(iterations):
    y = f.readline()
    result = ''
    for char in y:
        if result == '':
            result += char
        else:
            if ord(char) >= ord(result[0]):
                result = char + result
            else:
                result = result + char
    output.write( "Case #" + `x+1` + ": " + result)