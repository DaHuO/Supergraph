{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# GOOGLE JAM 16"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Problem A. Counting Sheep"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def digitsOfNumber(number):\n",
    "    return np.asarray(list(str(number)))\n",
    "\n",
    "def getNumberIteration(number):\n",
    "    liste = set([])\n",
    "    n=0\n",
    "    r=np.arange(10).astype(str)\n",
    "    \n",
    "    if(number==0):\n",
    "        return \"INSOMNIA\"\n",
    "    \n",
    "    \n",
    "    while(len(liste)<10):\n",
    "        n+=number\n",
    "        X = digitsOfNumber(n)\n",
    "        for i in r:\n",
    "            if(((X==i).sum())>0):\n",
    "                liste.add(i)\n",
    "    return (str(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "args = [int(i) for i in open(\"../Downloads/A-large.in\",\"r\").read().splitlines()][1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "%%time\n",
    "from multiprocessing import Pool\n",
    "pool = Pool()\n",
    "results = pool.map(getNumberIteration, args)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "file = open(\"google_sheep.txt\", \"w\")\n",
    "\n",
    "for idx,i in enumerate(results):\n",
    "    s=\"Case #\"+str(idx+1)+\": \"+i+\"\\n\"\n",
    "    file.write(s)\n",
    "\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Problem B. Revenge of the Pancakes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def stringtoarray(string):\n",
    "    dico={\"+\":True,\"-\":False}\n",
    "    return np.array([dico[i] for i in string])\n",
    "\n",
    "def pancake(string):\n",
    "    tab=stringtoarray(string)\n",
    "    cnt=0\n",
    "    T=len(tab)\n",
    "    while(tab.sum()<T):\n",
    "        if(tab.sum()==0):\n",
    "            return str(cnt+1)\n",
    "        cnt+=1\n",
    "        first=tab[0]\n",
    "        ind=np.nonzero(tab==(not(first)))[0][0]\n",
    "        if first:\n",
    "            a=np.zeros(ind)\n",
    "        else:\n",
    "            a=np.ones(ind)\n",
    "        b=tab[ind:]\n",
    "        tab = np.concatenate((a,b), axis=0)\n",
    "    return str(cnt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string=\"++--\"\n",
    "pancake(string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "args2 = [i for i in open(\"../Downloads/B-small-attempt1.in\",\"r\").read().splitlines()][1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CPU times: user 5.79 ms, sys: 12.7 ms, total: 18.4 ms\n",
      "Wall time: 25.6 ms\n"
     ]
    }
   ],
   "source": [
    "%%time\n",
    "from multiprocessing import Pool\n",
    "pool = Pool()\n",
    "results = pool.map(pancake, args2)"
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
    "file = open(\"google_B.txt\", \"w\")\n",
    "\n",
    "for idx,i in enumerate(results):\n",
    "    s=\"Case #\"+str(idx+1)+\": \"+i+\"\\n\"\n",
    "    file.write(s)\n",
    "\n",
    "file.close()"
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
