
all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def check_all(l):
    for k in all_numbers:
        if str(k) not in l:
            break
    else:
        return True
    return False

def main():
    n_test_cases = int(raw_input().strip())
    
    f = open("output_a_large.txt", "w")
    output = ""
    
    for x in range(n_test_cases):
        N = raw_input().strip()
        try:
            N = int(N)
        except:
            print "You must enter an integer!"
        
        seen_numbers = []
        new_numbers = []
        times_since_new_numbers = 0
        
        current_numbers = str(N)
        for n in current_numbers:
            if n not in seen_numbers:
                seen_numbers.append(n)
                times_since_new_numbers = 0
        
        cnt = 2
        while True:
            new_N = cnt * N
            current_numbers = str(new_N)
            for n in current_numbers:
                if n not in seen_numbers:
                    seen_numbers.append(n)
                    times_since_new_numbers = 0
                    new_numbers.append(n)
            
            if new_numbers == []:
                times_since_new_numbers += 1
            
            if times_since_new_numbers >= 1000:
                print "Case #%d: INSOMNIA" % (x + 1)
                output += "Case #%d: INSOMNIA\n" % (x + 1)
                break
                
            cnt += 1
            new_numbers = []
            
            if check_all(seen_numbers):
                print "Case #%d: %d" % (x + 1, new_N)
                output += "Case #%d: %d\n" % (x + 1, new_N)
                break
                
    f.write(output)
    f.close()


if __name__ == '__main__':
    main()