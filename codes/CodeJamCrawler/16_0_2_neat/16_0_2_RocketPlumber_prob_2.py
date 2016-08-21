__author__ = 'shant_000'

T = int(input())

for i in range(1, T+1):
    a_cake = input()
    uniques = ""
    for sign in a_cake:
        if uniques == "":
            uniques += sign
        elif sign != uniques[-1]:
            uniques += sign
    if uniques[-1] == '+':
        print("Case #" + str(i) + ": " + str(len(uniques)-1))
    elif uniques[-1] == '-':
        print("Case #" + str(i) + ": " + str(len(uniques)))