##Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N.
## Then she starts naming N, 2 × N, 3 × N, and so on. Whenever she names a number, she thinks about all of the digits
# in that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as
#  part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.
import collections


#open input file
f = open('A-large.in')
outputFile = open('output.in','w+')

case = 1

f.__next__()

for line in f:
    #get the input
    bt_number = line

    #create an empty list and a list with all digits
    current_digits = []
    full_digits = ['0','1','2','3','4','5','6','7','8','9']

    # slice the strings digits and put them in the empty list
    for digit in bt_number:
        if current_digits.count(digit) == 0 and digit != '\n':
            current_digits.append(digit)

    #define bool variable and a increment int
    isSleepy = False
    i = 2



    while isSleepy == False:
        #incremental multiplication
        new_num = int(bt_number) * int(i)

        #check if digits are in the list the add if not
        for digit in str(new_num):
            if current_digits.count(digit) == 0:
                current_digits.append(digit)


        #compare digits in both lists each time
        if collections.Counter(full_digits) == collections.Counter(current_digits) or new_num == 0:
            isSleepy = True
            break

        #increment i
        i+= 1

    if new_num == 0:
        s = str("case #{0}: INSOMNIA\n".format(case))
        outputFile.write(s)
    else:
        s = str("case #{0}: {1}\n".format(case,new_num))
        outputFile.write(s)
    case += 1

f.close()
outputFile.close()
