def rank_and_file(s, n):
    a = []
    for i in range(len(s)):
        rc = s[i]
        for j in range(len(rc)):
            if not rc[j] in a:
                a.append(rc[j])

    
    return rec([], s, a, 0, n)


    
    

def rec(c, r, a, d, n):
    if d == n:
        # Check if we are using all the heights
        for i in range(len(a)):
            height = a[i]
            occored = False

            for j in range(len(c)):
                if height in c[j]:
                    occored = True
                    break

            if not occored:
                return False

        # Final Check
        s = list(c)
        s.extend(r)
        
        p = list(c)
        for i in range(n):
            p.append([x[i] for x in c])


        for i in range(len(s)):
            try:
                p.remove(s[i])
            except ValueError:
                return False

        return ' '.join([str(x) for x in p[0]]).strip()
    else:
        for i in range(len(r)):
            if valid_placement(c, r[i]):
                # Compute the new configureation
                nc = list(c)
                nc.append(r[i])

                # Compute the new remaining list
                nr = list(r)
                nr.remove(r[i])

                res = rec(nc, nr, a, d+1, n)

                if not res == False:
                    return res

    return False

def valid_placement(c, rc):
    if len(c) == 0:
        return True
    
    p = c[len(c)-1]

    for i in range(len(p)):
        if p[i] >= rc[i]:
            return False

    return True
        
    

o = open('output.txt', 'w+')
f = open('B-small-attempt1.in', 'r+')
##f = open('test.txt', 'r+')
T = int(f.readline())

for i in range(T):
    N = int(f.readline())

    data = []
    for j in range((2 * N) - 1):
        line = f.readline().strip()
        l = [int(x) for x in line.split(' ')]
        data.append(l)
    
    res = rank_and_file(data, N)
    print(res)

    o.write("Case #" + str(i + 1) + ": " + str(res) + "\n")

f.close()
o.close()
