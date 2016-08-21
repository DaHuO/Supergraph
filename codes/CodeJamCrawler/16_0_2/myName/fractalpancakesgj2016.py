import csv

def check_validity(s):
    n = 0
    for i in range (len (s)):
        if s [i] == '+':
            n = n + 1
    if n == len (s):
        return True
    else:
        return False


def replace_front (s):
    s = list (s)
    all_plus = check_validity (s)
    if all_plus == True:
        return 0

    c = 0
    while (not all_plus):
        start = s [0]
        for i in range (len (s)):
            if s [i] == start:
                if start == '+':
                    s [i] = '-'
                else:
                    s [i] = '+'
            else:
                break
        c = c + 1
        all_plus = check_validity (s)


    return c


fileName = "B-large.in"
CSVReader = csv.reader(open(fileName), delimiter=',')
data = list(CSVReader)
data = [data[i][0] for i in range(1, len(data))]


f = open("resultL.csv","w")

for i in range (len (data)):
    c = replace_front (data [i])
    s = "Case #" + str (i+1) + ": " + str (c) + "\n"
    print(s)
    f.write(s)

f.close()






