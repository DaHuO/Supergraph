"""Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep
faster. First, she picks a number N. Then she starts naming N, 2N, 3N ans so on.
Whenever she names a number she thinks about all the digits in the number. She
keeps track of which digits (0-9) she has seen at least once so far as part of
any number she has named. Once she has seen each of the ten digits at least
once, she will fall asleep. 

Bleatrix must start with N and she must always name (i+1)*N directly after i*N
For example, suppose Bleatrix picks N = 1692. She would count as follows:
    N = 1692. Now she has seen the digits 1, 2, 6, 9
    2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9
    3N = 5076. Now she has seen the digits 0-9, and falls asleep. What is the
    last number that she will name before falling asleep? If she will count
    forever, print INSOMNIA instead. 


Input:
    The first line of input gives the number of test cases, T. T test cases
    follow. Each consists of one line with a single number N, the number
    Bleatrix has chosen. 

Output:
    For each test case, output one line containing Case #x: y, where x is the
    test case number starting from 1, and y is the last number that Bleatrix wil
    name before falling asleep, according to the rules above."""
cases = int(input())
digits = list(range(10))
case = 1
for line in range(cases):
    multiplier = 1
    begin = int(input())
    if begin == 0:
        print(("Case #%d: INSOMNIA") % case)
        case += 1 
        continue
    seen = [int(i) for i in list(str(begin))]
    while list(set(seen)) != list(set(digits)):
        add = begin*multiplier
        new_seen = [int(i) for i in list(str(add))]
        for j in new_seen:
            seen.append(j)
        multiplier +=1
    print(("Case #%d: " + str(add)) % case)
    case += 1
