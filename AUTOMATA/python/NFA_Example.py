#!/usr/bin/python

class NFA:
    """
    Implementation of NFA...
    """
    def __init__(self, states, transitionFunction, )

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

class DFA:
    """
    DFA Implementation
    Note: using current_state may be an instance of "cheating" as it does add another tuple,
    but I'm thinking it can be elimated with a recursive call in run_with_input_list()
    """
    current_state = None;
    def __init__(self, states, alphabet, transition_table, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return;
    
    def transition_to_state_with_input(self, input_value):
        # match current_state and input_value to next state
        for transition in self.transition_table:
            if self.current_state == transition[0]:
                if input_value == transition[1]:
                    self.current_state = transition[2]
                    return;
        # else machine does not accept
        self.current_state = None;
        return;

    def in_accept_state(self):
        return self.current_state in self.accept_states;
    
    def go_to_initial_state(self):
        self.current_state = self.start_state;
        return;
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        for inp in input_list:
            self.transition_to_state_with_input(inp);
            continue;
        return self.in_accept_state();    
    pass;
    
def main():
    state_list = ('000', '001', '010', '011', '100', '101', '110', '111')
    alphabet = ('0','1')
    #transitions are (initial state, input, new state)
    transition_table = (['000', '0', '000'],['000', '1', '001'],['001', '0', '010'],['001', '1', '011'],
    ['010', '0', '100'],['010', '1', '101'],['011', '0', '110'],['011', '1', '111'],
    ['100', '0','000'],['100', '1', '001'],['101', '0','010'],['101', '1','011'],
    ['110', '0','100'],['110', '1','101'],['111', '0', '110'],['111','1', '111'])
    initial_state = '000'
    accept_state = ('100', '101', '110', '111')
    
    machine = DFA(state_list, alphabet, transition_table, initial_state, accept_state)

    try:
        input_string = list('000100');
        assert(machine.run_with_input_list(input_string) == True)
        input_string = list('10100101');
        assert(machine.run_with_input_list(input_string) == True)
        input_string = list('111111');
        assert(machine.run_with_input_list(input_string) == True)
        input_string = list('110');
        assert(machine.run_with_input_list(input_string) == True)
        input_string = list('101010');
        assert(machine.run_with_input_list(input_string) == False)
        input_string = list('000');
        assert(machine.run_with_input_list(input_string) == False)
        input_string = list('11011');
        assert(machine.run_with_input_list(input_string) == False)
        input_string = list('01001');
        assert(machine.run_with_input_list(input_string) == False)
    except AssertionError:
        print("Houston we have a problem...")
    
    try:
        input_string = list('000');        
        assert(machine.run_with_input_list(input_string) == True)
    except AssertionError:
        print("Expecting '000' to return False." )
    
    try:
        input_string = list('111');
        assert(machine.run_with_input_list(input_string) == False)
    except AssertionError:
        print("Expecting '111' to return True.")

main()
