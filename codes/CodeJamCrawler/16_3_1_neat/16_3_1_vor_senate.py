#!/usr/bin/env python

class Party(object):
    def __init__(self, partyId, count):
        self.id = partyId
        self.count = count

def solve(partyCounts):
    ans = ''

    parties = []
    for i in range(len(partyCounts)):
        parties.append(Party(chr(65 + i), partyCounts[i]))
    largestParty = parties.pop(getIndexOfLargest(parties))
    nextLargestParty = parties.pop(getIndexOfLargest(parties))

    while (largestParty.count > nextLargestParty.count):
        print largestParty.id,
        largestParty.count -= 1

    for party in parties:
        while (party.count > 0):
            print party.id,
            party.count -= 1

    while (largestParty.count > 0):
        print largestParty.id + nextLargestParty.id,
        largestParty.count -= 1
        nextLargestParty.count -= 1

    print

def getIndexOfLargest(parties):
    indexLargest = 0
    countLargest = 0
    for i in range(len(parties)):
        count = parties[i].count
        if count > countLargest:
            indexLargest = i
            countLargest = count
    return indexLargest


T = int(raw_input().strip())
for testCaseNo in range(T):
    P = int(raw_input().strip())
    partyCounts = map(int, raw_input().strip().split(' '))
    print 'Case #' + str(testCaseNo + 1) + ':',
    solve(partyCounts)
