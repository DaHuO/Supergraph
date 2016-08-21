{
 "metadata": {
  "name": "",
  "signature": "sha256:1286c061a0addfde1818b6c3c7c6e05ef5bf3010a24c054a0ca04a70307c9ffb"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def jamcoin(coin_size, group_size, positions):\n",
      "    coin = [0] * coin_size\n",
      "    for i, pos in enumerate(positions):\n",
      "        coin[pos:pos+group_size] = [1] * group_size\n",
      "    divisors = map(lambda s : ((s ** group_size) - 1) / (s - 1), range(2,11))\n",
      "    return \"\".join(map(str, coin))[::-1] + \" \" + \" \".join(map(str, divisors))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 116
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "from itertools import combinations, chain\n",
      "\n",
      "def powerset(iterable):\n",
      "    s = list(iterable)\n",
      "    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))\n",
      "\n",
      "def find_jamcoins(N, J):\n",
      "    pair_positions = map(lambda x : x * 2, range(1, (N/2) - 1))\n",
      "    p = powerset(pair_positions)\n",
      "    p.next() # empty group\n",
      "    output = \"\"\n",
      "    for i in xrange(0, J):\n",
      "        positions = p.next()\n",
      "        positions = [0] + list(positions) + [(N - 1]\n",
      "        assert len(positions) > 0\n",
      "        print positions\n",
      "        output += jamcoin(N, 2, positions) + \"\\n\"\n",
      "    \n",
      "    return output\n",
      "\n",
      "print find_jamcoins(16, 5)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[0, 2, 7]\n",
        "[0, 4, 7]\n",
        "[0, 6, 7]\n",
        "[0, 8, 7]\n",
        "[0, 10, 7]\n",
        "0000000110001111 3 4 5 6 7 8 9 10 11\n",
        "0000000110110011 3 4 5 6 7 8 9 10 11\n",
        "0000000111000011 3 4 5 6 7 8 9 10 11\n",
        "0000001110000011 3 4 5 6 7 8 9 10 11\n",
        "0000110110000011 3 4 5 6 7 8 9 10 11\n",
        "\n"
       ]
      }
     ],
     "prompt_number": 125
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "pair_positions = map(lambda x : x * 2, range(0, (16/2)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 99
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "p = powerset(pair_positions)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 97
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "out = find_jamcoins(16,50)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 120
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "for l in out.splitlines():\n",
      "    b = l.split()\n",
      "    for d in xrange(2,11):\n",
      "        num = int(b[0], d)\n",
      "        div = int(b[d - 1])\n",
      "        if num % div != 0:\n",
      "            print \"Looo!\""
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 121
    },
    {
     "cell_type": "code",
     "collapsed": true,
     "input": [
      "Header = \"Case #1:\\n\"\n",
      "open(r\"C:\\Users\\Vladimir Anisimov\\Documents\\Programming\\CodeJam\\q3.small.out\", \"w\").write(Header + find_jamcoins(16, 50))\n",
      "open(r\"C:\\Users\\Vladimir Anisimov\\Documents\\Programming\\CodeJam\\q3.large.out\", \"w\").write(Header + find_jamcoins(32, 500))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 114
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "len(open(r\"C:\\Users\\Vladimir Anisimov\\Documents\\Programming\\CodeJam\\q3.small.out\").readlines())"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 115,
       "text": [
        "51"
       ]
      }
     ],
     "prompt_number": 115
    }
   ],
   "metadata": {}
  }
 ]
}