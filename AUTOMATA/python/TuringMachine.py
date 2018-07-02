#!/usr/bin/python


class TurningMachine:
    """
    This is an implementation of a Turning Machine
    """
    accepting = None;
    def __init__(self, states, input_alphabet, tape_alphabet, transition_table,
        start_state, accept_state, reject_state):
        """
        Q is the set of states,
        Σ is the input alphabet not containing the blank symbol
        Γ is the tape alphabet, where ∈ Γ and Σ ⊆ Γ
        δ : Q × Γ−→Q × Γ × {L, R} is the transition function
        q0 ∈ Q is the start state
        q accept ∈ Q is the accept state
        q reject ∈ Q is the reject state, where q reject 6 = q accept
        """
        self.Q = states
        self.Sigma = input_alphabet
        self.Gamma = tape_alphabet
        self.d = transition_table
        self.q0 = start_state
        self.qA = accept_state
        self.qR = reject_state
        return;
    
    def accept_string(self, w):
        #! test elements of w to see if they are included in Σ
        #! change self.Gamma into "tape" like structure, left to right, with w and then <blank symbol>
        pass

    pass;
    

def main():
    return;

main()
