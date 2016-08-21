

test = int(raw_input())

for case in range(test):
    number = int(raw_input())
    if number == 0:
        print "Case #" + str(case+1) + ": INSOMNIA"
    else:
        number_is_present = list()
        for i in range(10):
            number_is_present.append(False)

        reps = 1
        while True:
            number_new = number * reps
            reps += 1
            for num in str(number_new):
                if not number_is_present[int(num)]:
                    number_is_present[int(num)] = True

            flag = False
            for present in number_is_present:
                if present:
                    flag = True
                else:
                    flag = False
                    break

            if flag:
                print "Case #" + str(case+1) + ": " + str(number_new)
                break
