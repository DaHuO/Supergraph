from collections import defaultdict

def main(): 
    num_input = int(raw_input())

    for i in range(num_input):
        test_num = int(raw_input())
        if test_num == 0:
            print  'Case #{:d}: INSOMNIA'.format(i+1)
        else:
            counter = 1
            d_dict = defaultdict(int)
            while True:
                num = counter * test_num
                for s in str(num):
                    d_dict[s] = 1
                if sum(d_dict.values()) == 10:
                    print 'Case #{:d}: {:d}'.format(i+1, num)
                    break
                counter += 1

main()