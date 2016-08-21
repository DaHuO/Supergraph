

test = 0

test = int(raw_input())

for i in range(0, test):
    a = []
    curr = raw_input()
    for ia in curr:
        if len(a) == 0:
            a.append(ia)
        else:
            if ord(a[0]) <= ord(ia):
                a.insert(0, ia)
            else:
                a.append(ia)
    output = "Case #" + str(i+1) + ": "
    for ia in a:
        output += ia
    print output
    
