__author__ = 'TOBE'


import math

def ConvertToBase(x,N = 2):
    # converts from base ten to base N.
    ans = ""
    divided = x
    while divided:
        ans =  str(divided%N) + ans
        divided = divided/N

    return ans

def ConvertToBase10(x,N):
    # converts from base N to base 10
    ans = 0
    x1 = str(x)
    ans = int(x1[0])*N
    for i in xrange(1,len(x1)-1):
        ans += int(x1[i])
        ans *= N
    ans += int(x1[i+1])

    return ans

def IsPrime2(x):
    xstop = int(math.sqrt(x))
    answer = True
    divisor = 1
    i= 2
    while i < xstop:
        if x%i == 0:  # this means a number devides it
            divisor = i
            answer = False
            break
        if len(str(i)) > 2: # if i is greater that 99, then assume it is a prime
            answer = True
            divisor = 1
            break
        i += 1
    return [answer,divisor]


def IsPrime(x):
    xstop = int(math.sqrt(x))
    answer = True
    divisor = 1
    i= 2
    while i < xstop:
        if x%i == 0:  # this means a number devides it
            divisor = i
            answer = False
            break
        # if len(str(i)) > 2: # if i is greater that 99, then assume it is a prime
        #     answer = True
        #     divisor = 1
        #     break
        i += 1
    return [answer,divisor]


def CheckIfCoin(number,funtype = 1):
# number = 1000000000000101
    divisor_list = []
    is_jam_coin = True
    for i in xrange(2,10+1):
        # first convert to base
        # print "checking base ",i
        number2 = ConvertToBase10(number,i)
        # print "converted number in base ",i," is = ",number2
        if funtype == 1:
            is_prime = IsPrime(int(number2))
        else:
            is_prime = IsPrime2(int(number2))

        # print "done checking base ",i

        divisor_list.append(is_prime[1])

        if is_prime[0]:
            is_jam_coin = False
            break

    # print is_jam_coin
    if is_jam_coin == True:
        return [is_jam_coin,divisor_list]
    else:
        return False


def testrun():
    old_number = '10000000000000000000000000000000'
    counter = 0
    jam_coin_list = []
    for item in range(1,5000,2):
        # print "at path_node ",item
        suffix = ConvertToBase(int(item))
        suffix = str(suffix)
        check_number = old_number[:len(old_number)-len(suffix)] + suffix
        if len(check_number) != 32:
            print "WRONG INPUT"
            raw_input("enter")
        is_valid_coin =  CheckIfCoin(int(check_number),0)
        if is_valid_coin:
            counter += 1
            jam_coin_list.append([int(check_number),is_valid_coin[1]])
            print check_number,is_valid_coin
            # print "total found so far",len(jam_coin_list)
            if len(jam_coin_list) >= 500:
                print "all 500 found"
                return jam_coin_list
        else:
            # print is_valid_coin
            pass
    print counter
    return jam_coin_list


# code suit below is used to test
perform_test_runs = 0

if perform_test_runs:
    list_of_N_jam_coins = testrun()
    print "having found all 500, testing if they are truly jam coines"
    print "....................."

    for item in list_of_N_jam_coins:
        check_number = item[0]
        if len(str(check_number)) != 32:
            print "wrong input"
        else:
            print check_number,
            print CheckIfCoin(check_number)


solve_code_jam = 1

if solve_code_jam:
    list_of_N_jam_coins = testrun()

    print list_of_N_jam_coins

    output_file = open('submit_large.in','w')
    print >> output_file,"Case #1:"

    for item in list_of_N_jam_coins:
        print >> output_file,item[0],
        for k_item in item[1]:
            print >> output_file, k_item,
        print >> output_file, ""

    output_file.close()
