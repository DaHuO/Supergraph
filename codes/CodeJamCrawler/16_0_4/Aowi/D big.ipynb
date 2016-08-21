{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from math import ceil\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def art(K, C, S):\n",
    "    if C * S < K:\n",
    "        return 'IMPOSSIBLE'\n",
    "    \n",
    "    if C == 1:\n",
    "        return ' '.join([str(_) for _ in range(1, K + 1)])\n",
    "    \n",
    "    k_power = np.zeros(C, dtype = np.int64)\n",
    "    k_power[0] = 1\n",
    "    for k in range(1, C):\n",
    "        k_power[k] = K * k_power[k - 1]\n",
    "    \n",
    "    check = []\n",
    "    i = 1\n",
    "    while i <= K:\n",
    "        elem = 1\n",
    "        elem += (i - 1) * k_power[C - 1]\n",
    "        for j in range(i + 1, min(i + C - 1, K) + 1):\n",
    "            elem += k_power[C - 1 - (j - i)] * (j - 1)\n",
    "        check.append(elem)\n",
    "        i += C\n",
    "\n",
    "    return ' '.join([str(_) for _ in check])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "inp = open(\"D-large.in\")\n",
    "out = open(\"output.txt\", 'w')\n",
    "num = int(inp.readline())\n",
    "for i in range(num):\n",
    "    (K, C, S) = [int(x) for x in inp.readline().strip().split()]\n",
    "    out.write('Case #' + str(i+1) + ': ' + art(K, C, S) + '\\n')\n",
    "inp.close()\n",
    "out.close()"
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
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
