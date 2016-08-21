out = open('small.out', 'w')
out.write("Case #1:\n")
start_string = 10000000000000000000000000000001
counter = 500
prime = True
correct = True
while counter > 0:
    answer = str(start_string)
    not_prime_count = 0
    correct = True
    for base in range(2,11):
        new_num = int(str(start_string), base)
        #print new_num
        prime = True
        for divisor in range(2,20):
            if new_num % divisor == 0:
                answer = answer + " " + `divisor`
                prime = False
                not_prime_count = not_prime_count + 1
                break
        if prime == True:
            correct = False
    if correct == True:
        #print "got one!"
        out.write(answer + "\n")
        counter = counter - 1
    start_string = int(str(start_string), 2)
    start_string = start_string + 2
    start_string = bin(start_string)
    start_string = str(start_string)[2:]

    