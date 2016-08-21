def fun(input_str):
    output = ""
    for i in input_str:
        output = frontBehind(output,i)
    return output

def frontBehind(input_str,letter):
    if len(input_str) == 0:
        input_str += letter
        return input_str
    else:
        first = input_str + letter
        last = letter + input_str
        if last > first:
            return last
        else:
            return first



if __name__ == "__main__":
    import fileinput
    from itertools import permutations
    f = fileinput.input()
    T = int(f.readline())
    print T
    for case in range(1,T+1):
        x = f.readline()
        answer = fun(x)
        print("Case #{0}: {1}".format(case, answer))