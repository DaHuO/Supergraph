cases = int(input())
for i in range(cases):
    result = ""
    inited = False
    inp = input()
    for a in inp:
        if inited:
            if a < result[0]:
                result = result + a
            else:
                result = a + result

        else:
            inited = True
            result = "" + a
    print("Case #{}: ".format(i+1), end="")
    print(result)
