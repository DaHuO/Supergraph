cases = int(input())
for c in range(cases):
    string = input()
    d = {a: 0 for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    for s in string:
        d[s] += 1
    tel = [0]*10
    
    def take(letter, full, number):
        n = d.get(letter, 0)
        for x in full:
            d[x] -= n
        tel[number] += n
        
    take('Z', 'ZERO', 0)
    take('W', 'TWO', 2)
    take('U', 'FOUR', 4)
    take('X', 'SIX', 6)
    take('G', 'EIGHT', 8)
    take('H', 'THREE', 3)
    take('F', 'FIVE', 5)
    take('S', 'SEVEN', 7)
    take('I', 'NINE', 9)
    take('O', 'ONE', 1)
    
    print("Case #{}: {}".format(c+1, ''.join(str(i) * n for i, n in enumerate(tel))))
