digits = []
numbers = []

def show(something):
    print something

def digitSeen(digit):
    status = False
    if digit in digits:
        status = True
    return status

def push(digit):
    if not digitSeen(digit):
        digits.append(digit)
        
def parse(number):
    numbers.append(number)
    string = str(number)
    for char in string:
        push(int(char))
        
def asleep():
    status = False
    if len(digits) == 10:
        status = True
    return status

def reset():
    global digits, numbers
    digits = []
    numbers = []

def start(number):
    reset()
    i = 1
    if number == 0:
        return "INSOMNIA"
    while not asleep():
        parse(i * number)
        i += 1  
    return str(numbers.pop())
    
infile = open('A-large.in','r')
cases = int(infile.readline())

count = 1

outfile = open("A-large.out", "w")
for case in range(1, cases + 1):
    number = int(infile.readline())
    outfile.write("Case #" + str(case) + ": " + start(number) + '\n')

outfile.close()
   




