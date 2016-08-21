def readFile(filename):
    info = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            info.append(line)
    return info


def count(n):
    if n == 0:
        return "INSOMNIA"
    seen = [False] * 10 # 0-9 True array
    num_seen = 0
    mult = 1
    while num_seen < 10:
        m = n * mult
        result = m
        while m > 0:
            last = m%10
            if not seen[last]:
                seen[last] = True
                num_seen += 1
            m = m//10
        mult += 1
    return result
                
        
    

def main():
    filename = "data.txt"
    info = readFile(filename)
    for i in range(1, len(info)):
        result = count(int(info[i]))
        print ("Case #{0}: {1}".format(i, result))
        
