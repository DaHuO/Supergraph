import sys

test_cases = int(sys.stdin.readline())
f = open("output", "w")

for test_case in range(0, test_cases):

    parties = int(sys.stdin.readline())
    senators = [int(x) for x in sys.stdin.readline().split(" ")]

    answer = ""

    while max(senators) > 0:
        m = max(senators)
        indicies = [i for i, x in enumerate(senators) if x == m]
        senators[indicies[0]] -= 1;
        answer += chr(indicies[0] + ord('A'))

        if len(indicies) > 1 and len(indicies) != 3:
            senators[indicies[1]] -= 1
            answer += chr(indicies[1] + ord('A'))

        answer += " "

    f.write("Case #%d: %s\n" % (test_case + 1, answer))






        


