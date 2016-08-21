def get_n_jamcoins(n, length):
    results = []
    count = 0
    total = 0
    while total < n:
        cur_coin = (1 << (length - 1)) + (count << 1) + 1
        count += 1
        
        divisors = []
        base_count = 2
        is_jamcoin = True
        while base_count < 11 and is_jamcoin:
            divisor = get_divisor(to_base_n(base_count, int(bin(cur_coin)[2:])))
            if divisor == None:
                is_jamcoin = False
            else:
                divisors.append(divisor)
                base_count += 1
                
        if is_jamcoin:
            results.append((int(bin(cur_coin)[2:]), divisors))
            total += 1
            print((bin(cur_coin)[2:], divisors))
    return results
                

def get_divisor(n):
    results = []
    for i in range(2, int(n ** 0.5) + 1):
        if (n / i) % 1 == 0:
            return i
    return None
        
def to_base_n(n, x):
    result = 0
    count = 0
    while x > 0:
        result += (n ** count) * (x % 10)
        x //= 10
        count += 1
    return result


count = 0
cases = []
with open("C-small-attempt0.in") as file:
    for entry in file:
        if (count > 0):
            line = entry.split(' ')
            cases.append((line[0], line[1]))
        count += 1

results = []
print(cases)
for i in cases:
    results = get_n_jamcoins(int(i[1]), int(i[0]))

with open("out.txt", "w") as file:
    for i in range(len(results)):
        file.write("Case #" + str(i) + ":\n")
        file.write(str(results[i][0]))
        for j in results[i][1]:
            file.write(" " + str(j))
        file.write("\n")



with open("out.txt", "w") as file:
    file.write("Case #1:\n")
    for i in results:
        file.write(str(i[0]))
        for j in i[1]:
            file.write(" " + str(j))
        file.write("\n")
