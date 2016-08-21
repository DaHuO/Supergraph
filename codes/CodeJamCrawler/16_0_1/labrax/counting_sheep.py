
tests = int(input())
for i in range(1, tests+1):
    algarismos = set()
    number = int(input())
    it = 1
    
    if number == 0:
        print("Case #" + str(i) + ": INSOMNIA")
        continue
    
    curr = number
    while len(algarismos) < 10:
        for e in str(curr):
            algarismos.add(e)
        if len(algarismos) == 10:
            print("Case #" + str(i) + ": " + str(curr))
        curr += number
    
