def all_pancakes_happy(s):
    all_plus = True
    for i in s:
        if i == "-":
            all_plus = False
    return all_plus

def reverse_pancakes(s):
    s = list(reversed(s))

    for i in range(len(s)):
        if s[i] == "+":
            s[i] = "-"
        else:
            s[i] = "+"
    return s

def pancake_number(s):
    s = list(s)
    
    flips = 0

    while not all_pancakes_happy(s):

        i = list(reversed(s)).index("-")
        #list_1, list_2 = split_list(s, i)
        i = len(s) - i
        s, hs = s[:i], s[i:]


        if s[0] == "-":
            s = reverse_pancakes(s)
            flips += 1
        else:
            i = s.index("-")
            s = reverse_pancakes(s[:i]) + s[i:]
            flips += 1
        
        s = s + hs
    return flips
    

def read_data(filename):
    data = [line.strip() for line in open(filename)]
    return (data.pop(0), data)

def write_data(filename, data):
    total, tests = data
    
    f = open(filename, 'w')

    for i,t in enumerate(tests):
        f.write("Case #{}: {}\n".format(i+1, pancake_number(t)))

if __name__ == "__main__":
    write_data("B-large.out", read_data("B-large.in"))
