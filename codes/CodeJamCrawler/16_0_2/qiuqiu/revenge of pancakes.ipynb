{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ch = '--++'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def upsidedown(mystr):\n",
    "    mystr = mystr[::-1]\n",
    "    return  ['+' if _ch=='-' else '-' for _ch in mystr ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def stop(ch):\n",
    "    return set(ch)==set('+')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from collections import Counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def most_items(ch):\n",
    "    ct = Counter(ch)\n",
    "    if ct['+'] > ct['-']:\n",
    "        return 1\n",
    "    else:\n",
    "        return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "most_items(ch)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def search_neg_after_pos(ch):\n",
    "    i=0\n",
    "    max_i = len(ch)-1\n",
    "    while  (i<= max_i) and (ch[i]=='+'):\n",
    "        i+=1\n",
    "\n",
    "    while (i<= max_i)and (ch[i]=='-')  :\n",
    "        i+=1\n",
    "    if i > max_i:\n",
    "    #end with a +\n",
    "        return ''\n",
    "    else:\n",
    "        return ch[i:]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def search_pos_after_neg(ch):\n",
    "    i=0\n",
    "    max_i = len(ch)-1\n",
    "    while  (i<= max_i) and (ch[i]=='-'):\n",
    "        i+=1\n",
    "\n",
    "    while (i<= max_i)and (ch[i]=='+')  :\n",
    "        i+=1\n",
    "    if i > max_i:\n",
    "    #end with a +\n",
    "        return ''\n",
    "    else:\n",
    "        return ch[i:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 259,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "search_neg_after_pos('+++---')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'--'"
      ]
     },
     "execution_count": 261,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "search_pos_after_neg('--++--')"
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
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def pattern_posneg_leftright(ch):\n",
    "    it = 0\n",
    "    while len(ch):\n",
    "        ch = search_neg_after_pos(ch)\n",
    "        it += 2\n",
    "    return it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def pattern_negpos_leftright(ch):\n",
    "    it = 0\n",
    "    while len(ch) and set(ch)!=set('-'):\n",
    "        ch = search_pos_after_neg(ch)\n",
    "        it += 2\n",
    "    return it+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def algo(ch):\n",
    "    nb_mv = 0\n",
    "    ch  = list(ch)\n",
    "    if set(ch)==set('+'):\n",
    "        pass\n",
    "    else:  #shoud do someth\n",
    "        while ch[-1]=='+':      #if last is +, then leave it, treate top. so after this, last charact = '-'\n",
    "            ch = ch[:-1]\n",
    "        \n",
    "        #last ='-', so watch first, if first='+', then swtich to '-', then reverse all; if not,\n",
    "        if set(ch)==set('-'):  # only -\n",
    "            nb_mv = 1\n",
    "        else:\n",
    "            if ch[0]=='+':\n",
    "                nb_mv = pattern_posneg_leftright(ch)\n",
    "            else:\n",
    "                nb_mv = pattern_negpos_leftright(ch)\n",
    "    return nb_mv\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def run(infile, outfile):\n",
    "    with open(outfile,'w') as g:\n",
    "        i = 0\n",
    "        for line in open(infile,'r'):\n",
    "            line = line.strip()\n",
    "            if i==0:\n",
    "                pass\n",
    "            else:\n",
    "                tmp_res = \"case #\" +str(i)+': '+ str(algo(line)) +'\\n'\n",
    "                g.write(tmp_res )\n",
    "            i+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 295,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "infile = '/Users/mac/Downloads/B-small-attempt0.in'\n",
    "outfile = '/Users/mac/Downloads/pancake.txt'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 296,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "run(infile,outfile)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 297,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\r\n",
      "-\r\n",
      "-+\r\n",
      "+-\r\n",
      "+++\r\n",
      "--+-\r\n",
      "--+-+--+\r\n",
      "-----\r\n",
      "-++--+++-+\r\n",
      "-++++---++\r\n",
      "+--\r\n",
      "++-+++---+\r\n",
      "++-++--+-+\r\n",
      "+--+-+--\r\n",
      "--++--+-+-\r\n",
      "+-+----\r\n",
      "+-+\r\n",
      "---\r\n",
      "--+-+-+--+\r\n",
      "+---\r\n",
      "-++---++++\r\n",
      "-++-++-+++\r\n",
      "++-+\r\n",
      "--+--+++++\r\n",
      "++\r\n",
      "++--\r\n",
      "-+--+-----\r\n",
      "-++-++--++\r\n",
      "+-+++-----\r\n",
      "--+--+-+--\r\n",
      "-++-+--+-+\r\n",
      "----\r\n",
      "++-+---++-\r\n",
      "++--++\r\n",
      "--++\r\n",
      "+-+---+-\r\n",
      "-++++---+-\r\n",
      "++-\r\n",
      "-+-\r\n",
      "+++-\r\n",
      "++-+++-++-\r\n",
      "+++-+-+++-\r\n",
      "+-++-++---\r\n",
      "+--------+\r\n",
      "+-+-++-+--\r\n",
      "++++-+-+--\r\n",
      "-+-+-+-+--\r\n",
      "----+-++++\r\n",
      "+\r\n",
      "+-+-+-+-+-\r\n",
      "+-+-+---+-\r\n",
      "++--+-+-+-\r\n",
      "+--++++--+\r\n",
      "--\r\n",
      "+--+\r\n",
      "-++--++-++\r\n",
      "+-+-+++-\r\n",
      "-+--+-+-++\r\n",
      "-+-++-++-+\r\n",
      "+-++\r\n",
      "+--++-+-+-\r\n",
      "-+--+--+--\r\n",
      "---+-++---\r\n",
      "-++++++++-\r\n",
      "+----+\r\n",
      "+---+-+--+\r\n",
      "-+-+--+--\r\n",
      "-+--\r\n",
      "+-+-\r\n",
      "-+++\r\n",
      "++++++-+--\r\n",
      "-++\r\n",
      "---+\r\n",
      "+-++-+-+-\r\n",
      "----++-\r\n",
      "+-+-+--++-\r\n",
      "--++-++\r\n",
      "++++\r\n",
      "+-+++++\r\n",
      "-+-+\r\n",
      "--+++--+--\r\n",
      "-+--+\r\n",
      "++----+++-\r\n",
      "-++-\r\n",
      "-+---++---\r\n",
      "+++++\r\n",
      "----+----\r\n",
      "+++-+-++-+\r\n",
      "--+\r\n",
      "-+-+-+-+-+\r\n",
      "+++---+\r\n",
      "++-+---+-+\r\n",
      "++-+--+-++\r\n",
      "-++-++---+\r\n",
      "+++++-+\r\n",
      "--++----+-\r\n",
      "---+++++\r\n",
      "+-++-----+\r\n",
      "++++-++++-\r\n",
      "-+++-+\r\n",
      "--+--+-+-+\r\n"
     ]
    }
   ],
   "source": [
    "!cat {infile}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 298,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "case #1: 1\r\n",
      "case #2: 1\r\n",
      "case #3: 2\r\n",
      "case #4: 0\r\n",
      "case #5: 3\r\n",
      "case #6: 5\r\n",
      "case #7: 1\r\n",
      "case #8: 5\r\n",
      "case #9: 3\r\n",
      "case #10: 2\r\n",
      "case #11: 4\r\n",
      "case #12: 6\r\n",
      "case #13: 6\r\n",
      "case #14: 7\r\n",
      "case #15: 4\r\n",
      "case #16: 2\r\n",
      "case #17: 1\r\n",
      "case #18: 7\r\n",
      "case #19: 2\r\n",
      "case #20: 3\r\n",
      "case #21: 5\r\n",
      "case #22: 2\r\n",
      "case #23: 3\r\n",
      "case #24: 0\r\n",
      "case #25: 2\r\n",
      "case #26: 5\r\n",
      "case #27: 5\r\n",
      "case #28: 4\r\n",
      "case #29: 7\r\n",
      "case #30: 7\r\n",
      "case #31: 1\r\n",
      "case #32: 6\r\n",
      "case #33: 2\r\n",
      "case #34: 1\r\n",
      "case #35: 6\r\n",
      "case #36: 5\r\n",
      "case #37: 2\r\n",
      "case #38: 3\r\n",
      "case #39: 2\r\n",
      "case #40: 6\r\n",
      "case #41: 6\r\n",
      "case #42: 6\r\n",
      "case #43: 2\r\n",
      "case #44: 8\r\n",
      "case #45: 6\r\n",
      "case #46: 9\r\n",
      "case #47: 3\r\n",
      "case #48: 0\r\n",
      "case #49: 10\r\n",
      "case #50: 8\r\n",
      "case #51: 8\r\n",
      "case #52: 4\r\n",
      "case #53: 1\r\n",
      "case #54: 2\r\n",
      "case #55: 5\r\n",
      "case #56: 6\r\n",
      "case #57: 7\r\n",
      "case #58: 7\r\n",
      "case #59: 2\r\n",
      "case #60: 8\r\n",
      "case #61: 7\r\n",
      "case #62: 5\r\n",
      "case #63: 3\r\n",
      "case #64: 2\r\n",
      "case #65: 6\r\n",
      "case #66: 7\r\n",
      "case #67: 3\r\n",
      "case #68: 4\r\n",
      "case #69: 1\r\n",
      "case #70: 4\r\n",
      "case #71: 1\r\n",
      "case #72: 1\r\n",
      "case #73: 8\r\n",
      "case #74: 3\r\n",
      "case #75: 8\r\n",
      "case #76: 3\r\n",
      "case #77: 0\r\n",
      "case #78: 2\r\n",
      "case #79: 3\r\n",
      "case #80: 5\r\n",
      "case #81: 3\r\n",
      "case #82: 4\r\n",
      "case #83: 3\r\n",
      "case #84: 5\r\n",
      "case #85: 0\r\n",
      "case #86: 3\r\n",
      "case #87: 6\r\n",
      "case #88: 1\r\n",
      "case #89: 9\r\n",
      "case #90: 2\r\n",
      "case #91: 6\r\n",
      "case #92: 6\r\n",
      "case #93: 5\r\n",
      "case #94: 2\r\n",
      "case #95: 5\r\n",
      "case #96: 1\r\n",
      "case #97: 4\r\n",
      "case #98: 4\r\n",
      "case #99: 3\r\n",
      "case #100: 7\r\n"
     ]
    }
   ],
   "source": [
    "!cat {outfile}"
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
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
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
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
