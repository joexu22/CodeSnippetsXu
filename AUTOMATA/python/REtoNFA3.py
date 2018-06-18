# Define some special things
SPECIAL = '*|'
ALPHABET = '10'
EPSILON = None

# functions
def automaton_print(automaton):
    "Neatly prints the automaton"
    states, alphabet, start, final, transfer = automaton
    print('STATES  : ', states)
    print('ALPHABET: ', alphabet)
    print('START   : ', start)
    print('FINAL   : ', final)
    print('TABLE   : ', '(state, symbol)--->{states}')
    print('--------------------------------------')
    for key, value in sorted(transfer.items()):
        print('          ', key, ' ---- > ', value)


def merge_tables(table1, table2):
    """
    Merge the transition tables of two NFAs while renaming the states
    by appending _nfa1 and _nfa2 to the state names
    """
    table = {(key[0]+'_nfa1', key[1]): {i+'_nfa1' for i in value} for key, value in table1.items()}
    table.update({(key[0]+'_nfa2', key[1]): {i+'_nfa2' for i in value} for key, value in table2.items()})
    return table


def relabel_nfa(automaton):
    """
    Relabels automaton states and transitions with
    new numbers
    """
    states, alphabet, start, final, table = automaton

    state_relabels = {state: str(index + 1) for index, state in enumerate(states)}
    new_states = {state_relabels[i] for i in states}
    new_start = state_relabels[start]
    new_final = {state_relabels[i] for i in final}
    new_table = {(state_relabels[key[0]], key[1]): {state_relabels[i] for i in value}
                 for key, value in table.items()}
    new_automaton = (new_states, alphabet, new_start, new_final, new_table)
    return new_automaton


def concat(nfa1, nfa2):
    "Concatenate the two nfas"
    states1, _alphabet, start1, final1, table1 = nfa1
    states2, _alphabet, start2, final2, table2 = nfa2

    table = merge_tables(table1, table2)
    states = {i+'_nfa1' for i in states1}.union({i+'_nfa2' for i in states2})


    new_state_name_map = {name: str(1 + index) for index, name in enumerate(states)}
    new_state_name_map['end_nfa1'] = new_state_name_map['start_nfa2']  # These are the same states
    new_state_name_map['start_nfa1'] = 'start'
    new_state_name_map['end_nfa2'] = 'end'
    new_states = {new_state_name_map[i] for i in states}
    
    # Replace in table
    new_table = {}
    for key, value in table.items():
        new_key = (new_state_name_map[key[0]], key[1])
        if new_key not in new_table:
            new_table[new_key] = {new_state_name_map[i] for i in value}
    # Make the NFA
    NFA = (new_states, ALPHABET, 'start', {'end'}, new_table)
    return NFA


def union(nfa1, nfa2):
    """
    Make union of the two nfa
    """
    # Expand the nfas
    states1, _alphabet, start1, final1, table1 = nfa1
    states2, _alphabet, start2, final2, table2 = nfa2

    table = merge_tables(table1, table2)
    table.update({('start', EPSILON): {'start_nfa1', 'start_nfa2'},
                  ('end_nfa1', EPSILON): {'end'},
                  ('end_nfa2', EPSILON): {'end'},
                 })
    states = {i+'_nfa1' for i in states1}.union({i+'_nfa2' for i in states2})

    new_state_name_map = {name: str(1 + index) for index, name in enumerate(states)}
    new_state_name_map['start'] = 'start'
    new_state_name_map['end'] = 'end'
    states = states.union({'start', 'end'})
    new_states = {new_state_name_map[i] for i in states}

    # Replace in table
    new_table = {}
    for key, value in table.items():
        new_key = (new_state_name_map[key[0]], key[1])
        if new_key not in new_table:
            new_table[new_key] = {new_state_name_map[i] for i in value}
    # Make the NFA
    NFA = (new_states, ALPHABET, 'start', {'end'}, new_table)
    return NFA


def kleen(nfa):
    """
    Create kleen closure of this nfa
    """
    states, _alphabet, start, final, table = nfa
    new_state_name_map = {name: str(1 + index) for index, name in enumerate(states)}
    new_states = {new_state_name_map[i] for i in states}
    new_table = {(new_state_name_map[key[0]], key[1]): {new_state_name_map[i] for i in value}
                 for key, value in table.items()}
    new_states = new_states.union({'start', 'end'})
    new_table.update({('start', EPSILON):{'end', new_state_name_map['start']},
                      (new_state_name_map['end'], EPSILON):{'end', new_state_name_map['start']},
                      })
    NFA = (new_states, ALPHABET, 'start', {'end'}, new_table)
    return NFA


def make_nfa(pattern):
    """
    Make an NFA from a pattern
    """
    if isinstance(pattern, list):
        pattern = ''.join(pattern)
    assert all([i in ALPHABET + SPECIAL for i in pattern])  # everything is in ALPHABET + SPECIAL
    if len(pattern) > 1:
        head, *tail = pattern
        if tail[0] not in SPECIAL:
            NFA = concat(make_nfa(head), make_nfa(tail))
        else:
            symbol, *tail = tail
            if symbol == '|':
                other, *tail = tail
                union_nfa = union(make_nfa(head), make_nfa(other))
                NFA = concat(union_nfa, make_nfa(tail))
            if symbol == '*':
                NFA = concat(kleen(make_nfa(head)),
                             make_nfa(tail))
    elif len(pattern) == 1:  # single match
        states = {'start', 'end'}
        start = 'start'
        final = 'end'
        table = {('start', pattern): {'end'}}
        NFA = (states, ALPHABET, start, final, table)
    else:  # empty transition
        states = {'start', 'end'}
        start = 'start'
        final = 'end'
        table = {('start', EPSILON): {'end'}}
        NFA = (states, ALPHABET, start, final, table)
    return NFA


def epsilon_closure(state, table):
    """
    find epsilon closure of a given state
    using the given transition table
    """
    done, not_done = [], [state]
    # Build a tree with this state as root
    while not_done:
        to_do = []
        for s in not_done:
            epsilon_from_s = {tuple(v) for k, v in table.items() if ((k[0] == s) and (k[1] is None))}
            [to_do.append(i) for j in epsilon_from_s for i in j if i not in done]
            done.append(s)
        not_done = to_do
    return set(done)


def to_nfa_without_epsilon_transitions(nfa):
    """Removes epsilon transition from nfa"""
    states, alphabet, start, final, table = nfa

    closure_map = {i: frozenset(epsilon_closure(i, table)) for i in states}

    new_states = {closure_map[i] for i in states}
    new_start = closure_map[start]
    new_final = {i for i in closure_map.values() if any(((f in i) for f in final))}

    new_table = {}
    for new_state in new_states:
        for symbol in alphabet:
            key = (new_state, symbol)
            target = set()
            for member in new_state:
                if (member, symbol) in table.keys():
                    member_targets = table[(member, symbol)]
                    new_targets = {i for i in new_states  for mt in member_targets if mt in i}
                    target = target.union(new_targets)
            if len(target) > 0:
                new_table[key] = target

    # Relabel to avoid frozenset floods
    NFA = (new_states, alphabet, new_start, new_final, new_table)
    NFA = relabel_nfa(NFA)
    return NFA


def remove_unreachable(nfa):
    """
    Removes unreachable states and transitions
    from given nfa
    """
    states, alphabet, start, final, table = nfa
    new_states, new_final, new_table = set(), set(), dict()

    done, to_do = set(), set([start])
    while to_do:
        targets = set()
        for state in to_do - done:
            for symbol in alphabet:
                key = (state, symbol)
                if key in table.keys():
                    new_table[key] = table[key]
                    targets = targets.union(table[key])
            done.add(state)
        to_do = targets

    new_states = states.intersection(done)
    new_final = {i for i in final if i in done}

    NFA = (new_states, alphabet, start, new_final, new_table)
    return NFA


def to_dfa(nfa):
    """
    Convert given NFA to DFA
    NFA must be non epsilon move
    """
    states, alphabet, start, final, table = nfa
    new_table = dict()

    # We create states starting from the start state
    states_done, states_to_do = set(), [{start}]
    while states_to_do:
        target_list = []
        for current_states in states_to_do:
            for symbol in alphabet:
                target_states = set()
                for state in current_states:
                    key = (state, symbol)
                    if key in table:
                        targets = table[key]
                        target_states = target_states.union(targets)
                if (target_states not in states_done) or\
                   ((frozenset(current_states), symbol) not in new_table.keys()):
                       if len(target_states) > 0:
                           new_table[(frozenset(current_states), symbol)] = target_states
                states_done.add(frozenset(current_states))
                if len(target_states) > 0:
                    target_list.append(frozenset(target_states))
        states_to_do = set(target_list) - set(states_done)
    # start and end states
    new_start = frozenset({start})
    new_states = states_done
    new_final = {i for i in new_states if any(((f in i) for f in final))}

    state_relabels = {frozenset(state): str(index + 1) for index, state in enumerate(new_states)}
    new_states = {state_relabels[i] for i in new_states}
    new_start = state_relabels[new_start]
    new_final = {state_relabels[i] for i in new_final}
    new_table = {(state_relabels[key[0]], key[1]): state_relabels[frozenset(value)]
                 for key, value in new_table.items()}

    DFA = (new_states, alphabet, new_start, new_final, new_table)
    return DFA


def run_dfa(dfa, string):
    """
    Runs the given DFA on the given input string
    """
    states, alphabet, start, final, table = dfa
    current_state = start
    for symbol in string:
        if symbol not in alphabet:
            return False
        key = (current_state, symbol)
        try:
            current_state = table[key]
        except KeyError:
            return False
    return current_state in final


if __name__ == '__main__':
    pattern = '0|10*'
    print(pattern)
    automaton = make_nfa(pattern)
    automaton = to_nfa_without_epsilon_transitions(automaton)
    automaton = remove_unreachable(automaton)
    automaton = to_dfa(automaton)
    automaton_print(automaton)

    strings_to_run_on = ['1',
                         '0',
                         '01',
                         '100',
                         '11111'
                        ]
    for string in strings_to_run_on:
        print(string, run_dfa(automaton, string))

    def test():
        "Test stuff"
        def test_epsilon_closure():
            state = '1'
            table = {('1', None): {'2', '3', '4'},
                     ('2', '1'): {'5'},
                     ('3', '1'): {'4'},
                     ('4', None): {'6', '7'},
                     ('4', '1'): {'9'},
                     ('6', None): {'2', '8'},
                     ('7', None): {'1'},
                     ('8', None): {'3'}
                    }
            x = (epsilon_closure(state, table))
            assert set(x) == {'1', '2', '3', '4', '6', '7', '8'}
            print('Epsilon closure working ok')
    # Run the tests
    test()