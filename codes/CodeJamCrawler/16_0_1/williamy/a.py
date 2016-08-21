def last_num_before_slep(n):
    if int(n) == 0:
        return "INSOMNIA"
    else:
        seen = [0] * 10
        i = 1
        curr = int(n)
        while not all_seen(seen):
            product = i * curr 
            digits = str(product)
            for d in digits:
                seen[int(d)] = 1
            i += 1     
        result = (i - 1) * curr 
        return str(result)

def all_seen(a):
    for i in a:
        if i == 0: return False
    return True

def main():
    fp = open('A-large.in')
    num_rounds = int(fp.readline())
    curr_round = 0
    for line in fp:
        curr_round += 1 
        n = int(line)     
        print("Case #%d: %s" % (curr_round, last_num_before_slep(n)))

if __name__ == "__main__":
    main()
