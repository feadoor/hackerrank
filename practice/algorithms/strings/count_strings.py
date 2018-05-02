#!/usr/local/bin/pypy3

from collections import namedtuple, defaultdict, deque
from itertools import count

Endpoints = namedtuple('Endpoints', ['start', 'end'])

ALTERNATION = '|'
CONCATENATION = '~'
KLEENE_STAR = '*'

MODULUS = 1000000007

class ModularMatrix:

    def __init__(self, values, modulus):
        assert len(values) > 0
        assert all(len(values[i]) == len(values[i+1]) for i in range(len(values) - 1))
        self.modulus = modulus
        self._values = [[values[i][j] % modulus for j in range(len(values[i]))] for i in range(len(values))]

    @property
    def m(self):
        return len(self._values)

    @property
    def n(self):
        return len(self._values[0])

    @staticmethod
    def identity(k, mod):
        assert k >= 0
        ans_values = [[0] * k for i in range(k)]
        for i in range(k):
            ans_values[i][i] = 1
        return ModularMatrix(ans_values, mod)

    def __getitem__(self, tup):
        i, j = tup
        return self._values[i][j]

    def __mul__(self, other):
        assert (self.modulus == other.modulus and self.n == other.m)
        modulus, m, n, l = self.modulus, self.m, other.n, self.n

        ans_values = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(l):
                    ans_values[i][j] += self[i, k] * other[k, j]

        return ModularMatrix(ans_values, modulus)

    def __pow__(self, k):
        assert (k >= 0 and self.m == self.n)
        modulus, n = self.modulus, self.n

        ans = ModularMatrix.identity(n, modulus)
        worker = ModularMatrix(self._values, modulus)

        while k:
            if k & 1:
                ans = (ans * worker)
            worker = (worker * worker)
            k >>= 1

        return ans

class NFA:

    def __init__(self, start, end, transitions):
        self.start = start
        self.end = end
        self.transitions = transitions
        self._epsilon_closures = {}

    def _epsilon_closure(self, state):
        if state in self._epsilon_closures:
            return self._epsilon_closures[state]

        stack, seen_states = [state], set()
        while len(stack):
            next_state = stack.pop()
            if next_state not in seen_states:
                seen_states.add(next_state)
                stack.extend(self.transitions[next_state][''])

        self._epsilon_closures[state] = seen_states
        return seen_states

    def get_all_starts(self):
        return self._epsilon_closure(self.start)

    def get_next_states(self, states):
        all_next_states = defaultdict(set)
        for state in states:
            for char, next_states in self.transitions[state].items():
                if char != '':
                    for next_state in next_states:
                        all_next_states[char].update(self._epsilon_closure(next_state))
        return all_next_states

class DFA:

    def __init__(self, start, ends, num_states, transitions):
        self.start = start
        self.ends = ends
        self.num_states = num_states
        self.transitions = transitions

    @classmethod
    def from_nfa(cls, nfa):
        start, ends, state_idxs, seen_states = 0, set(), defaultdict(count().__next__), set()
        transitions = defaultdict(dict)

        state_queue = deque([tuple(sorted(nfa.get_all_starts()))])
        while len(state_queue):
            states = state_queue.popleft()
            state_idx = state_idxs[states]
            seen_states.add(state_idx)
            for char, next_states in nfa.get_next_states(states).items():
                tupled_next_states = tuple(sorted(next_states))
                if nfa.end in next_states: ends.add(state_idxs[tupled_next_states])
                transitions[state_idx][char] = state_idxs[tupled_next_states]
                if state_idxs[tupled_next_states] not in seen_states:
                    state_queue.append(tupled_next_states)

        return cls(start, ends, len(state_idxs), transitions)

    def _transition_matrix(self):
        matrix = [[0 for _ in range(self.num_states)] for _ in range(self.num_states)]
        for state in self.transitions:
            for other in self.transitions[state].values():
                matrix[state][other] = 1
        return matrix

    def matches(self, length, modulus):
        transition_matrix = ModularMatrix(self._transition_matrix(), modulus)
        powered = pow(transition_matrix, length)
        return sum(powered[self.start, end] for end in self.ends) % MODULUS

def is_operator(char):
    return char == ALTERNATION or char == CONCATENATION or char == KLEENE_STAR

def regex_to_postfix(regex):
    postfix, working_stack, depth = [], [], 0
    for char in regex:
        if is_operator(char):
            working_stack.append(char)
        elif char == ')':
            if is_operator(working_stack[-1]):
                postfix.append(working_stack.pop())
            else:
                postfix.append(CONCATENATION)
            working_stack.pop()
        elif char == '(':
            working_stack.append('(')
        else:
            postfix.append(char)
    return postfix

def postfix_to_nfa(postfix):
    transitions, states, endpoints_stack = defaultdict(lambda: defaultdict(set)), 0, []

    def next_state():
        nonlocal states
        states += 1
        return states

    def handle_char(char):
        start, end = next_state(), next_state()
        transitions[start][char].add(end)
        endpoints_stack.append(Endpoints(start, end))

    def handle_concat():
        ends2, ends1 = endpoints_stack.pop(), endpoints_stack.pop()
        transitions[ends1.end][''].add(ends2.start)
        endpoints_stack.append(Endpoints(ends1.start, ends2.end))

    def handle_alternation():
        ends1, ends2 = endpoints_stack.pop(), endpoints_stack.pop()
        start, end = next_state(), next_state()
        transitions[start][''].update({ends1.start, ends2.start})
        transitions[ends1.end][''].add(end)
        transitions[ends2.end][''].add(end)
        endpoints_stack.append(Endpoints(start, end))

    def handle_kleene_star():
        ends = endpoints_stack.pop()
        start, end = next_state(), next_state()
        transitions[ends.end][''].update({end, ends.start})
        transitions[start][''].update({end, ends.start})
        endpoints_stack.append(Endpoints(start, end))

    for token in postfix:
        if token == CONCATENATION:
            handle_concat()
        elif token == ALTERNATION:
            handle_alternation()
        elif token == KLEENE_STAR:
            handle_kleene_star()
        else:
            handle_char(token)

    endpoints = endpoints_stack.pop()
    return NFA(endpoints.start, endpoints.end, transitions)

def main():
    for _ in range(int(input())):
        regex, length = input().strip().split(' ')
        postfix = regex_to_postfix(regex)
        nfa = postfix_to_nfa(postfix)
        dfa = DFA.from_nfa(nfa)
        print(dfa.matches(int(length), MODULUS))

if __name__ == '__main__':
    main()
