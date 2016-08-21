#!/usr/bin/env python3
#-*- coding: utf8 -*-
import sys

def fastCleaning(KK, CC, SS):
    if (SS <= KK - CC):
        return [-1] * (SS+1)
    # Choose a collision column for CC sets, then add the missing "G" columns
    col_idx = 0
    CC = min(CC, KK)
    for ii in range(CC-1):
        col_idx += (CC-1-ii) * KK**ii
    selection = [col_idx]
    for jj in range(CC, KK):
        selection.append(jj)
    return(selection)

def generateSeeds(KK):
    seeds = [""]
    for _ in range(KK):
        new_seeds = list()
        for seed in seeds:
            new_seeds.append(seed + "G")
            new_seeds.append(seed + "L")
        seeds = new_seeds.copy()
    return seeds

def generateOneGSeeds(KK):
    seeds = list()
    for ii in range(KK):
        seeds.append("".join( ["L"]*ii + ["G"] + ["L"]*(KK-1-ii) ))
    print(seeds, file=sys.stderr)
    return(seeds)

def generateSequence(seed, CC):
    sequence = seed
    for _ in range(CC-1):
        new_seq = ""
        for char in sequence:
            if (char == "L"):
                new_seq += seed
            elif (char == "G"):
                new_seq += "G" * len(seed)
        sequence = new_seq
    return sequence


if __name__ == "__main__":
    TT = int(input())
    for ii in range(TT):
        KK, CC, SS = [int(_) for _ in input().split()]
        cleanings = fastCleaning(KK, CC, SS)
        #cleanings = suggestCleaning(KK, CC, SS)
        print(cleanings, file=sys.stderr)
        if (len(cleanings) <= SS):
            print( "Case #" + str(ii+1) + ": " + " ".join([str(_+1) for _ in cleanings]) )
        else:
            print("Case #" + str(ii+1) + ": IMPOSSIBLE")

