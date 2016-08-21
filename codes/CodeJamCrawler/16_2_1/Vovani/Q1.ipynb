{
 "metadata": {
  "name": "",
  "signature": "sha256:2e444f9f7ec5b7ed30e9c1e4a6fc35d653acaf6a6d784085215ea61107919bc1"
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
      "layers = [{\n",
      "    'Z' : (\"ZERO\", 0),\n",
      "    'W' : (\"TWO\", 2),\n",
      "    'U' : (\"FOUR\", 4),\n",
      "    'X' : (\"SIX\", 6),\n",
      "    'G' : (\"EIGHT\", 8)\n",
      "}, {\n",
      "    'O' : ('ONE', 1),\n",
      "    'T' : ('THREE', 3),\n",
      "    'F' : ('FIVE', 5),\n",
      "    'S' : ('SEVEN', 7)\n",
      "}, {\n",
      "'N' : ('NINE', 9)\n",
      "}]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 2
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def count_letters(s):\n",
      "    rv = {}\n",
      "    for c in s:\n",
      "        rv[c] = rv.get(c, 0) + 1\n",
      "    return rv\n",
      "\n",
      "def fetch_digits(s):\n",
      "    letter_count = count_letters(s)\n",
      "    digits = []\n",
      "    for layer in layers:\n",
      "        for key in layer.keys():\n",
      "            times = letter_count.get(key, 0)\n",
      "            if times == 0:\n",
      "                continue\n",
      "            info = layer[key]\n",
      "            dig_letters = count_letters(info[0])\n",
      "            real_times = []\n",
      "            for let in dig_letters.iteritems():\n",
      "                real_times.append(letter_count[let[0]] / let[1])\n",
      "            real_times = min(real_times)\n",
      "            for let in dig_letters.iteritems():\n",
      "                letter_count[let[0]] -= times\n",
      "            digits.extend([info[1],] * real_times)\n",
      "    \n",
      "    assert(len(filter(lambda x : x != 0, letter_count.values())) == 0)\n",
      "    return sorted(digits)\n",
      "        "
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 59
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = open(r\"C:\\Users\\Vladimir Anisimov\\Documents\\Programming\\CodeJam\\Round1\\A-large (1).in\")\n",
      "res = open(r\"C:\\Users\\Vladimir Anisimov\\Documents\\Programming\\CodeJam\\Round1\\q1__large_out.txt\", \"w\")\n",
      "T = int(f.readline())\n",
      "counter = 0\n",
      "for s in f.readlines():\n",
      "    res.write(\"Case #\" + str(counter + 1) + \": \" + \"\".join(map(str, fetch_digits(s))) + \"\\n\")\n",
      "    counter += 1\n",
      "    \n",
      "assert(counter == T)\n",
      "print T\n",
      "res.flush()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "AssertionError",
       "evalue": "",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[1;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
        "\u001b[1;32m<ipython-input-60-c563b38c6ad2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mcounter\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0ms\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreadlines\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m     \u001b[0mres\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Case #\"\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcounter\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m\": \"\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m\"\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mjoin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmap\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfetch_digits\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m\"\\n\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m     \u001b[0mcounter\u001b[0m \u001b[1;33m+=\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
        "\u001b[1;32m<ipython-input-59-0a8884314f56>\u001b[0m in \u001b[0;36mfetch_digits\u001b[1;34m(s)\u001b[0m\n\u001b[0;32m     23\u001b[0m             \u001b[0mdigits\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mextend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0minfo\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m*\u001b[0m \u001b[0mreal_times\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     24\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 25\u001b[1;33m     \u001b[1;32massert\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;32mlambda\u001b[0m \u001b[0mx\u001b[0m \u001b[1;33m:\u001b[0m \u001b[0mx\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mletter_count\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     26\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0msorted\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdigits\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     27\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
        "\u001b[1;31mAssertionError\u001b[0m: "
       ]
      }
     ],
     "prompt_number": 60
    }
   ],
   "metadata": {}
  }
 ]
}