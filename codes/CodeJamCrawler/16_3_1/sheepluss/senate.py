from collections import defaultdict
from operator import itemgetter

def senate(ncase, nparties):
  party_counts = {}
  reverse_counts = defaultdict(set)
  uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  party_count_raw = [int(i) for i in raw_input().strip().split(" ")]
  #print nparties
  #print party_count_raw
  for i in xrange(len(party_count_raw)):
    party_counts[uppercase[i]] = party_count_raw[i]
    reverse_counts[party_count_raw[i]].add(uppercase[i])
  total_count = sum(party_count_raw)
  party_counts_sorted = sorted(party_counts.items(), key=itemgetter(1))
  reverse_counts_sorted = sorted(reverse_counts.items(), key=itemgetter(0))
  evac_order = []
  accounted = 1 # from back
  #print party_counts_sorted
  while accounted != nparties:
    #print accounted
    while party_counts_sorted[nparties-accounted][1] > party_counts_sorted[nparties-accounted-1][1]:
      for i in xrange(accounted):
        evac_order.append(party_counts_sorted[nparties-i-1][0])
        party_counts_sorted[nparties-i-1] = (party_counts_sorted[nparties-i-1][0], party_counts_sorted[nparties-i-1][1]-1)
    accounted += 1
  accounted = 1
  while accounted <= nparties-2:
    for i in xrange(party_counts_sorted[nparties-accounted][1]):
      evac_order.append(party_counts_sorted[nparties-accounted][0])
    accounted += 1
  for i in xrange(party_counts_sorted[0][1]):
    evac_order.append(party_counts_sorted[0][0] + party_counts_sorted[1][0])
  print "Case #%d: %s" % (ncase, " ".join(evac_order))
  """if len(reverse_counts_sorted)==1:
    if nparties%2==0:
      for i in xrange(0, nparties, 2):
        for j in xrange(reverse_counts_sorted[0][0]):
          evac_order.append(uppercase[i] + uppercase[i+1])
    else:
      limit = nparties-3"""

ncases = int(raw_input().strip())
for i in xrange(1, ncases+1):
  senate(i, int(raw_input().strip()))
