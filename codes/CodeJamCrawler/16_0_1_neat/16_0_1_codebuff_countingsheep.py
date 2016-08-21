#from utilities import nonstd
#std = nonstd.IO(in_file='countingsheep.in', out_file='countingsheep.out')
#stdin = nonstd.In(in_file='countingsheep.in')

test_cases = int(input())

for test_case in range(test_cases):
    N = int(input())
    iteration = 1
    digits = set()
    insomnia = False
    current_no = N
    while len(digits) < 10:
        current_no = iteration * N
        if current_no is 0:
            insomnia = True
            break
        digits.update(list(str(current_no)))
        iteration += 1
    if not insomnia:
        print('Case #' + str(test_case+1) + ': ' + str(current_no))
    else:
        print('Case #' + str(test_case+1) + ': ' + 'INSOMNIA')

