import sys
from itertools import product

infile = sys.stdin
next(infile)

for line in infile:
    if not line:
        break
    
    nice_line = line.rstrip().split()
    num = int(nice_line[0])
    j = int(nice_line[1])


def main(num,j):
    print "Case #1:"
    count = 0
    for jam_coin in ("".join(jam) for jam in product("10", repeat = num)):
        if jam_coin[0] == '0' or jam_coin[-1] == '0':
            continue
        else:
            result = jam(jam_coin)
            if "None" not in result:
                print_jam = " ".join(jam(jam_coin))
                print print_jam
                count += 1
        
            if count == j:
                break
            

def jam(coin):
    printout = list()
    printout.append(coin)
    for idx in range(2,11):
        printout.append(str(divisors(int(coin,idx))))
        
    if None in printout:
        return None
    else:
        return printout
        
def divisors(num):
    if num <= 30000:
        end = num
    else:
        end = 30000
        
    for idx in range(2,end):
        if num % idx != 0:
            continue
        else:
            return idx
            
"""def all_poss_jams(num):
    all_jams = ("".join(jam) for jam in product("10", repeat = num))
    
    all_jams[:] = (jam for jam in all_jams if not (jam[0] == "0" or jam[-1] == "0"))
    for jam in all_jams:
        if jam[0] == "0" or jam[-1] == "0":
            jam = None
          
    return all_jams
"""    
    
main(num,j)