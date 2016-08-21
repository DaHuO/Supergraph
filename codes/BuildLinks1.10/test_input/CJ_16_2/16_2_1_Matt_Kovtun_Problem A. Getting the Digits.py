input_file = open("A-large.in")
output_file = open("Problem A. Getting the Digits_result.txt", "w")
#ints = [i for i in range(9)]
names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
z = {}
ints = []
for i in range(len(names)):
#    j[i] = list(names[i])
    ints.append(list(names[i]))
    for o in range(len(names[i])):
      #  print(names[i][o])
        if names[i][o] in z:
            pass
        else:
            z[names[i][o]] = 0
print(ints)
print(z)
tests = int(input_file.readline())
cases = 0
for p in range(tests):
    cases += 1
    phone = []
    line = input_file.readline().strip()
   # line = list(line)
    print(line)
#    print(j)
    dct = z

    for letter in line:
        if letter in dct:
            dct[letter] += 1
        else:
            dct[letter] = 1
    print(dct)
    for k in range(dct["Z"]):
        phone.insert(0, 0)
        for j in names[0]:
            dct[j] -= 1
   # print(dct)
    for k in range(dct["W"]):
        phone.insert(2, 2)
        for j in names[2]:
            dct[j] -= 1
    for k in range(dct["X"]):
        phone.insert(6, 6)
        for j in names[6]:
            dct[j] -= 1
    for k in range(dct["G"]):
        phone.insert(8, 8)
        for j in names[8]:
            dct[j] -= 1

    for k in range(dct["T"]):
        phone.insert(3, 3)
        for j in names[3]:
            dct[j] -= 1

    for k in range(dct["R"]):
        phone.insert(4, 4)
        for j in names[4]:
            dct[j] -= 1

    for k in range(dct["O"]):
        phone.insert(1, 1)
        for j in names[1]:
            dct[j] -= 1

    for k in range(dct["S"]):
        phone.insert(7, 7)
        for j in names[7]:
            dct[j] -= 1

    for k in range(dct["N"]//2):
        phone.insert(9, 9)
        for j in names[9]:
            dct[j] -= 1
    for k in range(dct["F"]):
        phone.insert(5, 5)
        for j in names[5]:
            dct[j] -= 1


    print(dct)
    print(sorted(phone))
    ans = ""
    for i in sorted(phone):
        ans += str(i)
    output_file.write("Case #{!s}: ".format(cases))
    output_file.write(str(ans) + "\n")