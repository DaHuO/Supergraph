def f(x):
    jafoi = set()
    digit = [ False for i in range(10)]
    current = x
    while True:
        temp = current
        while temp != 0:
            digit[temp%10] =  True
            temp //=10
        if False not in digit:
            return current
        else:
            if current in jafoi:
                return "INSOMNIA"
            else:
                jafoi.add(current)
                current += x
def main():
    inputFile = open("q1ainput.txt", "r")
    outputFile = open("q1aoutput.txt", "w")
    #n = input()
    n = int(inputFile.readline())
    for case in range(n):
        #dataInput = input()
        dataInput = int(inputFile.readline())
        resp = f(dataInput)
        #print "Case #%s: %s" % (str(case+1), str(resp))
        outputFile.write( 'Case #%s: %s\n' % (str(case+1) , str(resp) ) )
main()
