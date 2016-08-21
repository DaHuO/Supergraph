def count_sheep(n):
    if n == 0:
        return "INSOMNIA"
    
    all_digits = set()
    for i in range(0,10):
        all_digits.add(i)
        
    digits = set()

    total = 0
    prev = 0
    while digits != all_digits:
        prev = total
        total += n
        for i in str(total):
            digits.add(int(i))
            
    return str(total)


len = int(raw_input())
for case in range(0, len):
    n = int(raw_input())
    print "Case #" + str(case+1) + ":", count_sheep(n)

    
