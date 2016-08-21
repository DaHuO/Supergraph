'''
Created on Apr 9, 2016

@author: david
'''
#f=open("exampleA.txt")
f=open("A-small-attempt0.in")
#f=open("A-large.in")

word = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def contained(dic, cad):
    for elem in cad:
        if elem not in dic: return False
        dic[elem] -= 1
        if dic[elem] == 0:
            del dic[elem]
    return True
                
from abc import ABCMeta, abstractmethod

class IForwardStateSpace(metaclass=ABCMeta): 
    @abstractmethod
    def initial_states(self) -> "Iterable<State>": pass

    @abstractmethod
    def is_final(self, s: "State") -> "bool": pass

    @abstractmethod
    def decisions(self, s: "State") -> "Iterable<Decision>": pass

    @abstractmethod
    def decide(self, s: "State", d: "Decision") -> "State": pass 

class IReversibleForwardStateSpace(IForwardStateSpace):
    @abstractmethod
    def undo(self, s:"State", d: "Decision") -> "State": pass 

class BacktrackingEnumerator: 
    def __init__(self, createSolution: "(StateSpace, (IList<Decisions>, State) -> Solution"
                = lambda space, initial, decisions, final: (initial, tuple(decisions), final)):
        self.createSolution = createSolution
        
    def enumerate(self, space: "IForwardStateSpace") -> "Iterable<Solution>":
        def backtracking(state: "State") -> "Iterable<Solution>":
            if space.is_final(state): 
                yield self.createSolution(space, initial, decisions, state)
            seen.add(state)
            for decision in space.decisions(state):
                decisions.append(decision)
                successor = space.decide(state, decision)
                if successor not in seen:
                    for result in backtracking(successor): 
                        yield result
                if reversible:
                    state = space.undo(successor, decision)
                decisions.pop()
        
        reversible = isinstance(space, IReversibleForwardStateSpace)
        decisions = []
        seen = set()
        for initial in space.initial_states():
            for result in backtracking(initial): 
                yield result
    
    def first(self, space):
        return next(self.enumerate(space), None)

class PhoneSS(IForwardStateSpace): 
    def __init__(self, cad):
        dic = {}
        for elem in cad:
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1
        self.d = dic
        
    def initial_states(self):
        yield ("", 0)

    def is_final(self, s: "State"):
        #(res,num) = s
        return len(self.d) == 0

    def decisions(self, s: "State"):
        (res,num) = s
        #print("KK",res, self.d)
        if len(self.d) == 0: return
        for num in range(num, 10):
            oldDic = dict(self.d)
            if contained(self.d, word[num]):
                yield num #Phone(self.p+str(num), num+1, dic2)
            self.d = oldDic

    def decide(self, s: "State", num: "Decision"):    
        (res,_) = s      
        return (res+str(num), num)
    

T=int(f.readline())
P=[]
for i in range(T):
    p = f.readline().strip()
    P.append(p)

def solve(n):
    res = BacktrackingEnumerator().first(PhoneSS(n)) 
    if res==None: return res
    (initial, dec, final) = res     
    return final[0]
       
fRes = open("res.txt", "w")
case=0
for p in P:
    print(p)
    case+=1
    sol = solve(p)
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()