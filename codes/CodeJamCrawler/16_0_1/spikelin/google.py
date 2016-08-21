# __author__ = 'xjlin'

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
def get_number(n):
    while n!=0:
        yield n % 10
        n = n//10
for i in range(1, t + 1):
    #n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    string = []
    one_n = int(input())
    n = one_n
    app = list(set([x for x in get_number(n)]))
    string.extend(app)
    str_len = len(string)
    while (str_len != 10) and (one_n != 0):
        n += one_n
        app = list(set([x for x in get_number(n)]))
        string.extend(app)
        string = list(set(string))
        str_len = len(string)
    if one_n == 0:
        answer = 'INSOMNIA'
    else:
        answer = n

    print("Case #{}: {}".format(i, n))
    # check out .format's specification for more formatting options