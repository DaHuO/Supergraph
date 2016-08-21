f = open('A.in', 'r')
f_ans = open('A.out', 'w')

num_cases = int(f.readline())
for i in range(num_cases):
    N = int(f.readline())
    digits = set(list(str(N)))
    j = 2
    no_ans = False
    while len(digits) < 10:
        new_num = N * j
        new_digits = set(list(str(new_num)))
        digits |= new_digits
        j += 1
        print j
        if j > 100:
            no_ans = True
            break
    if no_ans:
        ans = "INSOMNIA"
    else:
        ans = str(new_num)
    f_ans.write("Case #" + str(i+1) + ": " + ans + '\n')
