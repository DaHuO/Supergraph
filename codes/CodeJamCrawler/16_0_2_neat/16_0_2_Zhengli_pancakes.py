import sys

def flip(cake_list, n):
    for i in range(n, len(cake_list)):
        if cake_list[i] == "+":
            cake_list[i] = "-"
        else:
            cake_list[i] = "+"
    cake_list = cake_list[: n] + cake_list[n:]
    return cake_list
    
def all_happy(cake_str):
    cake_list = list(cake_str)
    if "-" not in cake_list:
        return 0
    elif "+" not in cake_list:
        return 1
    cake_list.reverse()
    
    i = 0
    count = 0
    while "-" in cake_list and i < len(cake_list):
        if cake_list[i] == "-":
            flip(cake_list, i)
            count += 1
        # print cake_list
        i = i + 1
    return count
    

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        cake_str = sys.stdin.readline()
        print "Case #%d:" % (i + 1),
        print all_happy(cake_str)