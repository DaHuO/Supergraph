##input = open('B-sample-input.txt', 'r')
##output = open('B-sample-output.txt', 'w')

##input = open('B-small-attempt0.in', 'r')
##output = open('B-small.out', 'w')

input = open('B-large.in', 'r')
output = open('B-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def flip(s):
    news = ""
    for c in s:
        if c == "-":
            news = "+" + news
        else:
            news = "-" + news
    return news

def solve(s):
    lastminus = s.rfind("-")
    if lastminus == -1:
        return 0    
    s = s[:lastminus + 1]
    flips = 1
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            flips += 1
    return flips
    
##    flips = 0
##    sub = s
##    while "-" in sub:
##        if sub[-1] == "-":
##            if sub[0] == "+":
##                firstminus = sub.find("-")
##                sub = flip(sub[:firstminus]) + sub[firstminus:]
##                flips += 1
##            else:
##                sub = flip(sub)
##                flips += 1
##        else:
##            lastminus = sub.rfind("-")
##            sub = sub[:lastminus + 1]
##    return flips
                

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        s = input.readline().strip()
##        if case == 1:
        solution = solve(s)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        



main()
input.close()
output.close()
    
