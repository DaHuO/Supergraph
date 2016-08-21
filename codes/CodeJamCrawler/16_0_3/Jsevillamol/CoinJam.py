# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 11:33:24 2016

@author: jsevillamol
"""

from random import randint
from math import sqrt
from numpy.random import geometric

initial_fitness = 100
reward_fitness = 10
n_population = 1

def gen_coin_jam(size, how_many):
    solutions = set()
    
    population = []
    while len(population)<n_population:
        cand = coin_jam_candidate(size)
        if not cand in population:
            population.append(cand)
    
    #kill_count = 0
    while len(solutions) < how_many:
        #TODO: pick a random individual from population according to fitness
        challenger = population.pop()
        challenger.prove_yourself()
        if len(challenger.proof) == 9:
            solutions.add(challenger)
            print("Solutions found: {}".format(len(solutions)))
            candidate = coin_jam_candidate(size)
            while candidate in population or candidate in solutions:
                candidate = coin_jam_candidate(size)
            population.append(candidate)
        elif challenger.fitness > 0:
            population.append(challenger)
        else:
            candidate = coin_jam_candidate(size)
            while (candidate in population) or (candidate in solutions):
                candidate = coin_jam_candidate(size)
            population.append(candidate)
            #kill_count += 1
    #print("Dead challengers: {}".format(kill_count))
    return solutions

class coin_jam_candidate:
    def __init__(self, size): #TODO: are mutations efficient?
        self.coin = coin_seed(size)
        self.proof = []
        self.fitness = coin_jam_candidate.new_fitness()
    
    def prove_yourself(self):
        self.fitness -= 1
        n = int(self.coin, len(self.proof)+2)
        # Pick random number to try dividing
        candidate_factor = random_candidate(int(sqrt(n)))
        if n%candidate_factor == 0:
            self.fitness += coin_jam_candidate.reward_fitness()
            self.proof.append(candidate_factor)
            
    def and_we_have_a_winner(self):
        if len(self.proof)<9:
            return False
        for i in range(2,11):
            n = int(self.coin, i)
            if n%self.proof[i-2] != 0\
            or n==self.proof[i-2] or self.proof[i-2]==1:
                return False
        return True
        
    def __hash__(self):
        return hash(self.coin)
    
    def __eq__(self, other):
        return self.coin == other.coin
        
    fitness_counter = initial_fitness
    def new_fitness():
        coin_jam_candidate.fitness_counter += 1
        return coin_jam_candidate.fitness_counter
    
    def reward_fitness():
        return coin_jam_candidate.fitness_counter

def coin_seed(size):
    return "1"+ "".join([str(randint(0,1)) for i in range(size-2)]) + "1"

def random_candidate(max_n):
    candidate = 2
    while candidate % 2 == 0 or candidate < 3 or candidate > max_n:
        #candidate = randint(3, max_n)
        candidate = geometric(2/max_n)
    return candidate
    

def mutate(parent):
    raise NotImplemented

if True:
    with open("out.txt", 'w') as out:
        out.write("Case #1:\n")
        sol = gen_coin_jam(16, 50)
        for coin_jam, proof in [(x.coin, x.proof) for x in sol]:
            out.write("{}".format(coin_jam))
            for factor in proof:
                out.write(" {}".format(factor))
            out.write("\n")

from time import time
from statistics import mean

if True:
    with open("out.txt", 'r') as file:
        file.readline()
        c = coin_jam_candidate(16)
        coins = []
        for line in file:
            s = line.split()
            c.coin = s[0]
            c.proof = [int(i) for i in s[1:]]
            print(c.and_we_have_a_winner() and not c.coin in coins)
            coins.append(c.coin)

def test():
    difficulty = 17
    trials = 10
    how_many = 10
    for i in range(10, difficulty):
        times = []
        for j in range(trials):
            i_time = time()
            gen_coin_jam(i, how_many)
            a_time = time()
            times.append(a_time-i_time)
        print("Size: {} Time: {}".format(i, mean(times)))