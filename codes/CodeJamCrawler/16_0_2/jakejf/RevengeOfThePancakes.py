# Google Code Jame 2016
# Revenge of the Pancakes
# Jake Francis

def main():
    items = int(input())
    for i in range(1, items + 1):
        l = list(raw_input())
        count = 0
        size = len(l)
        for j in range(size - 1, -1, -1):
            if l[j] == '-':
                count += 1
                for k in range(j, -1, -1):
                    if l[k] == '+':
                        l[k] = '-'
                    else: l[k] = '+'
                
        print("Case #{}: {}".format(i, str(count)))

main()
