{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# imports\n",
    "import numpy as np # http://www.numpy.org/\n",
    "import math # https://docs.python.org/2/library/math.html\n",
    "import itertools as it # https://docs.python.org/2/library/itertools.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "basepath = '/home/epg/halde/codejam/2016/2/A/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "testset = 'A-small-attempt1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def completes(s):\n",
    "    r = s\n",
    "    while len(r) > 1:\n",
    "        next_round = ''\n",
    "        for i in xrange(len(r)/2):\n",
    "            c1 = r[2*i]\n",
    "            c2 = r[2*i+1]\n",
    "            \n",
    "            if c1 == c2:\n",
    "                # tie\n",
    "                return False\n",
    "            elif c1+c2 in ['PR', 'RP']:\n",
    "                next_round += 'P'\n",
    "            elif c1+c2 in ['PS', 'SP']:\n",
    "                next_round += 'S'\n",
    "            elif c1+c2 in ['RS', 'SR']:\n",
    "                next_round += 'R'\n",
    "        r = next_round\n",
    "    return True\n",
    "\n",
    "def do_solve(N, R, P, S):\n",
    "    # tie unavoidable in first round\n",
    "    if P + R < S or P + S < R or R + S < P:\n",
    "        return 'IMPOSSIBLE'\n",
    "    # tie unavoidable in later round\n",
    "    if N > 1:\n",
    "        if P == 0 or R == 0 or S == 0:\n",
    "            return 'IMPOSSIBLE'\n",
    "    \n",
    "    start = ''\n",
    "    # remaining values\n",
    "    p = P\n",
    "    r = R\n",
    "    s = S\n",
    "    # choose smallest possible start character\n",
    "    if P > 0:\n",
    "        start += 'P'\n",
    "        p -= 1\n",
    "    else:\n",
    "        # R and S exist\n",
    "        start += 'R'\n",
    "        r -= 1\n",
    "    for p in it.permutations('P'*p + 'R'*r + 'S'*s, 2**N-1):\n",
    "        res = start + ''.join(p)\n",
    "        if completes(res):\n",
    "            return res\n",
    "    \n",
    "    return 'IMPOSSIBLE'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: PR\n",
      "Case #2: IMPOSSIBLE\n",
      "Case #3: PSRS\n",
      "Case #4: IMPOSSIBLE\n",
      "Case #5: RS\n",
      "Case #6: IMPOSSIBLE\n",
      "Case #7: IMPOSSIBLE\n",
      "Case #8: PRRS\n",
      "Case #9: IMPOSSIBLE\n",
      "Case #10: IMPOSSIBLE\n",
      "Case #11: PRRSPSRS\n",
      "Case #12: IMPOSSIBLE\n",
      "Case #13: PS\n",
      "Case #14: IMPOSSIBLE\n",
      "Case #15: IMPOSSIBLE\n",
      "Case #16: PRPSPSRS\n",
      "Case #17: IMPOSSIBLE\n",
      "Case #18: IMPOSSIBLE\n",
      "Case #19: IMPOSSIBLE\n",
      "Case #20: IMPOSSIBLE\n",
      "Case #21: IMPOSSIBLE\n",
      "Case #22: PRPSPRRS\n",
      "Case #23: PRPS\n",
      "Case #24: IMPOSSIBLE\n",
      "Case #25: IMPOSSIBLE\n"
     ]
    }
   ],
   "source": [
    "with open(basepath + testset + '.in') as fin, open(basepath + testset + '.out', 'w') as fout:\n",
    "    T = int(fin.readline().rstrip('\\r\\n'))\n",
    "    for i in xrange(T):\n",
    "        N, R, P, S = tuple(map(int, fin.readline().rstrip('\\r\\n').split(' ')))\n",
    "        \n",
    "        sol = do_solve(N, R, P, S)\n",
    "        \n",
    "        sol_string = 'Case #{}: {}'.format(i+1, sol)\n",
    "        fout.write(sol_string + '\\n')\n",
    "        print sol_string"
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
   "language": "python2",
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
