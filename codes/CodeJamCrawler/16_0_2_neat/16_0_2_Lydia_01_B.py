inputFileName = "B-large.in.txt"
outputFileName = "B_result.out.txt"

def solution(cookies):
    flip = 0
    cookies.reverse()
    while(cookies.count('-') > 0):
        flipRange = []
        unflipRange = []
        for i in range(0, len(cookies)):
            if(cookies[i] == '-'):
                flipRange = cookies[i:]
                unflipRange = cookies[:i]
                break
        print flipRange
        if((flipRange[0] == '-') & (flipRange[-1] == '+')):
            x = len(flipRange)-1
            while(x > 0):
                if(flipRange[x] == '+'):
                    flipRange[x] = '-'
                else:
                    break
                x -= 1
            flip += 1
        flipRange.reverse();
        for c in range(0, len(flipRange)):
            if(flipRange[c] == '+'):
                flipRange[c] = '-'
            else:
                flipRange[c] = '+'
                    
        cookies = unflipRange + flipRange
        flip += 1
        print "after flip: "
        print cookies

    return flip


inputFile = open(inputFileName, 'r')
outputFile = open(outputFileName, 'a')

# read/write
noOfCase = int(inputFile.readline());
for i in range(1, noOfCase+1):
    input = inputFile.readline()[:-1]
    print "input: " + input
    cookies = list(input)
    output = "Case #" + str(i) + ": " + str(solution(cookies)) + "\n";
    print "output: " + output
    outputFile.write(output);


