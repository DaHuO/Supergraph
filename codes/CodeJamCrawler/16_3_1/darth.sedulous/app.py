import sys
import re

def main ():

    T = int (sys.stdin.readline ().strip ())

    for t in range (T):

        N = int (sys.stdin.readline ().strip ())
        P = list (map (int, sys.stdin.readline ().strip ().split (" ")))
       
        items = pairs (P) 
        total = sum (P)
        answer = []

        while total != 0:

            items.sort (key = lambda i: i ["number"], reverse = True)

            if total == 3:

                answer.append (items [0] ["name"])
                items [0] ["number"] -= 1
                total -= 1

            else:
                
                answer.append (items [0] ["name"] + items [1] ["name"])
                items [0] ["number"] -= 1
                items [1] ["number"] -= 1
                total -= 2

        answer = " ".join (answer)
        print ("Case #{}: {}".format (t + 1, answer))

    return 0

def pairs (numbers):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pairs = []

    for n in range (len (numbers)):

        pair = {"number": numbers [n], "name": alphabet [n]}
        pairs.append (pair)

    return pairs

if __name__ == "__main__":

    exit (main ())
