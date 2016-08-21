{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {
    "collapsed": false
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
    "fname = 'B-small-attempt0.in'\n",
    "data = ReadInts(fname)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "------------------------Question 2------------------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: 1\n",
      "Case #2: 1\n",
      "Case #3: 2\n",
      "Case #4: 0\n",
      "Case #5: 3\n",
      "Case #6: 6\n",
      "Case #7: 4\n",
      "Case #8: 5\n",
      "Case #9: 5\n",
      "Case #10: 5\n",
      "Case #11: 3\n",
      "Case #12: 4\n",
      "Case #13: 7\n",
      "Case #14: 5\n",
      "Case #15: 6\n",
      "Case #16: 0\n",
      "Case #17: 2\n",
      "Case #18: 5\n",
      "Case #19: 0\n",
      "Case #20: 2\n",
      "Case #21: 7\n",
      "Case #22: 7\n",
      "Case #23: 1\n",
      "Case #24: 1\n",
      "Case #25: 4\n",
      "Case #26: 3\n",
      "Case #27: 5\n",
      "Case #28: 3\n",
      "Case #29: 4\n",
      "Case #30: 3\n",
      "Case #31: 6\n",
      "Case #32: 5\n",
      "Case #33: 1\n",
      "Case #34: 7\n",
      "Case #35: 6\n",
      "Case #36: 1\n",
      "Case #37: 4\n",
      "Case #38: 5\n",
      "Case #39: 6\n",
      "Case #40: 2\n",
      "Case #41: 3\n",
      "Case #42: 10\n",
      "Case #43: 0\n",
      "Case #44: 5\n",
      "Case #45: 1\n",
      "Case #46: 6\n",
      "Case #47: 4\n",
      "Case #48: 8\n",
      "Case #49: 2\n",
      "Case #50: 1\n",
      "Case #51: 0\n",
      "Case #52: 2\n",
      "Case #53: 4\n",
      "Case #54: 1\n",
      "Case #55: 6\n",
      "Case #56: 2\n",
      "Case #57: 2\n",
      "Case #58: 5\n",
      "Case #59: 4\n",
      "Case #60: 1\n",
      "Case #61: 4\n",
      "Case #62: 2\n",
      "Case #63: 3\n",
      "Case #64: 4\n",
      "Case #65: 2\n",
      "Case #66: 3\n",
      "Case #67: 5\n",
      "Case #68: 3\n",
      "Case #69: 3\n",
      "Case #70: 5\n",
      "Case #71: 7\n",
      "Case #72: 5\n",
      "Case #73: 3\n",
      "Case #74: 4\n",
      "Case #75: 6\n",
      "Case #76: 2\n",
      "Case #77: 6\n",
      "Case #78: 4\n",
      "Case #79: 5\n",
      "Case #80: 6\n",
      "Case #81: 5\n",
      "Case #82: 2\n",
      "Case #83: 3\n",
      "Case #84: 8\n",
      "Case #85: 3\n",
      "Case #86: 9\n",
      "Case #87: 6\n",
      "Case #88: 5\n",
      "Case #89: 5\n",
      "Case #90: 6\n",
      "Case #91: 3\n",
      "Case #92: 2\n",
      "Case #93: 1\n",
      "Case #94: 6\n",
      "Case #95: 3\n",
      "Case #96: 2\n",
      "Case #97: 5\n",
      "Case #98: 5\n",
      "Case #99: 5\n",
      "Case #100: 7\n"
     ]
    }
   ],
   "source": [
    "N = int(data[0])\n",
    "for i in range(0, N):\n",
    "    pancakes = data[i+1]\n",
    "    pancake_list = list(pancakes)\n",
    "    value = compute_flips(pancake_list, len(pancake_list))    \n",
    "    print 'Case #%d: %d' %((i+1), value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def compute_flips(pancakes, length):\n",
    "    if pancakes[0] == '+':\n",
    "        s_front = symbol_at_the_front(pancakes, length, '+')\n",
    "        if s_front == length:\n",
    "            return 0\n",
    "        return 1 + compute_flips(pancakes[s_front:], length-s_front)\n",
    "    else:\n",
    "        s_front = symbol_at_the_front(pancakes, length, '-')\n",
    "        s_end = symbol_at_the_end(pancakes, length, '+')\n",
    "        if s_front == length-s_end:\n",
    "            return 1\n",
    "        new_length = length-s_front-s_end\n",
    "        flip_s = flip_str(pancakes[s_front:length-s_end], new_length)\n",
    "        return 1 + compute_flips(flip_s, new_length)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def symbol_at_the_end(pancakes, length, op):\n",
    "    count = 0\n",
    "    i = length-1\n",
    "    char = pancakes[i]\n",
    "    while i>=0 and char == op:      \n",
    "        count = count+1\n",
    "        i = i - 1\n",
    "        char = pancakes[i]\n",
    "    return count\n",
    "\n",
    "def symbol_at_the_front(pancakes, length, op):\n",
    "    count = 0\n",
    "    i = 0\n",
    "    char = pancakes[i]\n",
    "    while i < length and char == op:\n",
    "        count = count+1\n",
    "        i = i + 1\n",
    "        if i < length:\n",
    "            char = pancakes[i]\n",
    "    return count\n",
    "\n",
    "def flip_str(pancakes, length):\n",
    "    str_flip = list()\n",
    "    for i in range(length-1, -1, -1):\n",
    "        if pancakes[i] == '+':\n",
    "            str_flip.append('-')\n",
    "        else:\n",
    "            str_flip.append('+')\n",
    "    return str_flip"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "------------------------Question 1------------------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "N = int(data[0])\n",
    "for i in range(0, N):\n",
    "    value = compute_repeats(data[i+1])\n",
    "    print 'Case #%s: %s' %((i+1), value)\n",
    "    \n",
    "def compute_repeats(num):\n",
    "    if num == '0':\n",
    "        return 'INSOMNIA'\n",
    "    A = set({'0','1','2','3','4','5','6','7','8','9'})\n",
    "    tempInt = int(num)\n",
    "    numInt = int(num)\n",
    "    while len(A) != 0:\n",
    "        tempStr = str(tempInt)\n",
    "        for i in range(0, len(tempStr)):\n",
    "            if tempStr[i] in A:\n",
    "                A.remove(tempStr[i])\n",
    "        tempInt = tempInt + numInt \n",
    "    tempInt = tempInt-numInt\n",
    "    return str(tempInt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
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
