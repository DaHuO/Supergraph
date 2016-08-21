def print_solution(i, x):
    print 'Case #{}: {}'.format(i, x)

class Pancakes(object):
    def __init__(self, pancakes_s):
        ps = []
        for c in pancakes_s:
            if c == '+':
                ps.append(True)
            elif c == '-':
                ps.append(False)
            else:
                raise Exception('invalid pancakes: {}'.format(pancakes_s))
        self.ps = ps
    def get_first_false_index(self):
        index = 0
        while index < len(self.ps):
            if not self.ps[index]:
                break
            index += 1
        return index
    def get_last_false_index(self):
        index = len(self.ps) - 1
        while index >= 0:
            if not self.ps[index]:
                break
            index -= 1
        return index
    def flip_n(self, n):
        assert(n <= len(self.ps))
        i = 0
        while i < n/2:
            tmp = self.ps[i]
            self.ps[i] = not self.ps[n-1-i]
            self.ps[n-1-i] = not tmp
            i += 1
        if n % 2 == 1:
            self.ps[i] = not self.ps[i]    

def handle_test(i):        
    s = raw_input()
    pancakes_t = Pancakes(s)
    flips = 0
    last_plus_index = len(pancakes_t.ps)-1
    while last_plus_index >= 0:
        if pancakes_t.ps[last_plus_index]:
            last_plus_index -= 1
            continue
        if pancakes_t.ps[0]:
            #first_false is > 0 because panackes[0] is true
            first_false = pancakes_t.get_first_false_index() - 1
            pancakes_t.flip_n(first_false + 1)
        else:
            pancakes_t.flip_n(last_plus_index + 1)
        flips += 1
    print_solution(i, flips)
        
def main():
    n = int(raw_input())
    for i in range(n):
        handle_test(i + 1)

if __name__ == "__main__":
    main()        
