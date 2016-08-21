import sys
import re

def main ():

    T = int (sys.stdin.readline ().strip ())
    D = [] * 10

    D.append ({"value": 0, "subtotals": numbers ("ZERO")})
    D.append ({"value": 2, "subtotals": numbers ("TWO")})
    D.append ({"value": 4, "subtotals": numbers ("FOUR")})
    D.append ({"value": 6, "subtotals": numbers ("SIX")})
    D.append ({"value": 8, "subtotals": numbers ("EIGHT")})
    
    D.append ({"value": 1, "subtotals": numbers ("ONE")})
    D.append ({"value": 3, "subtotals": numbers ("THREE")})
    D.append ({"value": 5, "subtotals": numbers ("FIVE")})
    
    D.append ({"value": 7, "subtotals": numbers ("SEVEN")})
    D.append ({"value": 9, "subtotals": numbers ("NINE")})

    for t in range (T):

        S = sys.stdin.readline ().strip ()
        s = numbers (S)
        answer = ""

        for d in D:

            while enough (s, d ["subtotals"]):

                answer += str (d ["value"])

        answer = ''.join (sorted (answer))
        print ("Case #{}: {}".format (t + 1, answer))

    return 0

def numbers (string):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = [0] * 26

    for character in string:

        numbers [alphabet.index (character)] += 1

    return numbers

def enough (totals, subtotals):

    bit = True

    for p in range (len (subtotals)):

        if subtotals [p] > totals [p]:

            bit = False
            break

    if bit:

        for p in range (len (subtotals)):

            totals [p] -= subtotals [p]

    return bit

def empty (subtotals):

    bit = True

    for p in range (len (subtotals)):

        if subtotals [p] != 0:

            bit = False
            break

    return bit

if __name__ == "__main__":

    exit (main ())
