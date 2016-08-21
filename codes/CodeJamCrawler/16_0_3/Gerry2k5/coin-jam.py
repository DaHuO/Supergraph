#!/usr/bin/env python3

import sys
from math import floor, pow, sqrt

DEBUG = False

def base_convert(number, base):
  '''Return the decimal equivalent of a supplied
  number in a given base between 2 and 10

  Please note that no validation of the inputs is carried out'''

  power = 0
  num_out = 0
  
  while number > 0:
    digit = number % 10
    num_out += digit * pow(base, power)
    power += 1
    number //= 10

  return int(num_out)


def get_divisors(coin):
  '''Get a list containing the divisors of the coin in each base from 2 to 10
  Returns an empty list if the coin was prime in one of the bases'''

  divisors = []

  # Check each base from 2 to 10 inclusive
  for base in range(2, 11):
    # Get the value of the coin in the given base
    num_in_base = base_convert(int(coin), base)
    if DEBUG: print("Num in Base %d: %d" % (base, num_in_base))
    
    # Start with the lowest divisor
    divisor = 2

    # Calculate the maximum divisor
    max_divisor = floor(sqrt(num_in_base))
    if DEBUG: print("Max:", max_divisor)
    
    # Flag to determine if we found a divisor
    divisor_found = False

    # Try each possible divisor
    while divisor <= max_divisor:
      # Check if this is a valid divisor
      if DEBUG: print("Divisor:", divisor)
      if (num_in_base % divisor) == 0:
        # Set the flag and exit the while loop
        if DEBUG: print("Divisor found")
        divisor_found = True
        break
      # Not valid - try the next divisor
      else:
        divisor += 1
      
    # Store the divisor if it was found
    if divisor_found:
      divisors.append(divisor)
    # Number was prime in this base - Return empty list
    else:
      return []

  # Loop is finished - Return the list of divisors
  return divisors


def gen_coins(num_coins, coin_length):
  valid_coins = 0
  coin_purse = []

  # Generate the initial seed (potential jamcoin)
  seed = int(pow(2, coin_length - 1) + 1)
  if DEBUG: print("Seed:", seed)

  # Repeat until we have enough coins
  while valid_coins < num_coins:
    # Generate a potential jamcoin from the seed
    potential_coin = bin(seed)[2:]
    if DEBUG: print("Potential Coin:", potential_coin)
    
    # Generate the required divisors for the potential coin
    divisors = get_divisors(potential_coin)
    if DEBUG: print("Divisors:", divisors)

    # if the coin is valid
    if len(divisors) == 9:
      coin_purse.append([potential_coin, divisors])
      valid_coins += 1

    # Move to the next seed
    seed += 2

  return coin_purse

def main():
  if len(sys.argv) != 2:
    print("Usage: %s <input file>" % sys.argv[0])
    sys.exit(0)
  
  with open(sys.argv[1], 'r') as f:
    num_cases = int(f.readline())

    for case_num in range(num_cases):
      # Read the coin parameters
      (coin_length, num_coins) = [int(i) for i in f.readline().split()]
      
      print("Case #%d:" % int(case_num + 1))

      # Generate the required number of jamcoins
      if DEBUG: print("Looking for %d coins of length %d" % (num_coins, coin_length))
      jamcoins = gen_coins(num_coins, coin_length)
      if DEBUG: print("Jamcoins:", jamcoins)

      # Output each jamcoin and it's divisors
      for coin in range(num_coins):
        if DEBUG: print("Jamcoin %d:" % coin, jamcoins[coin])
        if DEBUG: print("Coin:", jamcoins[coin][0])
        if DEBUG: print("Divisors:", jamcoins[coin][1])
        print(jamcoins[coin][0], " ".join(str(divisor) for divisor in jamcoins[coin][1]))

if __name__ == "__main__":
  main()
