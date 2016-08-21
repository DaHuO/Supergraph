#!/usr/bin/env python3
import signal

import pyprimes

filename = "C-large"
COINWIDTH = 32
NUMBER_OF_COINS = 500

COIN_FORMAT = "1{centervalue:0{centerwidth}b}1"
MAX_FACTORING_TIME = 1  # seconds
CENTERWIDTH = COINWIDTH - 2 

class MyTimeoutError(Exception):
    pass

def timeouthandler(signum, frame):
    raise MyTimeoutError()

signal.signal(signal.SIGALRM, timeouthandler) 

def is_valid_coin(coinstring):
    for base in range(2,11):
        value = int(coinstring, base)
        if pyprimes.isprime(value):
            return False
    return True


def get_coin_factors(coinstring):
    factorstring = ""
    for base in range(2,11):
        value = int(coinstring, base)
        first_factor_info = next(pyprimes.factorise(value))
        factorstring += "{} ".format(first_factor_info[0])
    return factorstring.strip()

with open(filename + ".out", 'w') as outputfile:
    outputfile.write("Case #1:\n")
    
    coinnumber = 1
    for i in range(2**CENTERWIDTH):
        coinstring = COIN_FORMAT.format(centervalue=i, centerwidth=CENTERWIDTH)
        if is_valid_coin(coinstring):
            factorstring = ""
            signal.alarm(MAX_FACTORING_TIME)
            try: 
                factorstring = get_coin_factors(coinstring)
            except MyTimeoutError:
                pass
            finally:
                signal.alarm(0)
            
            if factorstring:
                print(coinnumber, coinstring, factorstring)
                outputfile.write("{} {}\n".format(coinstring, factorstring))
                coinnumber += 1
    
        if coinnumber > NUMBER_OF_COINS:
            break
            

