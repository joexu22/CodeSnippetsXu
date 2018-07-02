"""
NFAtoDFA.py
Python code that represent NFA and DFA
Converts NFA into DFA

Joe Xu
"""
from functools import reduce

class DFA:
	"""Class that encapsulates a DFA."""
	def __init__(self, transitionFunction, initialState, finalStates):
		self.delta = transitionFunction	
		self.q0 = initialState
		self.F = finalStates
	
	def deltaHat(self, state, inputString):
		for a in inputString: 
			state = self.delta[state][a]
		return state
	
	def inLanguage(self, inputString):
		return self.deltaHat(self.q0, inputString) in self.F
	
	# comments: 
	# 	* python dictionary keys must be immutable
	#	* it is a KeyError to extract an entry using a non-existent key

class NFA: 
	"""Class that encapsulates an NFA."""
	def __init__(self, transitionFunction, initialState, finalStates):
		self.delta = transitionFunction	
		self.q0 = initialState
		self.F = set(finalStates)
	
	def deltaHat(self, state, inputString):
		"""deltaHat is smart enough to return the empty set if no transition is defined."""
		states = set([state])
		for a in inputString: 
			newStates = set([])
			for state in states: 
				try: 
					newStates = newStates | self.delta[state][a]
				except KeyError: pass
			states = newStates
		return states
	
	def inLanguage(self, inputString):
		return len(self.deltaHat(self.q0, inputString) & self.F) > 0
	
	def alphabet(self):
		"""Returns the NFA's input alphabet, generated on the fly."""
		Sigma = reduce(lambda a,b:set(a)|set(b), [x.keys() for x in N.delta.values()])
		return Sigma
	
	def states(self):
		"""Returns the NFA's set of states, generated on the fly."""
		Q = set([self.q0]) | set(self.delta.keys()) | reduce(lambda a,b:a|b, reduce(lambda a,b:a+b, [x.values() for x in self.delta.values()]))	# {q0, all states with outgoing arrows, all with incoming arrows}
		return Q

def convertNFAtoDFA(N):
	"""Converts the input NFA into a DFA.  
	
	The output DFA has a state for every *reachable* subset of states in the input NFA.  
	In the worst case, there will be an exponential increase in the number of states.
	"""
	q0 = frozenset([N.q0])	# frozensets are hashable, so can key the delta dictionary
	Q = set([q0])
	unprocessedQ = Q.copy()	# unprocessedQ tracks states for which delta is not yet defined
	delta = {}
	F = []
	Sigma = N.alphabet()
	
	while len(unprocessedQ) > 0: 
		qSet = unprocessedQ.pop()
		delta[qSet] = {}
		for a in Sigma: 
			nextStates = reduce(lambda x,y: x|y, [N.deltaHat(q,a) for q in qSet])
			nextStates = frozenset(nextStates)
			delta[qSet][a] = nextStates
			if not nextStates in Q: 
				Q.add(nextStates)
				unprocessedQ.add(nextStates)
	for qSet in Q: 
		if len(qSet & N.F) > 0: 
			F.append(qSet)
	M = DFA(delta, q0, F)
	return M

delta = {'q0':{'0':set(['q0','q1']),'1':set(['q0'])}, 'q1':{'1':set(['q2'])}}
N = NFA(delta, 'q0', ['q2'])
N.deltaHat('q0', '0001')
print([(x, N.inLanguage(x)) for x in ['0001', '00010', '100101']])

M = convertNFAtoDFA(N)
print([(x, M.inLanguage(x)) for x in ['0001', '00010', '100101']])
# both the above lines should return [('0001', True), ('00010', False), ('100101', True)]

# to run the doctests, run python or python -v directly on this script
if __name__ == "__main__":
    import doctest
    doctest.testmod()