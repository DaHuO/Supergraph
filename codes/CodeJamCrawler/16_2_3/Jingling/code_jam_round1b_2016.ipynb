{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import sys\n",
    "\n",
    "def ReadInts(fname):\n",
    "    with open(fname, 'r') as f:\n",
    "        read_data = f.read()\n",
    "    return list(map(str, read_data.strip().split()))\n",
    "\n",
    "fname = 'C-large.in'\n",
    "data = ReadInts(fname)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "------------------------Question 3------------------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 1\n",
      "Case #2: 0\n",
      "Case #3: 0\n",
      "Case #4: 2\n",
      "Case #5: 5\n",
      "Case #6: 5\n",
      "Case #7: 2\n",
      "Case #8: 3\n",
      "Case #9: 5\n",
      "Case #10: 7\n",
      "Case #11: 7\n",
      "Case #12: 8\n",
      "Case #13: 1\n",
      "Case #14: 1\n",
      "Case #15: 4\n",
      "Case #16: 12\n",
      "Case #17: 5\n",
      "Case #18: 3\n",
      "Case #19: 5\n",
      "Case #20: 2\n",
      "Case #21: 12\n",
      "Case #22: 2\n",
      "Case #23: 6\n",
      "Case #24: 5\n",
      "Case #25: 1\n",
      "Case #26: 2\n",
      "Case #27: 3\n",
      "Case #28: 3\n",
      "Case #29: 0\n",
      "Case #30: 6\n",
      "Case #31: 1\n",
      "Case #32: 2\n",
      "Case #33: 7\n",
      "Case #34: 7\n",
      "Case #35: 5\n",
      "Case #36: 7\n",
      "Case #37: 7\n",
      "Case #38: 4\n",
      "Case #39: 7\n",
      "Case #40: 5\n",
      "Case #41: 5\n",
      "Case #42: 3\n",
      "Case #43: 7\n",
      "Case #44: 3\n",
      "Case #45: 6\n",
      "Case #46: 6\n",
      "Case #47: 6\n",
      "Case #48: 1\n",
      "Case #49: 6\n",
      "Case #50: 5\n",
      "Case #51: 5\n",
      "Case #52: 0\n",
      "Case #53: 2\n",
      "Case #54: 2\n",
      "Case #55: 7\n",
      "Case #56: 4\n",
      "Case #57: 5\n",
      "Case #58: 7\n",
      "Case #59: 4\n",
      "Case #60: 2\n",
      "Case #61: 0\n",
      "Case #62: 2\n",
      "Case #63: 4\n",
      "Case #64: 9\n",
      "Case #65: 7\n",
      "Case #66: 3\n",
      "Case #67: 5\n",
      "Case #68: 7\n",
      "Case #69: 5\n",
      "Case #70: 6\n",
      "Case #71: 2\n",
      "Case #72: 1\n",
      "Case #73: 3\n",
      "Case #74: 1\n",
      "Case #75: 3\n",
      "Case #76: 7\n",
      "Case #77: 7\n",
      "Case #78: 4\n",
      "Case #79: 5\n",
      "Case #80: 6\n",
      "Case #81: 2\n",
      "Case #82: 4\n",
      "Case #83: 3\n",
      "Case #84: 2\n",
      "Case #85: 6\n",
      "Case #86: 2\n",
      "Case #87: 5\n",
      "Case #88: 4\n",
      "Case #89: 7\n",
      "Case #90: 4\n",
      "Case #91: 5\n",
      "Case #92: 12\n",
      "Case #93: 2\n",
      "Case #94: 7\n",
      "Case #95: 2\n",
      "Case #96: 7\n",
      "Case #97: 5\n",
      "Case #98: 3\n",
      "Case #99: 7\n",
      "Case #100: 6\n"
     ]
    }
   ],
   "source": [
    "T = int(data[0])\n",
    "counter = 1\n",
    "for i in range(1,T+1):\n",
    "    graph = dict()\n",
    "    N = int(data[counter])\n",
    "    counter = counter + 1\n",
    "    for j in range(0, N):\n",
    "        word1 = data[counter]+'1'\n",
    "        word2 = data[counter+1]+'2'\n",
    "        counter = counter+2\n",
    "        if word1 not in graph:\n",
    "            graph[word1] = set()\n",
    "        graph[word1].add(word2)\n",
    "        if word2 not in graph:\n",
    "            graph[word2] = set()\n",
    "        graph[word2].add(word1)\n",
    "    res = bipartiteMatch(graph)\n",
    "    M = len(res[0])/2\n",
    "    V = len(graph)\n",
    "    min_edge_cover = V - M\n",
    "    dup = N - min_edge_cover\n",
    "    print 'Case #%d: %d' %(i, dup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "N"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Hopcroft-Karp bipartite max-cardinality matching and max independent set\n",
    "# David Eppstein, UC Irvine, 27 Apr 2002\n",
    "\n",
    "def bipartiteMatch(graph):\n",
    "\t'''Find maximum cardinality matching of a bipartite graph (U,V,E).\n",
    "\tThe input format is a dictionary mapping members of U to a list\n",
    "\tof their neighbors in V.  The output is a triple (M,A,B) where M is a\n",
    "\tdictionary mapping members of V to their matches in U, A is the part\n",
    "\tof the maximum independent set in U, and B is the part of the MIS in V.\n",
    "\tThe same object may occur in both U and V, and is treated as two\n",
    "\tdistinct vertices if this happens.'''\n",
    "\t\n",
    "\t# initialize greedy matching (redundant, but faster than full search)\n",
    "\tmatching = {}\n",
    "\tfor u in graph:\n",
    "\t\tfor v in graph[u]:\n",
    "\t\t\tif v not in matching:\n",
    "\t\t\t\tmatching[v] = u\n",
    "\t\t\t\tbreak\n",
    "\t\n",
    "\twhile 1:\n",
    "\t\t# structure residual graph into layers\n",
    "\t\t# pred[u] gives the neighbor in the previous layer for u in U\n",
    "\t\t# preds[v] gives a list of neighbors in the previous layer for v in V\n",
    "\t\t# unmatched gives a list of unmatched vertices in final layer of V,\n",
    "\t\t# and is also used as a flag value for pred[u] when u is in the first layer\n",
    "\t\tpreds = {}\n",
    "\t\tunmatched = []\n",
    "\t\tpred = dict([(u,unmatched) for u in graph])\n",
    "\t\tfor v in matching:\n",
    "\t\t\tdel pred[matching[v]]\n",
    "\t\tlayer = list(pred)\n",
    "\t\t\n",
    "\t\t# repeatedly extend layering structure by another pair of layers\n",
    "\t\twhile layer and not unmatched:\n",
    "\t\t\tnewLayer = {}\n",
    "\t\t\tfor u in layer:\n",
    "\t\t\t\tfor v in graph[u]:\n",
    "\t\t\t\t\tif v not in preds:\n",
    "\t\t\t\t\t\tnewLayer.setdefault(v,[]).append(u)\n",
    "\t\t\tlayer = []\n",
    "\t\t\tfor v in newLayer:\n",
    "\t\t\t\tpreds[v] = newLayer[v]\n",
    "\t\t\t\tif v in matching:\n",
    "\t\t\t\t\tlayer.append(matching[v])\n",
    "\t\t\t\t\tpred[matching[v]] = v\n",
    "\t\t\t\telse:\n",
    "\t\t\t\t\tunmatched.append(v)\n",
    "\t\t\n",
    "\t\t# did we finish layering without finding any alternating paths?\n",
    "\t\tif not unmatched:\n",
    "\t\t\tunlayered = {}\n",
    "\t\t\tfor u in graph:\n",
    "\t\t\t\tfor v in graph[u]:\n",
    "\t\t\t\t\tif v not in preds:\n",
    "\t\t\t\t\t\tunlayered[v] = None\n",
    "\t\t\treturn (matching,list(pred),list(unlayered))\n",
    "\n",
    "\t\t# recursively search backward through layers to find alternating paths\n",
    "\t\t# recursion returns true if found path, false otherwise\n",
    "\t\tdef recurse(v):\n",
    "\t\t\tif v in preds:\n",
    "\t\t\t\tL = preds[v]\n",
    "\t\t\t\tdel preds[v]\n",
    "\t\t\t\tfor u in L:\n",
    "\t\t\t\t\tif u in pred:\n",
    "\t\t\t\t\t\tpu = pred[u]\n",
    "\t\t\t\t\t\tdel pred[u]\n",
    "\t\t\t\t\t\tif pu is unmatched or recurse(pu):\n",
    "\t\t\t\t\t\t\tmatching[v] = u\n",
    "\t\t\t\t\t\t\treturn 1\n",
    "\t\t\treturn 0\n",
    "\n",
    "\t\tfor v in unmatched: recurse(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#back up\n",
    "A = '/home/sec/happy'\n",
    "A.split('/')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
