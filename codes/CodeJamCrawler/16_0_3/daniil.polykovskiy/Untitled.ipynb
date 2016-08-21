{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import sys\n",
    "import itertools"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def is_prime(a):\n",
    "    if a == 2:\n",
    "        return True\n",
    "    if a % 2 == 0:\n",
    "        return False\n",
    "    i = 3\n",
    "    while i*i <= a:\n",
    "        if a % i == 0:\n",
    "            return False\n",
    "        i += 2\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def divisor(a):\n",
    "    if a == 2:\n",
    "        return -1\n",
    "    if a % 2 == 0:\n",
    "        return 2\n",
    "    i = 3\n",
    "    while i*i <= a:\n",
    "        if a % i == 0:\n",
    "            return i\n",
    "        i += 2\n",
    "    return -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def tojam(a, N):\n",
    "    a = bin(a)[2:]\n",
    "    a = '1'+'0'*(N-len(a)-2)+a+'1'\n",
    "    return a\n",
    "\n",
    "def jam(a, N, verbose=False):\n",
    "    a = tojam(a, N)\n",
    "    for i in range(2, 11):\n",
    "        if is_prime(int(a, i)):\n",
    "            if verbose:\n",
    "                print(a, int(a, i), is_prime(int(a, i)))\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def jam_proof(a, N):\n",
    "    a = tojam(a, N)\n",
    "    divs = [divisor(int(a, i)) for i in range(2, 10)]\n",
    "    return a+' '+' '.join(map(str, divs))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1:\n",
      "100001 3 2 5 2 7 2 3 2\n",
      "100011 5 13 3 31 43 3 73 7\n",
      "100111 3 2 5 2 7 2 3 2\n"
     ]
    }
   ],
   "source": [
    "N = 6\n",
    "k = 3\n",
    "r = []\n",
    "print(\"Case #1:\")\n",
    "for a in range(2**(N-2)):\n",
    "    if jam(a, N):\n",
    "        r.append(jam_proof(a, N))\n",
    "        sys.stdout.write(r[-1]+'\\n')\n",
    "        sys.stdout.flush()\n",
    "        if len(r) == k:\n",
    "            break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32947 47 0\n",
      "14351422 2 0\n",
      "1073759493 3 0\n",
      "30517660006 2 0\n",
      "470185273591 11 0\n",
      "4747562352702 2 0\n",
      "35184374222857 204311 0\n",
      "205891136943238 2 0\n"
     ]
    }
   ],
   "source": [
    "r = '1000000010110011'\n",
    "for i in range(2, 10):\n",
    "    print(int(r, i), divisor(int(r, i)), end=' ')\n",
    "    print(int(r, i)%divisor(int(r, i)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jam(int('1001', 2), 6, True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int('1011', 2)"
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
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.4"
  },
  "latex_envs": {
   "bibliofile": "biblio.bib",
   "cite_by": "apalike",
   "current_citInitial": 1,
   "eqLabelWithNumbers": true,
   "eqNumInitial": 0
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
