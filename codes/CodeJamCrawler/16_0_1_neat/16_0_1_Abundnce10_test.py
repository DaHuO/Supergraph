import csv

INPUT_FILE = "./A-large.in"
OUTPUT_FILE = "A-large-output.csv"

file_inputs = [line.rstrip('\n') for line in open(INPUT_FILE)]

results = []


def numberToList(num):
    "takes a number (e.g. 3091) and turns into [3,0,9,1]"
    return list(str(num))


case = 1

for file_input in file_inputs[1:]: # skip first line
    starting_number = int(file_input)
    numbers = set()
    numbers.update(numberToList(starting_number))

    i = 1
    seeking = True
    number = starting_number
    limit = 100000

    while seeking == True and i < limit:
        number = i * starting_number
        numbers.update(numberToList(number))

        # print number, numbers

        if len(numbers) == 10:
            results.append(["Case #" + str(case) + ": " + str(number)])
            seeking = False
        else:
            i += 1

    if i == limit:
        results.append(["Case #" + str(case) + ": INSOMNIA"])

    case += 1 



resultFile = open(OUTPUT_FILE, 'w')
wr = csv.writer(resultFile, dialect='excel')
wr.writerows(results)
resultFile.close()