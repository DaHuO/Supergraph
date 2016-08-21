


def find_missing(number,people):
    counter = [0] * (2501)
    for i in range(2*number-1):
        for j in range(number):
            counter[people[i][j]] += 1
    missingList = ""
    for i in range(2501):
        if counter[i] % 2 == 1:
            missingList += (str(i)+" ")
    return missingList

for i in range(1,input()+1):
    number = input()
    people = []
    for j in range(1,2*number):
        people.append(map(int,raw_input().split()))
    missing = find_missing(number,people)
    print "Case #{0}: {1}".format(i,missing)